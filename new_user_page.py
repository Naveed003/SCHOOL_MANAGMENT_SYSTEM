# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs/new_user_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sign_up(object):
    def setupUi(self, sign_up):
        sign_up.setObjectName("sign_up")
        sign_up.resize(452, 462)
        sign_up.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"font-family: Times New Roman\n"
"")
        self.centralwidget = QtWidgets.QWidget(sign_up)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(110, 380, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_signup.setObjectName("btn_signup")
        self.txtemail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtemail.setGeometry(QtCore.QRect(110, 130, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtemail.setFont(font)
        self.txtemail.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtemail.setCursorPosition(0)
        self.txtemail.setObjectName("txtemail")
        self.txtusername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtusername.setGeometry(QtCore.QRect(110, 190, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtusername.setFont(font)
        self.txtusername.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtusername.setObjectName("txtusername")
        self.txtpass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtpass.setGeometry(QtCore.QRect(112, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtpass.setFont(font)
        self.txtpass.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtpass.setObjectName("txtpass")
        self.txtconfirmpass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtconfirmpass.setGeometry(QtCore.QRect(112, 310, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtconfirmpass.setFont(font)
        self.txtconfirmpass.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txtconfirmpass.setObjectName("txtconfirmpass")
        sign_up.setCentralWidget(self.centralwidget)

        self.retranslateUi(sign_up)
        QtCore.QMetaObject.connectSlotsByName(sign_up)

    def retranslateUi(self, sign_up):
        _translate = QtCore.QCoreApplication.translate
        sign_up.setWindowTitle(_translate("sign_up", "MainWindow"))
        self.label.setText(_translate("sign_up", "<html><head/><body><p><span style=\" color:#ffffff;\">SIGN-UP</span></p></body></html>"))
        self.btn_signup.setText(_translate("sign_up", "SIGN-UP"))
        self.txtemail.setPlaceholderText(_translate("sign_up", "ENTER EMAIL ID"))
        self.txtusername.setPlaceholderText(_translate("sign_up", "ENTER USERNAME"))
        self.txtpass.setPlaceholderText(_translate("sign_up", "ENTER PASSWORD"))
        self.txtconfirmpass.setPlaceholderText(_translate("sign_up", "CONFIRM PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sign_up = QtWidgets.QMainWindow()
    ui = Ui_sign_up()
    ui.setupUi(sign_up)
    sign_up.show()
    sys.exit(app.exec_())
