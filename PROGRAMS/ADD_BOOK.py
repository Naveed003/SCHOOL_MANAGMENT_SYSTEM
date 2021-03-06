
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_Book(object):
    def setupUi(self, Add_Book):
        Add_Book.setObjectName("Add_Book")
        Add_Book.resize(252, 330)
        Add_Book.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                               "font-family: Times New Roman;\n"
                               "COLOR: WHITE\n"
                               "\n"
                               "")
        self.centralwidget = QtWidgets.QWidget(Add_Book)
        self.centralwidget.setObjectName("centralwidget")
        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setGeometry(QtCore.QRect(10, 90, 231, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.formFrame.setFont(font)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.bookIdLabel = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.bookIdLabel.setFont(font)
        self.bookIdLabel.setObjectName("bookIdLabel")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.bookIdLabel)
        self.txtbookid = QtWidgets.QLineEdit(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.txtbookid.setFont(font)
        self.txtbookid.setStyleSheet("QLineEdit{\n"
                                     "    border: 1px solid white;\n"
                                     "\n"
                                     "}")
        self.txtbookid.setObjectName("txtbookid")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.txtbookid)
        self.nAMELabel = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.nAMELabel.setFont(font)
        self.nAMELabel.setObjectName("nAMELabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.nAMELabel)
        self.txtbookname = QtWidgets.QLineEdit(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.txtbookname.setFont(font)
        self.txtbookname.setStyleSheet("QLineEdit{\n"
                                       "    border: 1px solid white;\n"
                                       "\n"
                                       "}")
        self.txtbookname.setObjectName("txtbookname")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.txtbookname)
        self.eDITIONLabel = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.eDITIONLabel.setFont(font)
        self.eDITIONLabel.setObjectName("eDITIONLabel")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.eDITIONLabel)
        self.txtedition = QtWidgets.QSpinBox(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.txtedition.setFont(font)
        self.txtedition.setObjectName("txtedition")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.txtedition)
        self.aUTHORLabel = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.aUTHORLabel.setFont(font)
        self.aUTHORLabel.setObjectName("aUTHORLabel")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.aUTHORLabel)
        self.txtauthor = QtWidgets.QLineEdit(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.txtauthor.setFont(font)
        self.txtauthor.setStyleSheet("QLineEdit{\n"
                                     "    border: 1px solid white;\n"
                                     "\n"
                                     "}")
        self.txtauthor.setObjectName("txtauthor")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.txtauthor)
        self.pUBLISHERLabel = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.pUBLISHERLabel.setFont(font)
        self.pUBLISHERLabel.setObjectName("pUBLISHERLabel")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.pUBLISHERLabel)
        self.txtpublisher = QtWidgets.QLineEdit(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.txtpublisher.setFont(font)
        self.txtpublisher.setStyleSheet("QLineEdit{\n"
                                        "    border: 1px solid white;\n"
                                        "\n"
                                        "}")
        self.txtpublisher.setObjectName("txtpublisher")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.txtpublisher)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_add = QtWidgets.QToolButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(30, 270, 61, 21))
        self.btn_add.setStyleSheet("QToolButton { \n"
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
        self.btn_add.setObjectName("btn_add")
        self.btn_return = QtWidgets.QToolButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(160, 270, 61, 21))
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
        Add_Book.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_Book)
        QtCore.QMetaObject.connectSlotsByName(Add_Book)

    def retranslateUi(self, Add_Book):
        _translate = QtCore.QCoreApplication.translate
        Add_Book.setWindowTitle(_translate("Add_Book", "MainWindow"))
        self.bookIdLabel.setText(_translate("Add_Book", "BOOK ID: "))
        self.nAMELabel.setText(_translate("Add_Book", "NAME:"))
        self.eDITIONLabel.setText(_translate("Add_Book", "EDITION:"))
        self.aUTHORLabel.setText(_translate("Add_Book", "AUTHOR:"))
        self.pUBLISHERLabel.setText(_translate("Add_Book", "PUBLISHER:"))
        self.label.setText(_translate("Add_Book", "ADD BOOK"))
        self.btn_add.setText(_translate("Add_Book", "ADD"))
        self.btn_return.setText(_translate("Add_Book", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Book = QtWidgets.QMainWindow()
    ui = Ui_Add_Book()
    ui.setupUi(Add_Book)
    Add_Book.show()
    sys.exit(app.exec_())
