
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Student_Data(object):
    def setupUi(self, Student_Data):
        Student_Data.setObjectName("Student_Data")
        Student_Data.resize(1236, 568)
        Student_Data.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                   "font-family: Times New Roman\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(Student_Data)
        self.centralwidget.setObjectName("centralwidget")
        self.btnModify = QtWidgets.QToolButton(self.centralwidget)
        self.btnModify.setGeometry(QtCore.QRect(180, 490, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnModify.setFont(font)
        self.btnModify.setStyleSheet("QToolButton { \n"
                                     "    background-color: #33ff39;\n"
                                     "    border: 2px;\n"
                                     "    border-radius: 8px;\n"
                                     "                    \n"
                                     " }\n"
                                     "\n"
                                     "QToolButton:pressed {\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btnModify.setObjectName("btnModify")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 120, 351, 351))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    border: 2px solid white;\n"
                                 "\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                 "    border: 2px white;\n"
                                 "\n"
                                 "}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(140, 140, 181, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.maleradio = QtWidgets.QRadioButton(self.frame_2)
        self.maleradio.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.maleradio.setStyleSheet("color: white;\n"
                                     "BACKGROUND: ")
        self.maleradio.setObjectName("maleradio")
        self.femaleradio = QtWidgets.QRadioButton(self.frame_2)
        self.femaleradio.setGeometry(QtCore.QRect(90, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.femaleradio.setFont(font)
        self.femaleradio.setStyleSheet("color: white;")
        self.femaleradio.setObjectName("femaleradio")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_6.setObjectName("label_6")
        self.age = QtWidgets.QSpinBox(self.frame)
        self.age.setGeometry(QtCore.QRect(140, 240, 181, 22))
        self.age.setMinimum(3)
        self.age.setMaximum(20)
        self.age.setObjectName("age")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_9.setObjectName("label_9")
        self.txtroll = QtWidgets.QLineEdit(self.frame)
        self.txtroll.setGeometry(QtCore.QRect(142, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.txtroll.setFont(font)
        self.txtroll.setStyleSheet("QLineEdit {\n"
                                   "    border: 2px solid gray;\n"
                                   "    border-radius: 10px;\n"
                                   "    padding: 0 8px;\n"
                                   "    background: white;\n"
                                   "    selection-background-color: darkgray;\n"
                                   "}")
        self.txtroll.setObjectName("txtroll")
        self.txtname = QtWidgets.QLineEdit(self.frame)
        self.txtname.setGeometry(QtCore.QRect(140, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.txtname.setFont(font)
        self.txtname.setStyleSheet("QLineEdit {\n"
                                   "    border: 2px solid gray;\n"
                                   "    border-radius: 10px;\n"
                                   "    padding: 0 8px;\n"
                                   "    background: white;\n"
                                   "    selection-background-color: darkgray;\n"
                                   "}")
        self.txtname.setObjectName("txtname")
        self.txtphone = QtWidgets.QLineEdit(self.frame)
        self.txtphone.setGeometry(QtCore.QRect(140, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.txtphone.setFont(font)
        self.txtphone.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid gray;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 0 8px;\n"
                                    "    background: white;\n"
                                    "    selection-background-color: darkgray;\n"
                                    "}")
        self.txtphone.setObjectName("txtphone")
        self.txtdob = QtWidgets.QLineEdit(self.frame)
        self.txtdob.setGeometry(QtCore.QRect(140, 270, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.txtdob.setFont(font)
        self.txtdob.setStyleSheet("QLineEdit {\n"
                                  "    border: 2px solid gray;\n"
                                  "    border-radius: 10px;\n"
                                  "    padding: 0 8px;\n"
                                  "    background: white;\n"
                                  "    selection-background-color: darkgray;\n"
                                  "}")
        self.txtdob.setObjectName("txtdob")
        self.txtemail = QtWidgets.QLineEdit(self.frame)
        self.txtemail.setGeometry(QtCore.QRect(140, 310, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.txtemail.setFont(font)
        self.txtemail.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid gray;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 0 8px;\n"
                                    "    background: white;\n"
                                    "    selection-background-color: darkgray;\n"
                                    "}")
        self.txtemail.setObjectName("txtemail")
        self.division = QtWidgets.QComboBox(self.frame)
        self.division.setGeometry(QtCore.QRect(240, 190, 81, 41))
        self.division.setStyleSheet("border: 1px solid white;\n"
                                    "color: white\n"
                                    "")
        self.division.setObjectName("division")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.grade = QtWidgets.QComboBox(self.frame)
        self.grade.setGeometry(QtCore.QRect(140, 190, 91, 41))
        self.grade.setStyleSheet("border: 1px solid white;\n"
                                 "color: white\n"
                                 "")
        self.grade.setObjectName("grade")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.grade.addItem("")
        self.btnshowall = QtWidgets.QToolButton(self.centralwidget)
        self.btnshowall.setGeometry(QtCore.QRect(320, 490, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnshowall.setFont(font)
        self.btnshowall.setStyleSheet("QToolButton { \n"
                                      "    background-color: #33ff39;\n"
                                      "    border: 2px;\n"
                                      "    border-radius: 8px;\n"
                                      "                    \n"
                                      " }\n"
                                      "\n"
                                      "QToolButton:pressed {\n"
                                      "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btnshowall.setObjectName("btnshowall")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 10, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.studtable = QtWidgets.QTableWidget(self.centralwidget)
        self.studtable.setGeometry(QtCore.QRect(420, 120, 791, 351))
        self.studtable.setStyleSheet("COLOR: WHITE;\n"
                                     "QTabWidget::tab-bar {\n"
                                     "    left: 5px; /* move to the right by 5px */\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.studtable.setObjectName("studtable")
        self.studtable.setColumnCount(8)
        self.studtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.studtable.setHorizontalHeaderItem(7, item)
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(1090, 490, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
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
        self.btnShowStudent = QtWidgets.QToolButton(self.centralwidget)
        self.btnShowStudent.setGeometry(QtCore.QRect(50, 490, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnShowStudent.setFont(font)
        self.btnShowStudent.setStyleSheet("QToolButton { \n"
                                          "    background-color: #33ff39;\n"
                                          "    border: 2px;\n"
                                          "    border-radius: 8px;\n"
                                          "                    \n"
                                          " }\n"
                                          "\n"
                                          "QToolButton:pressed {\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);}")
        self.btnShowStudent.setObjectName("btnShowStudent")
        self.frame.raise_()
        self.label_7.raise_()
        self.btnshowall.raise_()
        self.btnModify.raise_()
        self.studtable.raise_()
        self.btn_return.raise_()
        self.btnShowStudent.raise_()
        Student_Data.setCentralWidget(self.centralwidget)

        self.retranslateUi(Student_Data)
        QtCore.QMetaObject.connectSlotsByName(Student_Data)

    def retranslateUi(self, Student_Data):
        _translate = QtCore.QCoreApplication.translate
        Student_Data.setWindowTitle(_translate("Student_Data", "MainWindow"))
        self.btnModify.setText(_translate("Student_Data", "MODIFY STUDENT"))
        self.label.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">ROLL NO:</span></p></body></html>"))
        self.label_2.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">SEX: </span></p></body></html>"))
        self.label_3.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">PHONE NO:</span></p></body></html>"))
        self.label_4.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">NAME: </span></p></body></html>"))
        self.label_5.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">CLASS :</span></p></body></html>"))
        self.maleradio.setText(_translate("Student_Data", "MALE"))
        self.femaleradio.setText(_translate("Student_Data", "FEMALE"))
        self.label_6.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">AGE :</span></p></body></html>"))
        self.label_8.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">DOB: </span></p></body></html>"))
        self.label_9.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" color:#ffffff;\">EMAIL ID: </span></p></body></html>"))
        self.txtroll.setPlaceholderText(
            _translate("Student_Data", "ROLL NUMBER"))
        self.txtname.setPlaceholderText(_translate("Student_Data", "NAME"))
        self.txtphone.setPlaceholderText(
            _translate("Student_Data", "PHONE NUMBER"))
        self.txtdob.setPlaceholderText(
            _translate("Student_Data", "YYYY-MM-DD"))
        self.txtemail.setPlaceholderText(
            _translate("Student_Data", "EMAIL ID"))
        self.division.setItemText(0, _translate("Student_Data", "A"))
        self.division.setItemText(1, _translate("Student_Data", "B"))
        self.division.setItemText(2, _translate("Student_Data", "C"))
        self.division.setItemText(3, _translate("Student_Data", "D"))
        self.division.setItemText(4, _translate("Student_Data", "E"))
        self.division.setItemText(5, _translate("Student_Data", "F"))
        self.division.setItemText(6, _translate("Student_Data", "G"))
        self.division.setItemText(7, _translate("Student_Data", "H"))
        self.grade.setItemText(0, _translate("Student_Data", "KG-1"))
        self.grade.setItemText(1, _translate("Student_Data", "KG-2"))
        self.grade.setItemText(2, _translate("Student_Data", "1"))
        self.grade.setItemText(3, _translate("Student_Data", "2"))
        self.grade.setItemText(4, _translate("Student_Data", "3"))
        self.grade.setItemText(5, _translate("Student_Data", "4"))
        self.grade.setItemText(6, _translate("Student_Data", "5"))
        self.grade.setItemText(7, _translate("Student_Data", "6"))
        self.grade.setItemText(8, _translate("Student_Data", "7"))
        self.grade.setItemText(9, _translate("Student_Data", "8"))
        self.grade.setItemText(10, _translate("Student_Data", "9"))
        self.grade.setItemText(11, _translate("Student_Data", "10"))
        self.grade.setItemText(12, _translate("Student_Data", "11"))
        self.grade.setItemText(13, _translate("Student_Data", "12"))
        self.btnshowall.setText(_translate("Student_Data", "SHOW ALL "))
        self.label_7.setText(_translate(
            "Student_Data", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">STUDENT DATA</span></p></body></html>"))
        item = self.studtable.horizontalHeaderItem(0)
        item.setText(_translate("Student_Data", "ROLL NO"))
        item = self.studtable.horizontalHeaderItem(1)
        item.setText(_translate("Student_Data", "NAME"))
        item = self.studtable.horizontalHeaderItem(2)
        item.setText(_translate("Student_Data", "PHONE NO"))
        item = self.studtable.horizontalHeaderItem(3)
        item.setText(_translate("Student_Data", "SEX"))
        item = self.studtable.horizontalHeaderItem(4)
        item.setText(_translate("Student_Data", "GRADE"))
        item = self.studtable.horizontalHeaderItem(5)
        item.setText(_translate("Student_Data", "DIVISION"))
        item = self.studtable.horizontalHeaderItem(6)
        item.setText(_translate("Student_Data", "DOB"))
        item = self.studtable.horizontalHeaderItem(7)
        item.setText(_translate("Student_Data", "EMAIL ID"))
        self.btn_return.setText(_translate("Student_Data", "RETURN"))
        self.btnShowStudent.setText(_translate("Student_Data", "SHOW STUDENT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Student_Data = QtWidgets.QMainWindow()
    ui = Ui_Student_Data()
    ui.setupUi(Student_Data)
    Student_Data.show()
    sys.exit(app.exec_())
