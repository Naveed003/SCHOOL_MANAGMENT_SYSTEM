import os
files = [
    "admission_menu",
    "fee_deposit",
    "fee_menu",
    "LOGIN_PAGE",
    "main_menu",
    "new_user_page",
    "student_data",
    "ADD_BOOK",
    "library_menu",
    "fee_details",
    "DELETE_BOOK",
    "statistics",
    "issue_book",
    "return_book",
    "ABOUT"
]
cmd = "pyuic5 -x "

for i in files:
    if i=="admission_menu": 
        i=i.upper()
        temp = cmd +"GUIs/"+ i + ".ui -o  temp/" + i + ".py"
        print(temp)
        os.system(temp)
        temp = ''

#QToolButton(background-color:#33ff39;border:2px;border-radius: 8px;COLOR: BLACK;"
#msgbox.setStyleSheet("background-color: rgb(8,8,8);color:white;font-family:Times New Roman;QLabel{ color: white} QMessageBox QPushButton{background-color: Silver;} ")