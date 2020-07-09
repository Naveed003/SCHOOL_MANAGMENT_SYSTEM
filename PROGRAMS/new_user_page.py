from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_Signup_Page(object):
    def ShowMessageBox(self, title, message):
        self.mydb.close()
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.exec_()

    def ShowMessageBox_(self, title, message):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.exec_()
    
    def cleartxt(self):
        self.txtemail.clear()
        self.txtusername.clear()
        self.txtpass.clear()
        self.txtconfirmpass
    
    def new_user(self):
        self.email=self.txtemail.text().lower()
        self.username=str(self.txtusername.text().lower())
        self.password=self.txtpass.text()
        self.confpass=self.txtconfirmpass.text()
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="logon@123",database="school_management_system")
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute("select * from users")
        res=self.mycursor.fetchall()
        emailids=[]
        usernames=[]
        passwords=[]
        for i in res:
            emailids.append(i[0].lower())
            usernames.append(i[1])
            passwords.append(i[2])
        if self.username=="" or self.email =="" or self.password=="" or self.confpass=="" :
            self.ShowMessageBox_("FAILED","ENTER ALL FIELDS")
        else:
            if self.username not in usernames and self.email not in emailids and self.password==self.confpass and "@" in self.email and self.username!=self.email and len(self.username)<=10 and self.username.isnumeric()==False and len(str(self.password))<=20 and len(str(self.password))>=8: 
                ins_query="insert into users values('{}','{}','{}')".format(self.email,self.username,self.password)
                self.mycursor.execute(ins_query)
                self.mydb.commit()
                self.ShowMessageBox("SUCCESSFULL","ACCOUNT CREATED")
            else:
                if self.email in emailids:
                    message="ANOTHER ACCOUNT IS USING {}".format(self.email)
                    self.ShowMessageBox_("FAILED",message)
                    self.txtemail.clear()
                elif self.username in usernames:
                    message="ANOTHER ACCOUNT IS USING {}".format(self.username)
                    self.ShowMessageBox_("FAILED",message)
                elif "@" not in self.email:
                    self.ShowMessageBox_("FAILED","ENTER A VALID EMAIL ADDRESS")
                    self.txtemail.clear()
                elif self.username==self.email:
                    self.ShowMessageBox_("FAILED","USERNAME SHOULD NOT BE SAME AS EMAIL ID")
                    self.txtusername.clear()
                elif len(self.username)>10 or len(str(self.username))>4:
                    self.ShowMessageBox_("FAILED","USERNAME TOO LONG OR TOO SHORT MAXIMUM 10 CHARACTERS AND MINIMUM 4 CHARACHTERS")
                    self.txtusername.clear()
                elif self.username.isnumeric()==True:
                    self.ShowMessageBox_("FAILED","USERNAME SHOULD CONTAIN ATLEAST 1 ALPHABET")
                    self.txtusername.clear()
                elif self.password!=self.confpass:
                    self.ShowMessageBox_("FAILED","PASSWORDS DONT'T MATCH")
                    self.txtpass.clear()
                    self.txtconfirmpass.clear()
                elif len(str(self.password))>20:
                    self.ShowMessageBox_("FAILED","PASSWORD TOO LONG. MAXIMUM 20 CHARACTER")
                    self.txtpass.clear()
                    self.txtconfirmpass.clear()
                elif len(str(self.password))<8:
                    self.ShowMessageBox_("FAILED","PASSWORD TOO SHORT. MINIMUM 8 CHARACTERS") 
                    self.txtpass.clear()
                    self.txtconfirmpass.clear()

    def setupUi(self, Signup_Page):
        Signup_Page.setObjectName("Signup_Page")
        Signup_Page.resize(452, 462)
        Signup_Page.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                  "font-family: Times New Roman\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(Signup_Page)
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
        self.btn_signup.clicked.connect(self.new_user)
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
        self.txtpass.setEchoMode(QtWidgets.QLineEdit.Password)
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
        self.txtconfirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtconfirmpass.setObjectName("txtconfirmpass")
        Signup_Page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Signup_Page)
        QtCore.QMetaObject.connectSlotsByName(Signup_Page)

    def retranslateUi(self, Signup_Page):
        _translate = QtCore.QCoreApplication.translate
        Signup_Page.setWindowTitle(_translate("Signup_Page", "MainWindow"))
        self.label.setText(_translate(
            "Signup_Page", "<html><head/><body><p><span style=\" color:#ffffff;\">SIGN-UP</span></p></body></html>"))
        self.btn_signup.setText(_translate("Signup_Page", "SIGN-UP"))
        self.txtemail.setPlaceholderText(
            _translate("Signup_Page", "ENTER EMAIL ID"))
        self.txtusername.setPlaceholderText(
            _translate("Signup_Page", "ENTER USERNAME"))
        self.txtpass.setPlaceholderText(
            _translate("Signup_Page", "ENTER PASSWORD"))
        self.txtconfirmpass.setPlaceholderText(
            _translate("Signup_Page", "CONFIRM PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup_Page = QtWidgets.QMainWindow()
    ui = Ui_Signup_Page()
    ui.setupUi(Signup_Page)
    Signup_Page.show()
    sys.exit(app.exec_())
