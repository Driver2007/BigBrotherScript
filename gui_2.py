# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.email_addresses=[]
        self.sms_numbers=[]
        self.sms_em_only_chb=[]
        self.tango_attributes=[]
        self.value_label=[]
        self.limit_value_c=[]
        self.limit_value_p=[]
        self.label_x10=[]
        self.tango_em_attr_chb=[]
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 561, 440))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.send_email_to_chb = QtWidgets.QCheckBox(self.tab)
        self.send_email_to_chb.setGeometry(QtCore.QRect(10, 10, 221, 22))
        self.send_email_to_chb.setObjectName("send_email_to_chb")
        self.send_sms_to_chb = QtWidgets.QCheckBox(self.tab)
        self.send_sms_to_chb.setGeometry(QtCore.QRect(10, 140, 121, 22))
        self.send_sms_to_chb.setObjectName("send_sms_to_chb")
        self.stop_pb = QtWidgets.QPushButton(self.tab)
        self.stop_pb.setGeometry(QtCore.QRect(120, 320, 99, 27))
        self.stop_pb.setObjectName("stop_pb")
        self.start_pb = QtWidgets.QPushButton(self.tab)
        self.start_pb.setGeometry(QtCore.QRect(10, 320, 99, 27))
        self.start_pb.setObjectName("start_pb")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 40, 541, 95))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        for i in range(3):
            self.email_addresses.append(QtWidgets.QLineEdit(self.widget))
            self.email_addresses[i].setObjectName("email_{}".format(i))
            self.verticalLayout_4.addWidget(self.email_addresses[i])
            
        self.splitter_10 = QtWidgets.QSplitter(self.tab)
        self.splitter_10.setGeometry(QtCore.QRect(10, 170, 541, 95))
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.widget1 = QtWidgets.QWidget(self.splitter_10)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        for i in range(3):
            self.sms_numbers.append(QtWidgets.QLineEdit(self.widget1))
            self.sms_numbers[i].setObjectName("sms_{}".format(i))
            self.verticalLayout_5.addWidget(self.sms_numbers[i])
        
        
        self.widget2 = QtWidgets.QWidget(self.splitter_10)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        for i in range(3):
            self.sms_em_only_chb.append(QtWidgets.QCheckBox(self.widget2))
            self.sms_em_only_chb[i].setObjectName("sms_em_only_chb_{}".format(i))
            self.verticalLayout_6.addWidget(self.sms_em_only_chb[i])
        

            
        self.splitter_11 = QtWidgets.QSplitter(self.tab)
        self.splitter_11.setGeometry(QtCore.QRect(20, 270, 314, 27))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label = QtWidgets.QLabel(self.splitter_11)
        self.label.setObjectName("label")
        self.period = QtWidgets.QLineEdit(self.splitter_11)
        self.period.setObjectName("period")
        self.label_2 = QtWidgets.QLabel(self.splitter_11)
        self.label_2.setObjectName("label_2")
        self.widget3 = QtWidgets.QWidget(self.tab)
        self.widget3.setGeometry(QtCore.QRect(230, 300, 321, 42))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.last_mail_l = QtWidgets.QLabel(self.widget3)
        self.last_mail_l.setText("")
        self.last_mail_l.setObjectName("last_mail_l")
        self.verticalLayout_7.addWidget(self.last_mail_l)
        self.next_mail_l = QtWidgets.QLabel(self.widget3)
        self.next_mail_l.setText("")        
        self.next_mail_l.setObjectName("next_mail_l")
        self.verticalLayout_7.addWidget(self.next_mail_l)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(320, 10, 221, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(320, 140, 191, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(10, 385, 191, 17))
        self.label_15.setObjectName("label_15")
        
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(10, 360, 191, 17))
        self.label_16.setObjectName("label_16")
        self.upload_progress = QtWidgets.QProgressBar(self.tab)
        self.upload_progress.setGeometry(QtCore.QRect(130, 357, 118, 23))
        self.upload_progress.setProperty("value", 0)
        self.upload_progress.setObjectName("upload_progress")

        self.tabWidget.addTab(self.tab, "")
        self.control = QtWidgets.QWidget()
        self.control.setObjectName("control")
        self.label_3 = QtWidgets.QLabel(self.control)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.control)
        self.label_4.setGeometry(QtCore.QRect(380, 10, 41, 17))
        self.label_4.setObjectName("label_4")
        self.screenshot_chb = QtWidgets.QCheckBox(self.control)
        self.screenshot_chb.setGeometry(QtCore.QRect(10, 320, 301, 22))
        self.screenshot_chb.setObjectName("screenshot_chb")
        self.file_chb = QtWidgets.QCheckBox(self.control)
        self.file_chb.setGeometry(QtCore.QRect(10, 345, 220, 22))
        self.file_chb.setObjectName("file_chb")
        self.filepath = QtWidgets.QLineEdit(self.control)
        self.filepath.setGeometry(QtCore.QRect(220, 345, 300, 22))        
        self.filepath.setObjectName("filepath")
        
        self.label_6 = QtWidgets.QLabel(self.control)
        self.label_6.setGeometry(QtCore.QRect(180, 380, 41, 17))
        self.label_6.setObjectName("label_6")
        self.filename = QtWidgets.QLineEdit(self.control)
        self.filename.setGeometry(QtCore.QRect(220, 380, 300, 22))        
        self.filename.setObjectName("filenaem")  
        
        self.splitter = QtWidgets.QSplitter(self.control)
        self.splitter.setGeometry(QtCore.QRect(40, 40, 191, 270))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.splitter.setHandleWidth(10)
        
        self.layoutWidget = QtWidgets.QWidget(self.control)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 40, 121, 270))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.widget4 = QtWidgets.QWidget(self.control)
        self.widget4.setGeometry(QtCore.QRect(10, 35, 22, 280))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        for i in range(8):
            self.tango_attributes.append(QtWidgets.QLineEdit(self.splitter))
            self.tango_attributes[i].setObjectName("tango_attribute_{}".format(i))
        
            self.value_label.append(QtWidgets.QLabel(self.layoutWidget))
            self.value_label[i].setObjectName("value_label_{}".format(i))
            self.verticalLayout.addWidget(self.value_label[i])
            
            self.tango_em_attr_chb.append(QtWidgets.QCheckBox(self.widget4))
            self.tango_em_attr_chb[i].setText("")
            self.tango_em_attr_chb[i].setObjectName("tango_em_attr_chb")
            self.verticalLayout_3.addWidget(self.tango_em_attr_chb[i])
            
        self.label_5 = QtWidgets.QLabel(self.control)
        self.label_5.setGeometry(QtCore.QRect(240, 10, 41, 17))
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(self.control)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 21, 20))
        self.label_12.setObjectName("label_12")
        
        d=206
        self.widget = QtWidgets.QWidget(self.control)
        self.widget.setGeometry(QtCore.QRect(370, 40, 61, d))
        self.widget.setObjectName("widget")        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.widget1 = QtWidgets.QWidget(self.control)
        self.widget1.setGeometry(QtCore.QRect(490, 40, 61, d))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        
        self.layoutWidget4 = QtWidgets.QWidget(self.control)
        self.layoutWidget4.setGeometry(QtCore.QRect(240, 40, 121, 201))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.widget2 = QtWidgets.QWidget(self.control)
        self.widget2.setGeometry(QtCore.QRect(445, 40, 41, d))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        

        
 
        for i in range(6):
            self.limit_value_c.append(QtWidgets.QSpinBox(self.widget))
            self.limit_value_c[i].setMinimum(1)
            self.limit_value_c[i].setMaximum(9)
            self.limit_value_c[i].setObjectName("value_coef_{}".format(i))
            self.verticalLayout_2.addWidget(self.limit_value_c[i])
            
            self.limit_value_p.append(QtWidgets.QSpinBox(self.widget1))
            self.limit_value_p[i].setMinimum(-15)
            self.limit_value_p[i].setMaximum(20)
            self.limit_value_p[i].setObjectName("value_power_{}".format(i))
            self.verticalLayout_9.addWidget(self.limit_value_p[i])
            
            #self.value_label.append(QtWidgets.QLabel(self.layoutWidget4))
            #self.value_label[i].setObjectName("value_label_{}".format(i))
            #self.value_label[i].setText("")
            #self.verticalLayout.addWidget(self.value_label[i])
            
            self.label_x10.append(QtWidgets.QLabel(self.widget2))
            self.label_x10[i].setObjectName("label_x10_{}".format(i))
            self.verticalLayout_10.addWidget(self.label_x10[i])
        

        
        self.widget5 = QtWidgets.QWidget(self.control)
        self.widget5.setGeometry(QtCore.QRect(240, 240, 121, 71))
        self.widget5.setObjectName("widget5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.OnOff_L_7 = QtWidgets.QLabel(self.widget5)
        self.OnOff_L_7.setObjectName("OnOff_L_7")
        self.verticalLayout_8.addWidget(self.OnOff_L_7)
        self.OnOff_L_8 = QtWidgets.QLabel(self.widget5)
        self.OnOff_L_8.setObjectName("OnOff_L_8")
        self.verticalLayout_8.addWidget(self.OnOff_L_8)
        self.tabWidget.addTab(self.control, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_email_to_chb.setText(_translate("MainWindow", "send email to:"))
        self.send_sms_to_chb.setText(_translate("MainWindow", "send SMS to:"))
        self.stop_pb.setText(_translate("MainWindow", "Stop"))
        self.start_pb.setText(_translate("MainWindow", "Start"))
        for i in range(3):
            self.sms_em_only_chb[i].setText(_translate("MainWindow", "emergency only"))
        self.label.setText(_translate("MainWindow", "Send message every "))
        self.label_13.setText(_translate("MainWindow", "example: example@domain.com"))
        self.label_14.setText(_translate("MainWindow", "example: +4917612345678"))
        self.label_16.setText(_translate("MainWindow", "Upload progress"))
        self.label_2.setText(_translate("MainWindow", "min"))
        self.last_mail_l.setText(_translate("MainWindow", ""))
        self.next_mail_l.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Communication"))
        self.label_3.setText(_translate("MainWindow", "Tango attribute"))
        self.label_4.setText(_translate("MainWindow", "Limit"))
        self.label_6.setText(_translate("MainWindow", "file name"))
        self.screenshot_chb.setText(_translate("MainWindow", "Attach screenshot to email"))
        self.file_chb.setText(_translate("MainWindow", "Attach file to email, path:"))
        self.label_5.setText(_translate("MainWindow", "Value"))
        self.label_12.setText(_translate("MainWindow", "Em"))
        for i in range(6):
            self.value_label[i].setText(_translate("MainWindow", ""))
            self.label_x10[i].setText(_translate("MainWindow", "x10^"))
        
        self.OnOff_L_7.setText(_translate("MainWindow", ""))
        self.OnOff_L_8.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control), _translate("MainWindow", "Control"))
