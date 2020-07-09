
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MAIN_MENU(object):
    def setupUi(self, MAIN_MENU):
        MAIN_MENU.setObjectName("MAIN_MENU")
        MAIN_MENU.resize(512, 336)
        MAIN_MENU.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                "font-family: Times New Roman\n"
                                "\n"
                                "")
        self.centralwidget = QtWidgets.QWidget(MAIN_MENU)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_admission = QtWidgets.QPushButton(self.centralwidget)
        self.btn_admission.setGeometry(QtCore.QRect(20, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
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
        self.btn_student_data = QtWidgets.QPushButton(self.centralwidget)
        self.btn_student_data.setGeometry(QtCore.QRect(260, 210, 231, 41))
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
        self.btn_library = QtWidgets.QPushButton(self.centralwidget)
        self.btn_library.setGeometry(QtCore.QRect(20, 210, 231, 41))
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
        self.btn_fees_details = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fees_details.setGeometry(QtCore.QRect(260, 150, 231, 41))
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
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(20, 270, 231, 41))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 270, 231, 41))
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
        MAIN_MENU.setCentralWidget(self.centralwidget)

        self.retranslateUi(MAIN_MENU)
        QtCore.QMetaObject.connectSlotsByName(MAIN_MENU)

    def retranslateUi(self, MAIN_MENU):
        _translate = QtCore.QCoreApplication.translate
        MAIN_MENU.setWindowTitle(_translate("MAIN_MENU", "MainWindow"))
        self.label.setText(_translate(
            "MAIN_MENU", "<html><head/><body><p><span style=\" color:#ffffff;\">MAIN MENU</span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.btn_admission.setText(_translate(
            "MAIN_MENU", "ADMISSION DETAILS"))
        self.btn_student_data.setText(_translate("MAIN_MENU", "STUDENT DATA"))
        self.btn_library.setText(_translate("MAIN_MENU", "LIBRARY"))
        self.btn_fees_details.setText(_translate("MAIN_MENU", "FEES DETAILS"))
        self.btn_exit.setText(_translate("MAIN_MENU", "EXIT"))
        self.pushButton.setText(_translate("MAIN_MENU", "ABOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN_MENU = QtWidgets.QMainWindow()
    ui = Ui_MAIN_MENU()
    ui.setupUi(MAIN_MENU)
    MAIN_MENU.show()
    sys.exit(app.exec_())
