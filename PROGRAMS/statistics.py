
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 426)
        MainWindow.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                 "font-family: Times New Roman\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("COLOR: WHITE;")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 130, 511, 221))
        self.frame.setStyleSheet("BORDER: 2PX SOLID WHITE")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tblstatistics = QtWidgets.QTableWidget(self.frame)
        self.tblstatistics.setGeometry(QtCore.QRect(5, 20, 501, 191))
        self.tblstatistics.setStyleSheet("COLOR: WHITE;\n"
                                         "border: 1px solid white;")
        self.tblstatistics.setObjectName("tblstatistics")
        self.tblstatistics.setColumnCount(5)
        self.tblstatistics.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblstatistics.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblstatistics.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblstatistics.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblstatistics.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblstatistics.setHorizontalHeaderItem(4, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("COLOR: WHITE;")
        self.label_2.setObjectName("label_2")
        self.btn_return = QtWidgets.QToolButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(460, 370, 61, 21))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "STATISTICS"))
        item = self.tblstatistics.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BOOK-ID"))
        item = self.tblstatistics.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BOOK-NAME"))
        item = self.tblstatistics.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ROLL NO"))
        item = self.tblstatistics.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tblstatistics.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CLASS"))
        self.label_2.setText(_translate("MainWindow", " ISSUED BOOK "))
        self.btn_return.setText(_translate("MainWindow", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
