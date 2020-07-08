
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fees_deposit(object):
    def setupUi(self, Fees_deposit):
        Fees_deposit.setObjectName("Fees_deposit")
        Fees_deposit.resize(667, 602)
        Fees_deposit.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                   "font-family: Times New Roman\n"
                                   "\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(Fees_deposit)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("COLOR: WHITE;")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 110, 291, 101))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    border: 2px solid white;\n"
                                 "\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtcheckroll = QtWidgets.QLineEdit(self.frame)
        self.txtcheckroll.setGeometry(QtCore.QRect(20, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtcheckroll.setFont(font)
        self.txtcheckroll.setStyleSheet("QLineEdit {\n"
                                        "    border: 2px solid gray;\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 0 8px;\n"
                                        "    background: white;\n"
                                        "    selection-background-color: darkgray;\n"
                                        "}")
        self.txtcheckroll.setObjectName("txtcheckroll")
        self.btn_enter = QtWidgets.QToolButton(self.frame)
        self.btn_enter.setGeometry(QtCore.QRect(20, 50, 251, 21))
        self.btn_enter.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_enter.setFont(font)
        self.btn_enter.setStyleSheet("QToolButton { \n"
                                     "    background-color: #33ff39;\n"
                                     "    border: 2px;\n"
                                     "    border-radius: 8px;\n"
                                     "    FONT: 12PX;\n"
                                     "    COLOR: BLACK;\n"
                                     "\n"
                                     "                    \n"
                                     " }\n"
                                     "\n"
                                     "QToolButton:pressed {\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_enter.setObjectName("btn_enter")
        self.txtcheckname = QtWidgets.QLineEdit(self.frame)
        self.txtcheckname.setGeometry(QtCore.QRect(160, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtcheckname.setFont(font)
        self.txtcheckname.setStyleSheet("QLineEdit {\n"
                                        "    border: 2px solid gray;\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 0 8px;\n"
                                        "    background: white;\n"
                                        "    selection-background-color: darkgray;\n"
                                        "}")
        self.txtcheckname.setObjectName("txtcheckname")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 59, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: white;\n"
                                   "color:white")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.txtcheckroll.raise_()
        self.txtcheckname.raise_()
        self.btn_enter.raise_()
        self.tblfees = QtWidgets.QTableWidget(self.centralwidget)
        self.tblfees.setGeometry(QtCore.QRect(30, 250, 611, 161))
        self.tblfees.setStyleSheet("COLOR: WHITE;\n"
                                   "BORDER: 1px solid white;\n"
                                   "font-family: Times New Roman")
        self.tblfees.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tblfees.setLineWidth(1)
        self.tblfees.setMidLineWidth(0)
        self.tblfees.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tblfees.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblfees.setObjectName("tblfees")
        self.tblfees.setColumnCount(6)
        self.tblfees.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblfees.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tblfees.setHorizontalHeaderItem(5, item)
        self.tblfees.horizontalHeader().setVisible(True)
        self.tblfees.horizontalHeader().setCascadingSectionResizes(False)
        self.tblfees.horizontalHeader().setHighlightSections(True)
        self.tblfees.horizontalHeader().setStretchLastSection(False)
        self.tblfees.verticalHeader().setVisible(True)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(60, 430, 181, 151))
        self.frame_2.setStyleSheet("QFrame{\n"
                                   "    border: 2px solid white;\n"
                                   "\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.txtroll = QtWidgets.QLineEdit(self.frame_2)
        self.txtroll.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtroll.setFont(font)
        self.txtroll.setStyleSheet("QLineEdit {\n"
                                   "    border: 2px solid gray;\n"
                                   "    border-radius: 10px;\n"
                                   "    padding: 0 8px;\n"
                                   "    background: white;\n"
                                   "    selection-background-color: darkgray;\n"
                                   "}")
        self.txtroll.setObjectName("txtroll")
        self.btn_pay = QtWidgets.QToolButton(self.frame_2)
        self.btn_pay.setGeometry(QtCore.QRect(30, 100, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_pay.setFont(font)
        self.btn_pay.setStyleSheet("QToolButton { \n"
                                   "    background-color: #33ff39;\n"
                                   "    border: 2px;\n"
                                   "    border-radius: 8px;\n"
                                   "    FONT: 12PX;\n"
                                   "    COLOR: BLACK;\n"
                                   "\n"
                                   "                    \n"
                                   " }\n"
                                   "\n"
                                   "QToolButton:pressed {\n"
                                   "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_pay.setObjectName("btn_pay")
        self.txtfeesdepo = QtWidgets.QLineEdit(self.frame_2)
        self.txtfeesdepo.setGeometry(QtCore.QRect(20, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtfeesdepo.setFont(font)
        self.txtfeesdepo.setStyleSheet("QLineEdit {\n"
                                       "    border: 2px solid gray;\n"
                                       "    border-radius: 10px;\n"
                                       "    padding: 0 8px;\n"
                                       "    background: white;\n"
                                       "    selection-background-color: darkgray;\n"
                                       "}")
        self.txtfeesdepo.setObjectName("txtfeesdepo")
        self.txtroll.raise_()
        self.txtfeesdepo.raise_()
        self.btn_pay.raise_()
        self.btn_return = QtWidgets.QToolButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(450, 480, 161, 32))
        self.btn_return.setStyleSheet("QToolButton { \n"
                                      "    background-color: #33ff39;\n"
                                      "    border: 2px;\n"
                                      "    border-radius: 8px;\n"
                                      "    FONT: 12PX;\n"
                                      "    COLOR: BLACK;\n"
                                      "\n"
                                      "                    \n"
                                      " }\n"
                                      "\n"
                                      "QToolButton:pressed {\n"
                                      "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_return.setObjectName("btn_return")
        self.btn_returnmain = QtWidgets.QToolButton(self.centralwidget)
        self.btn_returnmain.setGeometry(QtCore.QRect(452, 530, 161, 32))
        self.btn_returnmain.setStyleSheet("QToolButton { \n"
                                          "    background-color: #33ff39;\n"
                                          "    border: 2px;\n"
                                          "    border-radius: 8px;\n"
                                          "    FONT: 12PX;\n"
                                          "    COLOR: BLACK;\n"
                                          "\n"
                                          "                    \n"
                                          " }\n"
                                          "\n"
                                          "QToolButton:pressed {\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btn_returnmain.setObjectName("btn_returnmain")
        Fees_deposit.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fees_deposit)
        QtCore.QMetaObject.connectSlotsByName(Fees_deposit)

    def retranslateUi(self, Fees_deposit):
        _translate = QtCore.QCoreApplication.translate
        Fees_deposit.setWindowTitle(_translate("Fees_deposit", "MainWindow"))
        self.label.setText(_translate("Fees_deposit", "FEE DEPOSIT"))
        self.txtcheckroll.setPlaceholderText(
            _translate("Fees_deposit", "ROLL NO"))
        self.btn_enter.setText(_translate("Fees_deposit", "ENTER"))
        self.txtcheckname.setPlaceholderText(
            _translate("Fees_deposit", "NAME"))
        self.label_2.setText(_translate("Fees_deposit", "or"))
        item = self.tblfees.horizontalHeaderItem(0)
        item.setText(_translate("Fees_deposit", "ROLL NO"))
        item = self.tblfees.horizontalHeaderItem(1)
        item.setText(_translate("Fees_deposit", "NAME"))
        item = self.tblfees.horizontalHeaderItem(2)
        item.setText(_translate("Fees_deposit", "GRADE"))
        item = self.tblfees.horizontalHeaderItem(3)
        item.setText(_translate("Fees_deposit", "TOTAL FEES"))
        item = self.tblfees.horizontalHeaderItem(4)
        item.setText(_translate("Fees_deposit", "AMOUNT PAID"))
        item = self.tblfees.horizontalHeaderItem(5)
        item.setText(_translate("Fees_deposit", "AMOUNT PENDING"))
        self.txtroll.setPlaceholderText(_translate("Fees_deposit", "ROLL NO"))
        self.btn_pay.setText(_translate("Fees_deposit", "PAY"))
        self.txtfeesdepo.setPlaceholderText(
            _translate("Fees_deposit", "FEES DEPOSITED"))
        self.btn_return.setText(_translate("Fees_deposit", "RETURN"))
        self.btn_returnmain.setText(_translate(
            "Fees_deposit", "RETURN TO MAIN MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fees_deposit = QtWidgets.QMainWindow()
    ui = Ui_Fees_deposit()
    ui.setupUi(Fees_deposit)
    Fees_deposit.show()
    sys.exit(app.exec_())
