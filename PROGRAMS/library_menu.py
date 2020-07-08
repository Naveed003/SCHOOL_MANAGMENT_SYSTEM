
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Library_Menu(object):
    def setupUi(self, Library_Menu):
        Library_Menu.setObjectName("Library_Menu")
        Library_Menu.resize(513, 421)
        Library_Menu.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                   "font-family: Times New Roman\n"
                                   "\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(Library_Menu)
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
        self.btn_add_book = QtWidgets.QPushButton(self.frame)
        self.btn_add_book.setGeometry(QtCore.QRect(10, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_add_book.setFont(font)
        self.btn_add_book.setStyleSheet("QPushButton { \n"
                                        "    background-color: #33ff39;\n"
                                        "    border: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "                    \n"
                                        " }\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                        "")
        self.btn_add_book.setObjectName("btn_add_book")
        self.btn_delete_book = QtWidgets.QPushButton(self.frame)
        self.btn_delete_book.setGeometry(QtCore.QRect(160, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_delete_book.setFont(font)
        self.btn_delete_book.setStyleSheet("QPushButton { \n"
                                           "    background-color: #33ff39;\n"
                                           "    border: 2px;\n"
                                           "    border-radius: 10px;\n"
                                           "                    \n"
                                           " }\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                           "")
        self.btn_delete_book.setObjectName("btn_delete_book")
        self.btn_statistics = QtWidgets.QPushButton(self.frame)
        self.btn_statistics.setGeometry(QtCore.QRect(320, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_statistics.setFont(font)
        self.btn_statistics.setStyleSheet("QPushButton { \n"
                                          "    background-color: #33ff39;\n"
                                          "    border: 2px;\n"
                                          "    border-radius: 10px;\n"
                                          "                    \n"
                                          " }\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                          "")
        self.btn_statistics.setObjectName("btn_statistics")
        self.btn_add_book.raise_()
        self.btn_statistics.raise_()
        self.btn_delete_book.raise_()
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
        self.btn_issue_book = QtWidgets.QPushButton(self.frame_2)
        self.btn_issue_book.setGeometry(QtCore.QRect(10, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_issue_book.setFont(font)
        self.btn_issue_book.setStyleSheet("QPushButton { \n"
                                          "    background-color: #33ff39;\n"
                                          "    border: 2px;\n"
                                          "    border-radius: 10px;\n"
                                          "                    \n"
                                          " }\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                          "")
        self.btn_issue_book.setObjectName("btn_issue_book")
        self.btn_return_book = QtWidgets.QPushButton(self.frame_2)
        self.btn_return_book.setGeometry(QtCore.QRect(160, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_return_book.setFont(font)
        self.btn_return_book.setStyleSheet("QPushButton { \n"
                                           "    background-color: #33ff39;\n"
                                           "    border: 2px;\n"
                                           "    border-radius: 10px;\n"
                                           "                    \n"
                                           " }\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}\n"
                                           "")
        self.btn_return_book.setObjectName("btn_return_book")
        self.btn_return = QtWidgets.QPushButton(self.frame_2)
        self.btn_return.setGeometry(QtCore.QRect(322, 31, 121, 41))
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
        self.btn_return.raise_()
        self.btn_return_book.raise_()
        self.btn_issue_book.raise_()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("COLOR: WHITE")
        self.label_3.setObjectName("label_3")
        Library_Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Library_Menu)
        QtCore.QMetaObject.connectSlotsByName(Library_Menu)

    def retranslateUi(self, Library_Menu):
        _translate = QtCore.QCoreApplication.translate
        Library_Menu.setWindowTitle(_translate("Library_Menu", "MainWindow"))
        self.label.setText(_translate(
            "Library_Menu", "<html><head/><body><p>LIBRARY MENU</p><p><br/></p></body></html>"))
        self.btn_add_book.setText(_translate("Library_Menu", "ADD BOOK"))
        self.btn_delete_book.setText(_translate("Library_Menu", "DELETE BOOK"))
        self.btn_statistics.setText(_translate("Library_Menu", "STATISTICS"))
        self.label_2.setText(_translate("Library_Menu", "OPERATIONS"))
        self.btn_issue_book.setText(_translate("Library_Menu", "ISSUE BOOK"))
        self.btn_return_book.setText(_translate("Library_Menu", "RETURN BOOK"))
        self.btn_return.setText(_translate("Library_Menu", "RETURN"))
        self.label_3.setText(_translate("Library_Menu", "ACTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Library_Menu = QtWidgets.QMainWindow()
    ui = Ui_Library_Menu()
    ui.setupUi(Library_Menu)
    Library_Menu.show()
    sys.exit(app.exec_())
