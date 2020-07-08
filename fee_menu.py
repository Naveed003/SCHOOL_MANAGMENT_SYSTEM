# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs/fee_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fee_menu(object):
    def setupUi(self, fee_menu):
        fee_menu.setObjectName("fee_menu")
        fee_menu.resize(506, 275)
        fee_menu.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"font-family: Times New Roman\n"
"")
        self.centralwidget = QtWidgets.QWidget(fee_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"")
        self.label.setObjectName("label")
        self.btn_fee_deposit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fee_deposit.setGeometry(QtCore.QRect(18, 129, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_fee_deposit.setFont(font)
        self.btn_fee_deposit.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.btn_fee_deposit.setObjectName("btn_fee_deposit")
        self.btn_fees_details = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fees_details.setGeometry(QtCore.QRect(258, 129, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
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
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(18, 199, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet("QPushButton { \n"
"    background-color: #33ff39;\n"
"    border: 2px;\n"
"    border-radius: 10px;\n"
"                    \n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
"")
        self.btn_return.setObjectName("btn_return")
        fee_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(fee_menu)
        QtCore.QMetaObject.connectSlotsByName(fee_menu)

    def retranslateUi(self, fee_menu):
        _translate = QtCore.QCoreApplication.translate
        fee_menu.setWindowTitle(_translate("fee_menu", "MainWindow"))
        self.label.setText(_translate("fee_menu", "<html><head/><body><p>FEE MENU</p></body></html>"))
        self.btn_fee_deposit.setText(_translate("fee_menu", "FEE DEPOSIT"))
        self.btn_fees_details.setText(_translate("fee_menu", "FEE DETAILS"))
        self.btn_return.setText(_translate("fee_menu", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fee_menu = QtWidgets.QMainWindow()
    ui = Ui_fee_menu()
    ui.setupUi(fee_menu)
    fee_menu.show()
    sys.exit(app.exec_())
