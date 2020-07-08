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
    "DELETE_BOOK"
]
cmd = "pyuic5 -x "

for i in files:
    temp = cmd +"GUIs/"+ i + ".ui -o  PROGRAMS/" + i + ".py"
    print(temp)
    os.system(temp)
    temp = ''
