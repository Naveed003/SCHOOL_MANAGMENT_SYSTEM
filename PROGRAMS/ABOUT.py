
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 466)
        MainWindow.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                 "font-family: Times New Roman;\n"
                                 "COLOR: WHITE\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 401, 391))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("font-size: 20;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ABOUT"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE PROJECT TITLED &quot;SCHOOL MANAGMENT SYSTEM&quot; IS A MANAGMENT SOFTWARE FOR MONITORING THE SCHOOL.THIS PROJECT IS IS DESIGNED AND CODED IN IDLE AND DATABASE MANAGEMENT IS HANDLED BY MySQL.THIS SOFTWARE MAINLY FOCUSES ON BASIC OPERATIONS RELATED TO ADMISSION, LIKE ADDING A STUDENT, DELETING A STUDENT, MODIFYING A STUDENT AND OPERATIONS RELATED TO FEES AND LIBRARY MANAGEMENT. &quot;SCHOOL MANAGEMENT SYSTEM&quot; IS A PYTHON APPLICATION WRITTEN ON A macOS. &quot;SCHOOL MANAGEMENT SYSTEM&quot; SUPPORTS TWO OPERATING SYSTEM THAT IS macOS AND WINDOWS. THIS SOFTWARE IS EASY TO USE FOR BOTH BEGINNERS AND ADVANCED USERS. </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
