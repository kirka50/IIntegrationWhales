# Form implementation generated from reading ui file 'MainWorkWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from pathlib import Path

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 733)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftF = QtWidgets.QFrame(self.centralwidget)
        self.LeftF.setMinimumSize(QtCore.QSize(200, 200))
        self.LeftF.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LeftF.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LeftF.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.LeftF.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.LeftF.setObjectName("LeftF")
        self.gridLayout = QtWidgets.QGridLayout(self.LeftF)
        self.gridLayout.setObjectName("gridLayout")
        self.ArchiveBox = QtWidgets.QGroupBox(self.LeftF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArchiveBox.sizePolicy().hasHeightForWidth())
        self.ArchiveBox.setSizePolicy(sizePolicy)
        self.ArchiveBox.setMinimumSize(QtCore.QSize(0, 0))
        self.ArchiveBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ArchiveBox.setFont(font)
        self.ArchiveBox.setStyleSheet("border:1px solid black;\n"
                                      "border-radius: 5px;")
        self.ArchiveBox.setTitle("")
        self.ArchiveBox.setFlat(False)
        self.ArchiveBox.setCheckable(False)
        self.ArchiveBox.setChecked(False)
        self.ArchiveBox.setObjectName("ArchiveBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ArchiveBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.ArchiveBox)
        self.scrollArea.setStyleSheet("border:None;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 160, 655))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.ArchiveBox, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.LeftF)
        self.CentralF = QtWidgets.QFrame(self.centralwidget)
        self.CentralF.setStyleSheet("border: solid 2px black;\n"
                                    "border-radius: 5px;")
        self.CentralF.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.CentralF.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.CentralF.setObjectName("CentralF")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CentralF)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.CentralF)
        self.frame.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                 "border: 1px solid")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(500, 550))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:None;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.CentralF)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setStyleSheet("border:1px solid black;\n"
                                   "border-radius:5px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.CentralF)
        self.Right = QtWidgets.QFrame(self.centralwidget)
        self.Right.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Right.setStyleSheet("font: 75 13pt \"Arial\";")
        self.Right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Right.setObjectName("Right")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Right)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.Right)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("font: 75 13pt \"Arial\";\n"
                                    "border:1px solid black;\n"
                                    "border-radius: 10px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.BackButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackButton.sizePolicy().hasHeightForWidth())
        self.BackButton.setSizePolicy(sizePolicy)
        self.BackButton.setMinimumSize(QtCore.QSize(180, 20))
        self.BackButton.setObjectName("BackButton")
        self.verticalLayout_3.addWidget(self.BackButton)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(180, 20))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setStyleSheet("border:None;")
        self.label.setText("")
        path = str((Path(__file__).parent / "assets" / "min_logo.jpg"))
        self.label.setPixmap(QtGui.QPixmap(path))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.Right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактор"))
        self.label_3.setText(_translate("MainWindow", "Пожалуйста, выберите картинку в списке слева"))
        self.BackButton.setText(_translate("MainWindow", "Загрузить снова"))
        self.pushButton.setText(_translate("MainWindow", "Исправить айди"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())