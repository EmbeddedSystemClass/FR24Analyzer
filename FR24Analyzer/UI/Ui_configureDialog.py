# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cmb/Workspace/FR24_Analyzer/FR24Analyzer/UI/configureDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_configureDialog(object):
    def setupUi(self, configureDialog):
        configureDialog.setObjectName("configureDialog")
        configureDialog.resize(503, 456)
        configureDialog.setModal(False)
        self.frame = QtWidgets.QFrame(configureDialog)
        self.frame.setGeometry(QtCore.QRect(10, 390, 481, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 464, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(75, 29))
        self.label.setMaximumSize(QtCore.QSize(75, 29))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(300, 29))
        self.textBrowser.setMaximumSize(QtCore.QSize(301, 29))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.configureBrowseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.configureBrowseButton.setMinimumSize(QtCore.QSize(75, 29))
        self.configureBrowseButton.setMaximumSize(QtCore.QSize(75, 29))
        self.configureBrowseButton.setObjectName("configureBrowseButton")
        self.horizontalLayout.addWidget(self.configureBrowseButton)
        self.frame_2 = QtWidgets.QFrame(configureDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 341, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 322, 204))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setMinimumSize(QtCore.QSize(150, 29))
        self.label_7.setMaximumSize(QtCore.QSize(150, 29))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setMinimumSize(QtCore.QSize(150, 29))
        self.label_4.setMaximumSize(QtCore.QSize(250, 29))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setMinimumSize(QtCore.QSize(150, 29))
        self.label_6.setMaximumSize(QtCore.QSize(150, 29))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.airportName = QtWidgets.QTextEdit(self.layoutWidget1)
        self.airportName.setMinimumSize(QtCore.QSize(150, 29))
        self.airportName.setMaximumSize(QtCore.QSize(150, 29))
        self.airportName.setToolTip("")
        self.airportName.setWhatsThis("")
        self.airportName.setObjectName("airportName")
        self.verticalLayout_4.addWidget(self.airportName)
        self.airportLat = QtWidgets.QTextEdit(self.layoutWidget1)
        self.airportLat.setMinimumSize(QtCore.QSize(150, 29))
        self.airportLat.setMaximumSize(QtCore.QSize(150, 29))
        self.airportLat.setToolTip("")
        self.airportLat.setWhatsThis("")
        self.airportLat.setObjectName("airportLat")
        self.verticalLayout_4.addWidget(self.airportLat)
        self.airportLon = QtWidgets.QTextEdit(self.layoutWidget1)
        self.airportLon.setMinimumSize(QtCore.QSize(150, 29))
        self.airportLon.setMaximumSize(QtCore.QSize(150, 29))
        self.airportLon.setToolTip("")
        self.airportLon.setWhatsThis("")
        self.airportLon.setObjectName("airportLon")
        self.verticalLayout_4.addWidget(self.airportLon)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setMinimumSize(QtCore.QSize(75, 29))
        self.label_8.setMaximumSize(QtCore.QSize(75, 29))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setMinimumSize(QtCore.QSize(75, 29))
        self.label_9.setMaximumSize(QtCore.QSize(75, 29))
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setMinimumSize(QtCore.QSize(75, 29))
        self.label_10.setMaximumSize(QtCore.QSize(75, 29))
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.areaLayout = QtWidgets.QVBoxLayout()
        self.areaLayout.setObjectName("areaLayout")
        self.areaLat = QtWidgets.QTextEdit(self.layoutWidget1)
        self.areaLat.setMinimumSize(QtCore.QSize(150, 29))
        self.areaLat.setMaximumSize(QtCore.QSize(150, 29))
        self.areaLat.setToolTip("")
        self.areaLat.setWhatsThis("")
        self.areaLat.setObjectName("areaLat")
        self.areaLayout.addWidget(self.areaLat)
        self.areaLon = QtWidgets.QTextEdit(self.layoutWidget1)
        self.areaLon.setMinimumSize(QtCore.QSize(150, 29))
        self.areaLon.setMaximumSize(QtCore.QSize(150, 29))
        self.areaLon.setToolTip("")
        self.areaLon.setWhatsThis("")
        self.areaLon.setObjectName("areaLon")
        self.areaLayout.addWidget(self.areaLon)
        self.horizontalLayout_3.addLayout(self.areaLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.frame_3 = QtWidgets.QFrame(configureDialog)
        self.frame_3.setGeometry(QtCore.QRect(10, 270, 341, 111))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(12, 12, 146, 16))
        self.label_11.setObjectName("label_11")
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(14, 35, 312, 68))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setMinimumSize(QtCore.QSize(150, 29))
        self.label_12.setMaximumSize(QtCore.QSize(150, 29))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setMinimumSize(QtCore.QSize(150, 29))
        self.label_13.setMaximumSize(QtCore.QSize(250, 29))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.redisIP = QtWidgets.QTextEdit(self.layoutWidget2)
        self.redisIP.setMinimumSize(QtCore.QSize(150, 29))
        self.redisIP.setMaximumSize(QtCore.QSize(150, 29))
        self.redisIP.setToolTip("")
        self.redisIP.setWhatsThis("")
        self.redisIP.setObjectName("redisIP")
        self.verticalLayout_8.addWidget(self.redisIP)
        self.postgresIP = QtWidgets.QTextEdit(self.layoutWidget2)
        self.postgresIP.setMinimumSize(QtCore.QSize(150, 29))
        self.postgresIP.setMaximumSize(QtCore.QSize(150, 29))
        self.postgresIP.setToolTip("")
        self.postgresIP.setWhatsThis("")
        self.postgresIP.setObjectName("postgresIP")
        self.verticalLayout_8.addWidget(self.postgresIP)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.label_2 = QtWidgets.QLabel(configureDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 421, 16))
        self.label_2.setObjectName("label_2")
        self.saveConfig = QtWidgets.QPushButton(configureDialog)
        self.saveConfig.setGeometry(QtCore.QRect(390, 350, 100, 29))
        self.saveConfig.setMinimumSize(QtCore.QSize(100, 29))
        self.saveConfig.setMaximumSize(QtCore.QSize(75, 29))
        self.saveConfig.setObjectName("saveConfig")

        self.retranslateUi(configureDialog)
        QtCore.QMetaObject.connectSlotsByName(configureDialog)

    def retranslateUi(self, configureDialog):
        _translate = QtCore.QCoreApplication.translate
        configureDialog.setWindowTitle(_translate("configureDialog", "Configure FR24 Analyzer"))
        self.label.setText(_translate("configureDialog", "From File"))
        self.configureBrowseButton.setText(_translate("configureDialog", "Browse"))
        self.label_5.setText(_translate("configureDialog", "Geographical Paramters"))
        self.label_7.setText(_translate("configureDialog", "Airport Name"))
        self.label_4.setText(_translate("configureDialog", "Airport Lattitude"))
        self.label_6.setText(_translate("configureDialog", "Airport Longtitude"))
        self.label_8.setText(_translate("configureDialog", "Area"))
        self.label_9.setText(_translate("configureDialog", "Lattitude"))
        self.label_10.setText(_translate("configureDialog", "Longtitude"))
        self.label_11.setText(_translate("configureDialog", "Network Paramters"))
        self.label_12.setText(_translate("configureDialog", "Redis IP"))
        self.label_13.setText(_translate("configureDialog", "Postgres IP"))
        self.label_2.setText(_translate("configureDialog", "Enter the required paramteres or choose a config.yaml file."))
        self.saveConfig.setText(_translate("configureDialog", "Save"))
