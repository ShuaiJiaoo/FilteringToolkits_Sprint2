# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'centralWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_centralWidget(object):
    def setupUi(self, centralWidget):
        centralWidget.setObjectName("centralWidget")
        centralWidget.resize(880, 410)
        self.horizontalLayout = QtWidgets.QHBoxLayout(centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(centralWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelImage = QtWidgets.QLabel(self.frame_2)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.horizontalLayout_2.addWidget(self.labelImage)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(280, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setMinimumSize(QtCore.QSize(0, 100))
        self.frame1.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.gridLayout = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditAcc = QtWidgets.QLineEdit(self.frame1)
        self.lineEditAcc.setObjectName("lineEditAcc")
        self.gridLayout.addWidget(self.lineEditAcc, 2, 2, 1, 1)
        self.spinBoxStorage = QtWidgets.QSpinBox(self.frame1)
        self.spinBoxStorage.setObjectName("spinBoxStorage")
        self.gridLayout.addWidget(self.spinBoxStorage, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditTime = QtWidgets.QLineEdit(self.frame1)
        self.lineEditTime.setObjectName("lineEditTime")
        self.gridLayout.addWidget(self.lineEditTime, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.pushButtonSubmit = QtWidgets.QPushButton(self.frame1)
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        self.gridLayout.addWidget(self.pushButtonSubmit, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame1)
        self.frame_21 = QtWidgets.QFrame(self.frame)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame_21)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_21)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_2.addWidget(self.spinBox_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_21)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonOpen = QtWidgets.QPushButton(self.frame_21)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalLayout_6.addWidget(self.pushButtonOpen)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButtonRun = QtWidgets.QPushButton(self.frame_21)
        self.pushButtonRun.setObjectName("pushButtonRun")
        self.horizontalLayout_6.addWidget(self.pushButtonRun)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.frame_21)
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(centralWidget)
        QtCore.QMetaObject.connectSlotsByName(centralWidget)

    def retranslateUi(self, centralWidget):
        _translate = QtCore.QCoreApplication.translate
        centralWidget.setWindowTitle(_translate("centralWidget", "MainWindow"))
        self.label.setText(_translate("centralWidget", "TimeWeight"))
        self.label_2.setText(_translate("centralWidget", "PerformanceWeight"))
        self.label_5.setText(_translate("centralWidget", "VariationWeight"))
        self.pushButtonSubmit.setText(_translate("centralWidget", "Submit"))
        self.label_3.setText(_translate("centralWidget", "please select the process discovery algorrithm"))
        self.pushButton.setText(_translate("centralWidget", "Export Log"))
        self.pushButton_2.setText(_translate("centralWidget", "Export Petri Tree"))
        self.pushButtonOpen.setText(_translate("centralWidget", "Open"))
        self.pushButtonRun.setText(_translate("centralWidget", "Run"))
