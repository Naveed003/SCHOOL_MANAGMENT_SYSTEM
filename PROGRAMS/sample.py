
list=[i for i in range(0,9)]
query="insert into students(ROLL_NO,NAME,PHONE_NO,SEX,GRADE,DIVISION,AGE,EMAIL_ID,doj) values({},'{}','{}','{}',{},'{}',{},'{}','{}')".format(i for i in list)
print(query)