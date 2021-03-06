# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 210)
        MainWindow.setMinimumSize(QtCore.QSize(0, 210))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setObjectName("label_file")
        self.gridLayout.addWidget(self.label_file, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFile.setMinimumSize(QtCore.QSize(400, 28))
        self.lineEditFile.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEditFile.setStyleSheet("padding: 0 5;")
        self.lineEditFile.setObjectName("lineEditFile")
        self.horizontalLayout.addWidget(self.lineEditFile)
        self.selectFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectFileButton.setMinimumSize(QtCore.QSize(120, 0))
        self.selectFileButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.selectFileButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.selectFileButton.setObjectName("selectFileButton")
        self.horizontalLayout.addWidget(self.selectFileButton)
        self.horizontalLayout.setStretch(0, 60)
        self.horizontalLayout.setStretch(1, 30)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setObjectName("label_dir")
        self.gridLayout.addWidget(self.label_dir, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditDir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDir.setMinimumSize(QtCore.QSize(400, 28))
        self.lineEditDir.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEditDir.setStyleSheet("padding: 0 5;")
        self.lineEditDir.setObjectName("lineEditDir")
        self.horizontalLayout_2.addWidget(self.lineEditDir)
        self.selectDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectDirButton.setMinimumSize(QtCore.QSize(120, 0))
        self.selectDirButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.selectDirButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.selectDirButton.setObjectName("selectDirButton")
        self.horizontalLayout_2.addWidget(self.selectDirButton)
        self.horizontalLayout_2.setStretch(0, 60)
        self.horizontalLayout_2.setStretch(1, 30)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(120, 25, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setMinimumSize(QtCore.QSize(160, 0))
        self.startButton.setMaximumSize(QtCore.QSize(160, 16777215))
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 5, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 3, 1, 1)
        self.label_sheet_name = QtWidgets.QLabel(self.centralwidget)
        self.label_sheet_name.setObjectName("label_sheet_name")
        self.gridLayout.addWidget(self.label_sheet_name, 2, 3, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 30)
        self.gridLayout.setColumnMinimumWidth(1, 30)
        self.gridLayout.setColumnMinimumWidth(2, 10)
        self.gridLayout.setColumnMinimumWidth(3, 20)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "?????????????????? Excel ??????????"))
        self.label_file.setText(_translate("MainWindow", "???????? ?????? ????????????????????????????:"))
        self.lineEditFile.setText(_translate("MainWindow", "???? ????????????"))
        self.selectFileButton.setToolTip(_translate("MainWindow", "?????????? ?????????? ?????? ??????????????????"))
        self.selectFileButton.setText(_translate("MainWindow", "???????????????? ????????"))
        self.label_dir.setText(_translate("MainWindow", "?????????? ?????? ???????????????? ????????????????????:"))
        self.selectDirButton.setToolTip(_translate("MainWindow", "?????????? ?????????? ?????? ???????????????? ????????????????????"))
        self.selectDirButton.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.startButton.setText(_translate("MainWindow", "??????????"))
        self.label_sheet_name.setText(_translate("MainWindow", "Sheet name:"))
