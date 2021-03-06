

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import mysql.connector


class Ui_Admission_Menu(object):
    def ShowMessageBox(self, title, message):
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

    def male(self):
        self.sex = "M"

    def female(self):
        self.sex = "F"

    def vals(self):
        self.roll = self.txtrollno.text()
        self.name = self.txtname.text()
        self.phone = self.txtphone.text()
        self.gra = self.grade.currentText()
        self.divis = self.division.currentText()
        self.age = self.age_val.value()
        self.doj = date.today()
        self.email = self.txtemail.text()
        self.values = [self.roll, self.name, self.phone, self.sex,
                       self.gra, self.divis, self.age, self.email, self.doj]

    def fetchingcolumns(self):
        self.mycursor.execute("show columns from students")
        res = self.mycursor.fetchall()
        self.columns = []
        for i in res:
            self.columns.append(i[0])
    def cleartxt(self):
        self.txtname.clear()
        self.txtphone.setText("+971")
        self.txtemail.clear()
        self.txtrollno.clear()
        self.age_val.clear()

    def show(self):
        self.vals()
        for i in range(len(self.values)):
            if i == 1 and self.values[i] != '':
                self.searchval = [self.values[i]]
                break
            elif i == 7 and self.values[i] != "":

                self.searchval = [self.values[i]]
                break
            elif i == 4:
                if self.values[i] != "" and self.values[i+1] != "":

                    self.searchval = [self.values[i], self.values[i+1]]
                    break

            elif self.values[i] != "" and self.values[i] != "+971" and self.values[7] == "":
                self.searchval = [self.values[i]]

                break

        if i == 1:
            self.mycursor.execute("select name from students")
            tempres = self.mycursor.fetchall()
            templist = []
            tempstuds = []
            for i in tempres:
                for j in i:
                    templist.append(j)

            for i in range(len(templist)):
                if self.searchval[0].lower() in templist[i].lower():
                    tempstuds.append(templist[i])
            if tempstuds != []:
                mainlist = []
                for i in tempstuds:
                    query = "select ROLL_NO,NAME,AGE,SEX,GRADE,DIVISION,EMAIL_ID from students where name='{}'".format(
                        i)
                    self.mycursor.execute(query)
                    res = self.mycursor.fetchall()
                    respone = []
                    strr = ''

                    for i in range(len(res)):
                        response = []
                        for j in range(len(res[i])):
                            if j != 4 and j != 5:
                                response.append(res[i][j])
                            elif j == 4 and j+1 == 5:
                                strr = str(res[i][j])+"-"+str(res[i][j+1])
                                response.append(strr)

                        mainlist.append(response)
                if len(tempstuds) > 1:
                    message = str(len(tempstuds))+" students found "
                    self.ShowMessageBox("FOUND", message)
                elif len(tempstuds) == 1:
                    message = str(len(tempstuds))+" student found"
                    self.ShowMessageBox("FOUND", message)

                self.table_adm.setRowCount(0)
                for i in range(len(tempstuds)):
                    rowPosition = self.table_adm.rowCount()
                    self.table_adm.insertRow(rowPosition)
                    for j in range(len(mainlist[i])):
                        numcols = self.table_adm.columnCount()
                        numrows = self.table_adm.rowCount()
                        self.table_adm.setRowCount(numrows)
                        self.table_adm.setColumnCount(numcols)
                        self.table_adm.setItem(
                            i, j, QtWidgets.QTableWidgetItem(str(mainlist[i][j])))
                return
            else:
                self.ShowMessageBox_(
                    "STUDENT NOT FOUND", "STUDENT WITH THE ENTERED PARAMETERS COULD NOT BE FOUND")
                return

        else:
            self.fetchingcolumns()
            if len(self.searchval) == 1:
                self.column = self.columns[i]
                self.searchval = self.searchval[0]
                query = "select ROLL_NO,NAME,AGE,SEX,GRADE,DIVISION,EMAIL_ID from students where {}='{}'".format(
                    self.column, self.searchval)

            else:
                self.column = self.columns[4]
                self.column1 = self.columns[5]
                query = "select ROLL_NO,NAME,AGE,SEX,GRADE,DIVISION,EMAIL_ID from students where {}='{}' and {}='{}'".format(
                    self.column, self.searchval[0], self.column1, self.searchval[1])
            self.mycursor.execute(query)
            res = self.mycursor.fetchall()
            response = []
            strr = ""
            mainlist = []
            if res != []:

                for i in range(len(res)):
                    for j in range(len(res[i])):
                        if j != 4 and j != 5:
                            response.append(res[i][j])
                        elif j == 4 and j+1 == 5:
                            strr = str(res[i][j])+"-"+str(res[i][j+1])
                            response.append(strr)
                    mainlist.append(response)
                    response = []

                if len(res) > 1:
                    message = str(len(res))+" students found "
                    self.ShowMessageBox("FOUND", message)
                elif len(res) == 1:
                    message = str(len(res))+" student found"
                    self.ShowMessageBox("FOUND", message)

                self.table_adm.setRowCount(0)
                for i in range(len(res)):
                    rowPosition = self.table_adm.rowCount()
                    self.table_adm.insertRow(rowPosition)
                    for j in range(len(mainlist[i])):
                        numcols = self.table_adm.columnCount()
                        numrows = self.table_adm.rowCount()
                        self.table_adm.setRowCount(numrows)
                        self.table_adm.setColumnCount(numcols)
                        self.table_adm.setItem(
                            i, j, QtWidgets.QTableWidgetItem(str(mainlist[i][j])))
                return
            else:
                self.ShowMessageBox_(
                    "STUDENT NOT FOUND", "STUDENT WITH THE ENTERED PARAMETERS COULD NOT BE FOUND")
                return

    def Add(self):
        self.vals()
        if "" in self.values:
            self.ShowMessageBox_("FAILED",'ENTER ALL VALUES')
            return
        elif len(str(self.values[0]))<5:
            self.ShowMessageBox_("FAILED","ENTER A ROLL NUMBER WITH ATLEAST 5 DIGIT ROLL")
            return
        elif len(str(self.values[2][4:]))!=9 or self.values[2][4:].isnumeric()==False:
            self.ShowMessageBox_("FAILED","EMTER A VALID PHONE NUMBER")
            return
        elif "@" not in self.values[7]:
            self.ShowMessageBox_("FAILED",'ENTER A VALID EMAIL ADDRESS')
        
        

        self.mycursor.execute("select ROLL_no from students;")
        res = self.mycursor.fetchall()
        templist = []
        if res != []:
            for i in res:
                for j in i:
                    templist.append(j)
            if self.values[0] in templist:
                self.ShowMessageBox_(
                    "FAILED", "STUDENT WITH THE ENTERED ROLL NUMBER ALDREADY EXISTS")
                return
            query = "insert into students(ROLL_NO,NAME,PHONE_NO,SEX,GRADE,DIVISION,AGE,EMAIL_ID,doj) values({},'{}','{}','{}',{},'{}',{},'{}','{}')".format(self.values[0], self.values[1], self.values[2], self.values[3], self.values[4], self.values[5], self.values[6], self.values[7], self.values[8]
                                                                                                                                                            )
            self.mycursor.execute(query)
            self.mydb.commit()
        else:
            query = "insert into students(ROLL_NO,NAME,PHONE_NO,SEX,GRADE,DIVISION,AGE,EMAIL_ID,doj) values({},'{}','{}','{}',{},'{}',{},'{}','{}')".format(self.values[0], self.values[1], self.values[2], self.values[3], self.values[4], self.values[5], self.values[6], self.values[7], self.values[8]
                                                                                                                                                            )
            self.mycursor.execute(query)
            self.mydb.commit()
        query = "select ROLL_NO,NAME,AGE,SEX,GRADE,DIVISION,EMAIL_ID from students where roll_no='{}'".format(
            self.values[0])
        self.mycursor.execute(query)
        res=self.mycursor.fetchall()
        response=[]
        strr=""
        mainlist=[]
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j != 4 and j != 5:
                    response.append(res[i][j])
                elif j == 4 and j+1 == 5:
                    strr = str(res[i][j])+"-"+str(res[i][j+1])
                    response.append(strr)
            mainlist.append(response)
            response = []
        message="added student with roll number {} and name {} to school databse".format(self.values[0],self.values[1])
        self.ShowMessageBox("SUCCESFULL",message)
        self.table_adm.setRowCount(0)
        for i in range(len(res)):
            rowPosition = self.table_adm.rowCount()
            self.table_adm.insertRow(rowPosition)
            for j in range(len(mainlist[i])):
                numcols = self.table_adm.columnCount()
                numrows = self.table_adm.rowCount()
                self.table_adm.setRowCount(numrows)
                self.table_adm.setColumnCount(numcols)
                self.table_adm.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(mainlist[i][j])))
        
        self.cleartxt()

        
                

    def setupUi(self, Admission_Menu):
        self.sex = ""
        self.mydb = mysql.connector.connect(
            host="localhost", user="root", password="logon@123", database="school_management_system")
        self.mycursor = self.mydb.cursor()
        Admission_Menu.setObjectName("Admission_Menu")
        Admission_Menu.resize(1021, 578)
        Admission_Menu.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                     "font-family: Times New Roman;\n"
                                     "")
        self.centralwidget = QtWidgets.QWidget(Admission_Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.table_adm = QtWidgets.QTableWidget(self.centralwidget)
        self.table_adm.setGeometry(QtCore.QRect(380, 160, 621, 331))
        self.table_adm.setStyleSheet("COLOR: WHITE;\n"
                                     "border: 1px solid white;")
        self.table_adm.setObjectName("table_adm")
        self.table_adm.setColumnCount(6)
        self.table_adm.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_adm.setHorizontalHeaderItem(5, item)
        self.btn_clear = QtWidgets.QToolButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(271, 500, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("QToolButton { \n"
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
        self.btn_clear.setObjectName("btnModify")
        self.btn_clear.clicked.connect(self.cleartxt)
        self.btDelete = QtWidgets.QToolButton(self.centralwidget)
        self.btDelete.setGeometry(QtCore.QRect(190, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btDelete.setFont(font)
        self.btDelete.setStyleSheet("QToolButton { \n"
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
        self.btDelete.setObjectName("btDelete")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 150, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("COLOR: WHITE;\n"
                                   "")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 20, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(28, 160, 341, 331))
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
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.maleradio = QtWidgets.QRadioButton(self.frame_2)
        self.maleradio.setGeometry(QtCore.QRect(10, 10, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.maleradio.setFont(font)
        self.maleradio.setStyleSheet("color: white;\n"
                                     "BACKGROUND: ")
        self.maleradio.setObjectName("maleradio")
        self.maleradio.toggled.connect(self.male)
        self.femaleradio = QtWidgets.QRadioButton(self.frame_2)
        self.femaleradio.setGeometry(QtCore.QRect(90, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.femaleradio.setFont(font)
        self.femaleradio.setStyleSheet("color: white;")
        self.femaleradio.setObjectName("femaleradio")
        self.femaleradio.toggled.connect(self.female)
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
        self.age_val = QtWidgets.QSpinBox(self.frame)
        self.age_val.setGeometry(QtCore.QRect(140, 240, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.age_val.setFont(font)
        self.age_val.setStyleSheet("color: white;")
        self.age_val.setMinimum(3)
        self.age_val.setMaximum(20)
        self.age_val.setObjectName("age_val")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
                                   "    border: 2px white;\n"
                                   "\n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.txtrollno = QtWidgets.QLineEdit(self.frame)
        self.txtrollno.setGeometry(QtCore.QRect(140, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.txtrollno.setFont(font)
        self.txtrollno.setStyleSheet("QLineEdit {\n"
                                     "    border: 2px solid gray;\n"
                                     "    border-radius: 10px;\n"
                                     "    padding: 0 8px;\n"
                                     "    background: white;\n"
                                     "    selection-background-color: darkgray;\n"
                                     "}")
        self.txtrollno.setObjectName("txtrollno")
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
        self.txtemail = QtWidgets.QLineEdit(self.frame)
        self.txtemail.setGeometry(QtCore.QRect(140, 280, 181, 31))
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
        self.division.setItemText(0, "")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.division.addItem("")
        self.grade = QtWidgets.QComboBox(self.frame)
        self.grade.setGeometry(QtCore.QRect(140, 189, 91, 41))
        self.grade.setStyleSheet("border: 1px solid white;\n"
                                 "color: white\n"
                                 "")
        self.grade.setObjectName("grade")
        self.grade.addItem("")
        self.grade.setItemText(0, "")
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
        self.btn_return = QtWidgets.QToolButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(910, 500, 61, 22))
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
        self.btnAdd = QtWidgets.QToolButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(110, 500, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnAdd.setFont(font)
        self.btnAdd.setStyleSheet("QToolButton { \n"
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
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.Add)
        self.btnShowAll = QtWidgets.QToolButton(self.centralwidget)
        self.btnShowAll.setGeometry(QtCore.QRect(820, 500, 71, 22))
        self.btnShowAll.setStyleSheet("QToolButton { \n"
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
        self.btnShowAll.setObjectName("btnShowAll")
        self.btnShow = QtWidgets.QToolButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(30, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnShow.setFont(font)
        self.btnShow.setStyleSheet("QToolButton { \n"
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
        self.btnShow.setObjectName("btnShow")
        self.btnShow.clicked.connect(self.show)
        self.table_adm.raise_()
        self.btn_clear.raise_()
        self.btDelete.raise_()
        self.label_7.raise_()
        self.frame.raise_()
        self.btn_return.raise_()
        self.btnAdd.raise_()
        self.btnShowAll.raise_()
        self.btnShow.raise_()
        self.label_9.raise_()
        Admission_Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Admission_Menu)
        QtCore.QMetaObject.connectSlotsByName(Admission_Menu)

    def retranslateUi(self, Admission_Menu):
        _translate = QtCore.QCoreApplication.translate
        Admission_Menu.setWindowTitle(
            _translate("Admission_Menu", "MainWindow"))
        item = self.table_adm.horizontalHeaderItem(0)
        item.setText(_translate("Admission_Menu", "ROLL NO"))
        item = self.table_adm.horizontalHeaderItem(1)
        item.setText(_translate("Admission_Menu", "NAME"))
        item = self.table_adm.horizontalHeaderItem(2)
        item.setText(_translate("Admission_Menu", "AGE"))
        item = self.table_adm.horizontalHeaderItem(3)
        item.setText(_translate("Admission_Menu", "SEX"))
        item = self.table_adm.horizontalHeaderItem(4)
        item.setText(_translate("Admission_Menu", "CLASS"))
        item = self.table_adm.horizontalHeaderItem(5)
        item.setText(_translate("Admission_Menu", "EMAIL ID"))
        self.btn_clear.setText(_translate("Admission_Menu", "CLEAR"))
        self.btDelete.setText(_translate("Admission_Menu", "DELETE"))
        self.label_9.setText(_translate("Admission_Menu", "STUDENT DETAILS"))
        self.label_7.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">ADMISSION MENU</span></p></body></html>"))
        self.label.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">ROLL NO:</span></p></body></html>"))
        self.label_2.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">SEX: </span></p></body></html>"))
        self.label_3.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">PHONE NO:</span></p></body></html>"))
        self.label_4.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">NAME: </span></p></body></html>"))
        self.label_5.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">CLASS :</span></p></body></html>"))
        self.maleradio.setText(_translate("Admission_Menu", "MALE"))
        self.femaleradio.setText(_translate("Admission_Menu", "FEMALE"))
        self.label_6.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">AGE :</span></p></body></html>"))
        self.label_8.setText(_translate(
            "Admission_Menu", "<html><head/><body><p><span style=\" color:#ffffff;\">EMAIL ID: </span></p></body></html>"))
        self.txtrollno.setPlaceholderText(
            _translate("Admission_Menu", "ROLL NO"))
        self.txtname.setPlaceholderText(_translate("Admission_Menu", "NAME"))
        self.txtphone.setText(_translate("Admission_Menu", "+971"))
        self.txtphone.setPlaceholderText(
            _translate("Admission_Menu", "PHONE NO"))
        self.txtemail.setPlaceholderText(
            _translate("Admission_Menu", "EMAIL ID"))
        self.division.setItemText(1, _translate("Admission_Menu", "A"))
        self.division.setItemText(2, _translate("Admission_Menu", "B"))
        self.division.setItemText(3, _translate("Admission_Menu", "C"))
        self.division.setItemText(4, _translate("Admission_Menu", "D"))
        self.division.setItemText(5, _translate("Admission_Menu", "E"))
        self.division.setItemText(6, _translate("Admission_Menu", "F"))
        self.division.setItemText(7, _translate("Admission_Menu", "G"))
        self.division.setItemText(8, _translate("Admission_Menu", "H"))
        self.grade.setItemText(1, _translate("Admission_Menu", "KG-1"))
        self.grade.setItemText(2, _translate("Admission_Menu", "KG-2"))
        self.grade.setItemText(3, _translate("Admission_Menu", "1"))
        self.grade.setItemText(4, _translate("Admission_Menu", "2"))
        self.grade.setItemText(5, _translate("Admission_Menu", "3"))
        self.grade.setItemText(6, _translate("Admission_Menu", "4"))
        self.grade.setItemText(7, _translate("Admission_Menu", "5"))
        self.grade.setItemText(8, _translate("Admission_Menu", "6"))
        self.grade.setItemText(9, _translate("Admission_Menu", "7"))
        self.grade.setItemText(10, _translate("Admission_Menu", "8"))
        self.grade.setItemText(11, _translate("Admission_Menu", "9"))
        self.grade.setItemText(12, _translate("Admission_Menu", "10"))
        self.grade.setItemText(13, _translate("Admission_Menu", "11"))
        self.grade.setItemText(14, _translate("Admission_Menu", "12"))
        self.btn_return.setText(_translate("Admission_Menu", "RETURN"))
        self.btnAdd.setText(_translate("Admission_Menu", "ADD"))
        self.btnShowAll.setText(_translate("Admission_Menu", "SHOW ALL"))
        self.btnShow.setText(_translate("Admission_Menu", "SHOW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admission_Menu = QtWidgets.QMainWindow()
    ui = Ui_Admission_Menu()
    ui.setupUi(Admission_Menu)
    Admission_Menu.show()
    sys.exit(app.exec_())
