# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs/library_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MAIN_MENU(object):
    def setupUi(self, MAIN_MENU):
        MAIN_MENU.setObjectName("MAIN_MENU")
        MAIN_MENU.resize(513, 421)
        MAIN_MENU.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"font-family: Times New Roman\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MAIN_MENU)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("COLOR: WHITE;\n"
"")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 140, 471, 101))
        self.frame.setStyleSheet("QFrame{\n"
"    border: 2px solid white;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_admission = QtWidgets.QPushButton(self.frame)
        self.btn_admission.setGeometry(QtCore.QRect(10, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_admission.setFont(font)
        self.btn_admission.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.btn_admission.setObjectName("btn_admission")
        self.btn_fees_details = QtWidgets.QPushButton(self.frame)
        self.btn_fees_details.setGeometry(QtCore.QRect(160, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_fees_details.setFont(font)
        self.btn_fees_details.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.btn_fees_details.setObjectName("btn_fees_details")
        self.btn_student_data = QtWidgets.QPushButton(self.frame)
        self.btn_student_data.setGeometry(QtCore.QRect(320, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_student_data.setFont(font)
        self.btn_student_data.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.btn_student_data.setObjectName("btn_student_data")
        self.btn_admission.raise_()
        self.btn_student_data.raise_()
        self.btn_fees_details.raise_()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("COLOR: WHITE")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 270, 471, 101))
        self.frame_2.setStyleSheet("QFrame{\n"
"    border: 2px solid white;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_library = QtWidgets.QPushButton(self.frame_2)
        self.btn_library.setGeometry(QtCore.QRect(10, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_library.setFont(font)
        self.btn_library.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.btn_library.setObjectName("btn_library")
        self.btn_exit = QtWidgets.QPushButton(self.frame_2)
        self.btn_exit.setGeometry(QtCore.QRect(160, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.btn_exit.setObjectName("btn_exit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(322, 31, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.raise_()
        self.btn_exit.raise_()
        self.btn_library.raise_()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("COLOR: WHITE")
        self.label_3.setObjectName("label_3")
        MAIN_MENU.setCentralWidget(self.centralwidget)

        self.retranslateUi(MAIN_MENU)
        QtCore.QMetaObject.connectSlotsByName(MAIN_MENU)

    def retranslateUi(self, MAIN_MENU):
        _translate = QtCore.QCoreApplication.translate
        MAIN_MENU.setWindowTitle(_translate("MAIN_MENU", "MainWindow"))
        self.label.setText(_translate("MAIN_MENU", "<html><head/><body><p>LIBRARY MENU</p><p><br/></p></body></html>"))
        self.btn_admission.setText(_translate("MAIN_MENU", "ADD BOOK"))
        self.btn_fees_details.setText(_translate("MAIN_MENU", "DELETE BOOK"))
        self.btn_student_data.setText(_translate("MAIN_MENU", "STATISTICS"))
        self.label_2.setText(_translate("MAIN_MENU", "OPERATIONS"))
        self.btn_library.setText(_translate("MAIN_MENU", "ISSUE BOOK"))
        self.btn_exit.setText(_translate("MAIN_MENU", "RETURN BOOK"))
        self.pushButton.setText(_translate("MAIN_MENU", "RETURN"))
        self.label_3.setText(_translate("MAIN_MENU", "ACTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN_MENU = QtWidgets.QMainWindow()
    ui = Ui_MAIN_MENU()
    ui.setupUi(MAIN_MENU)
    MAIN_MENU.show()
    sys.exit(app.exec_())
