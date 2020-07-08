from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Delete_Book(object):
    def setupUi(self, Delete_Book):
        Delete_Book.setObjectName("Delete_Book")
        Delete_Book.resize(252, 205)
        Delete_Book.setStyleSheet("background-color: rgb(8, 8, 8);\n"
                                  "font-family: Times New Roman;\n"
                                  "COLOR: WHITE\n"
                                  "\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(Delete_Book)
        self.centralwidget.setObjectName("centralwidget")
        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setGeometry(QtCore.QRect(10, 90, 231, 41))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_delete = QtWidgets.QToolButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(60, 160, 61, 21))
        self.btn_delete.setStyleSheet("QToolButton { \n"
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
        self.btn_delete.setObjectName("btn_delete")
        self.btn_return = QtWidgets.QToolButton(self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(150, 160, 61, 21))
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
        Delete_Book.setCentralWidget(self.centralwidget)

        self.retranslateUi(Delete_Book)
        QtCore.QMetaObject.connectSlotsByName(Delete_Book)

    def retranslateUi(self, Delete_Book):
        _translate = QtCore.QCoreApplication.translate
        Delete_Book.setWindowTitle(_translate("Delete_Book", "MainWindow"))
        self.bookIdLabel.setText(_translate("Delete_Book", "BOOK ID: "))
        self.label.setText(_translate("Delete_Book", "DELETE BOOK"))
        self.btn_delete.setText(_translate("Delete_Book", "DELETE"))
        self.btn_return.setText(_translate("Delete_Book", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete_Book = QtWidgets.QMainWindow()
    ui = Ui_Delete_Book()
    ui.setupUi(Delete_Book)
    Delete_Book.show()
    sys.exit(app.exec_())
