#!/usr/bin/env python3
from __future__ import print_function
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from gui_2 import Ui_MainWindow
import sys
import PyTango
import os
import configparser
import subprocess
import pdb
import time

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
import pickle
import os.path
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import googleapiclient.http
from httplib2 import Http
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import threading

SETTINGS="settings.ini"
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.start_trigger=False
        self.config = configparser.ConfigParser()
        if not "control" in self.config:
            self.config["control"] = {}
        if not "email" in self.config:
            self.config["email"] = {}
        if not "sms" in self.config:
            self.config["sms"] = {}
        if not "communication" in self.config:
            self.config["communication"] = {}
        
        self.attributes=[]
        self.devices=[]
        self.attribute_value=[]
        
        self.emergency=False
        self.message_sent=False
        self.email_trigger=False
        self.upload_trigger=False
        self.upload_running=False
        self.uploaded_trigger=False
        self.file_link=""  
        self.last_upload=""
 
        
        self.nowhour=25

        self.ui.start_pb.clicked.connect(self.start)
        self.ui.stop_pb.clicked.connect(self.stop)
        

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)


        self.timer2 = QtCore.QTimer(self)
        self.timer2.timeout.connect(self.update_current_values)
        
        if not 'upload_thread' in dir(self):
            self.upload_thread = threading.Thread(target=self.upload)
            self.upload_thread.setDaemon(True)
            self.upload_thread.start()
        if not 'email_thread' in dir(self):
            self.email_thread = threading.Thread(target=self.email)
            self.email_thread.setDaemon(True)
            self.email_thread.start()

        if os.path.isfile(SETTINGS)==True:
            self.read_settings()
        else:        
            self.timer2.setInterval(1000)
            self.timer2.start()
            

        
    def read_settings(self):
        self.tango_link=[]
        self.limits=[]
        self.config.read("settings.ini")
        if "control" in self.config.sections():
            control=self.config["control"]
            i=0
            for link in control:
                if "tango_link" in link:    
                    self.tango_link.append(self.config["control"]["tango_link_"+str(i)].replace("+", "/"))
                    self.limits.append(self.config["control"]["tango_value_"+str(i)])
                    
                    if self.tango_link[i]!="":
                        if i<6:
                            self.ui.tango_attributes[i].setText(self.tango_link[i])
                            coef,power=self.limits[i].split("e")                
                            self.ui.limit_value_c[i].setValue(int(coef))           
                            self.ui.limit_value_p[i].setValue(int(power))
                        elif i>=6:
                            self.ui.tango_attributes[i].setText(self.tango_link[i])
                    i+=1
        if "email" in self.config.sections():
            email=self.config["email"]
            e=0
            for link in email:
                if "@" in link:
                    self.ui.email_addresses[e].setText(self.config["email"][link])
                    e+=1
                    
        if "sms" in self.config.sections():
            sms=self.config["sms"]
            s=0
            for link in sms:
                if "+" in link:
                    self.ui.sms_numbers[s].setText(self.config["sms"][link])
                    s+=1

        if "communication" in self.config.sections():
            communication=self.config["communication"]
            
            if "filepath" in communication:
                self.ui.filepath.setText(self.config["communication"]["filepath"])
            if "send_email_to_chb" in communication:
                if self.config["communication"]["send_email_to_chb"]=="True":
                    self.ui.send_email_to_chb.setChecked(True)
            if "send_sms_to_chb" in communication:
                if self.config["communication"]["send_sms_to_chb"]=="True":
                    self.ui.send_sms_to_chb.setChecked(True)
            if "screenshot_chb" in communication:
                if self.config["communication"]["screenshot_chb"]=="True":
                    self.ui.screenshot_chb.setChecked(True)
            if "file_chb" in communication:
                if self.config["communication"]["file_chb"]=="True":
                    self.ui.file_chb.setChecked(True)
            for i in range(3):
                if "sms_em_only_chb_"+str(i) in communication:
                    if self.config["communication"]["sms_em_only_chb_"+str(i)]=="True":
                        self.ui.sms_em_only_chb[i].setChecked(True)
            for i in range(6):
                if "tango_em_attr_chb_"+str(i) in communication:
                    if self.config["communication"]["tango_em_attr_chb_"+str(i)]=="True":
                        self.ui.tango_em_attr_chb[i].setChecked(True)

        self.timer2.setInterval(1000)
        self.timer2.start()
        return
        
    def start(self):

        with open(SETTINGS, 'w') as configfile:
            self.config.write(configfile)
        self.timer.setInterval(1000)
        self.timer.start()
        
    def stop(self):
        self.timer.stop()
        
    def check_tango_link(self, link):
        s=0
        for i in range(len(link)):
           if link[i]=="/":
               s+=1
        return s
        
    
    def message(self,title,text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()
        

    def upload(self):
        """send file(s) to google cloud"""
        while True:
            if self.upload_trigger==True:
                self.upload_running=True
                self.upload_trigger=False
                self.path=self.ui.filepath.text()
                self.filename=self.ui.filename.text()
                archived=False
                filepath=os.path.join(self.path,self.filename)
                if os.path.isfile(filepath):
                    self.ui.label_15.setText("Archiving file!")
                    while archived==False:
                        process=subprocess.Popen(["zip","-j","-1",filepath+".zip",filepath], stdout=subprocess.PIPE)
                        stdout = process.communicate()[0]
                        stdout='STDOUT:{}'.format(stdout)
                        if "warning" not in stdout:
                            archived=True
                        
                    self.ui.label_15.setText("Uploading file!")
                    creds = None
                    if os.path.exists('token.pickle'):
                        with open('token.pickle', 'rb') as token:
                            creds = pickle.load(token)
                            # If there are no (valid) credentials available, let the user log in.
                    if not creds or not creds.valid:
                        if creds and creds.expired and creds.refresh_token:
                            creds.refresh(Request())
                        else:
                            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                            creds = flow.run_local_server(port=0)
                            # Save the credentials for the next run
                        with open('token.pickle', 'wb') as token:
                            pickle.dump(creds, token)
                    service = build('drive', 'v3', credentials=creds)
                
                    # Call the Drive v3 API
                    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
                    items = results.get('files', [])
                    if items:
                        for item in items:
                            if self.filename+".zip"==item['name']:
                                service.files().delete(fileId=item['id']).execute()
                    media = MediaFileUpload(self.filename+".zip", mimetype='application/zip', chunksize=256*1024, resumable=True)
                
                    file_metadata = {'name': self.filename+".zip"}
                        
                    file = service.files().create(body=file_metadata,
                                                    media_body=media,
                                                    fields='id')
    
                    response = None
                    while not response:
                        status, response = file.next_chunk()
                        if status:
                            self.ui.upload_progress.setProperty("value", int(status.progress() * 100))
                            
                    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
                    items = results.get('files', [])
                    if items:
                        for item in items:
                            if self.filename+".zip"==item['name']:
                                self.file_link="https://drive.google.com/file/d/" + item['id']+'/view'
                    print ("Your sharable link: "+ self.file_link)
                    self.upload_running=False
                    self.last_upload="File uploaded at "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"!"
                    self.ui.upload_progress.setProperty("value", 0)
                    self.email_trigger=True
            time.sleep(1)

        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        
    
    def email(self):
        while True:
            time.sleep(1)
            if self.email_trigger==True:
                self.email_trigger=False
                msg = MIMEMultipart()
                gmail_user = "pressure.uni.mainz@gmail.com"
                gmail_pwd = "pressureunimainz"
                FROM = "pressure.uni.mainz@gmail.com"
                TO = []        
                for i in range (len(self.ui.email_addresses)):
                    if self.ui.email_addresses[i].text()!="":
                        TO.append(str(self.ui.email_addresses[i].text()))
                if self.emergency==True:
                    SUBJECT = "WARNING! Microscope status"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                elif self.emergency==False:
                    SUBJECT = "Microscope status"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
                TEXT = ""
                for i in range(len(self.ui.tango_attributes)):
                    if self.ui.tango_attributes[i].text()!="":
                        if i<6:
                            TEXT += "Parameter "+ self.ui.tango_attributes[i].text()+"="+str(self.attribute_value[i])+". Limit is "+str(self.ui.limit_value_c[i].value())+"e"+str(self.ui.limit_value_p[i].value())+"\n"
                        else:
                            if self.attribute_value[i]==True:
                                TEXT += "Parameter "+ self.ui.tango_attributes[i].text()+" is ON\n"

                            elif self.attribute_value[i]==False:
                                TEXT += "Parameter "+ self.ui.tango_attributes[i].text()+" is OFF\n"
                if self.ui.file_chb.isChecked():
                    TEXT+=("Link to downdload lat measured file "+ self.file_link)+"\n"
                print (TEXT)
                if self.ui.screenshot_chb.isChecked():
                    screenshot_path="screenshot.png"
                    subprocess.run(["scrot", screenshot_path])
                    with open(screenshot_path, "rb") as file:
                        part = MIMEApplication(file.read(),Name=os.path.basename(screenshot_path))
                msg.attach(part)
        

                msg.attach(MIMEText(TEXT))

                try:
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    server.ehlo()
                    server.login(gmail_user, gmail_pwd)
                    server.sendmail(FROM, TO, msg.as_string())
                    self.ui.label_15.setText("successfully sent the mail at "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    print ('successfully sent the mail')
                except:
                    self.ui.label_15.setText("failed to send mail")
                    print ("failed to send mail")
            

        
    def update(self):
        for i in range(len(self.attribute_value)):
            if self.ui.tango_attributes[i].text()!="" and self.emergency==False:
                if self.attribute_value=="not recognized":
                    continue
                if i<6:
                    value=float(self.attribute_value[i])
                    limit=float(int(self.ui.limit_value_c[i].value())*(10**int(self.ui.limit_value_p[i].value())))
                    if value>limit:
                        print ("linit1")
                        self.emergency=True
                        self.email_trigger=True
                if i>=6:
                    value=bool(self.attribute_value[i])
                    if value!=True:
                        print ("limit2")
                        self.emergency=True
                        self.email_trigger=True
        if os.path.isfile(self.ui.filepath.text()):
            print(True)
        now = datetime.datetime.now()
        if self.nowhour!=now.hour:
            self.nowhour=now.hour
            if self.ui.file_chb.isChecked():
                self.upload_trigger=True
            else:
                self.email_trigger=True
        if self.last_upload!="":
            self.ui.label_15.setText("File uploaded at "+self.last_upload+"!")
                    

        
            
    def update_current_values(self):
        self.attribute_value=[0.0]*len(self.ui.tango_attributes)
        for i in range(len(self.ui.tango_attributes)):
            if self.ui.tango_attributes[i].text()!="":

                try:
                    temp_link=self.ui.tango_attributes[i].text()
                    device=temp_link[0:temp_link.rfind("/")]
                    attribute=temp_link[temp_link.rfind("/")+1:len(temp_link)]
                    if i<6:
                        self.attribute_value[i]=PyTango.DeviceProxy(device).read_attribute(attribute).value
                        self.ui.value_label[i].setText('%.2E' % self.attribute_value[i])
                        self.config["control"]["tango_link_"+str(i)]=str(device+"+"+attribute)
                        self.config["control"]["tango_value_"+str(i)]=str(self.ui.limit_value_c[i].value())+"e"+str(self.ui.limit_value_p[i].value())
                    if i>=6:
                        self.attribute_value[i]=PyTango.DeviceProxy(device).read_attribute(attribute).value
                        self.ui.value_label[i].setText(str(self.attribute_value[i]))                        
                        self.config["control"]["tango_link_"+str(i)]=str(device+"+"+attribute)
                #else:
                except:
                    self.ui.value_label[i].setText("not recognized")
                    self.config["control"]["tango_link_"+str(i)]=""
                    self.config["control"]["tango_value_"+str(i)]="" 
                
            else:
                self.ui.value_label[i].setText("")
                self.config["control"]["tango_link_"+str(i)]=""
                self.config["control"]["tango_value_"+str(i)]=""
                
                
                
        for i in range (len(self.ui.email_addresses)):
            if self.ui.email_addresses[i].text()!="":
                self.config["email"]["@"+str(i)]=str(self.ui.email_addresses[i].text())
        for i in range (len(self.ui.sms_numbers)):
            if self.ui.sms_numbers[i].text()!="":
                self.config["sms"]["+"+str(i)]=str(self.ui.sms_numbers[i].text())
                
        if self.ui.filepath.text()!="":
            self.config["communication"]["filepath"]=self.ui.filepath.text()
            
        if self.ui.send_email_to_chb.isChecked():
            self.config["communication"]["send_email_to_chb"]="True"
        else:
            self.config["communication"]["send_email_to_chb"]="False"
           
        if self.ui.send_sms_to_chb.isChecked():
            self.config["communication"]["send_sms_to_chb"]="True"
        else:
            self.config["communication"]["send_sms_to_chb"]="False"

        if self.ui.file_chb.isChecked():
            self.config["communication"]["file_chb"]="True"
        else:
            self.config["communication"]["file_chb"]="False"

        if self.ui.screenshot_chb.isChecked():
            self.config["communication"]["screenshot_chb"]="True"
        else:
            self.config["communication"]["screenshot_chb"]="False"

        for i in range(3):
            if self.ui.sms_em_only_chb[i].isChecked():
                self.config["communication"]["sms_em_only_chb_"+str(i)]="True"
            else:
                self.config["communication"]["sms_em_only_chb_"+str(i)]="Fasle"
        
        for i in range(6):
            if self.ui.tango_em_attr_chb[i].isChecked():
                self.config["communication"]["tango_em_attr_chb_"+str(i)]="True"
            else:
                self.config["communication"]["tango_em_attr_chb_"+str(i)]="Fasle"
            
            
        #with open(SETTINGS, 'w') as configfile:
            #self.config.write(configfile)
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()