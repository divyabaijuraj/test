import cx_Oracle
import openpyxl
import pandas as pd
from openpyxl import workbook


con = cx_Oracle.connect("feb22_divya/feb22_divya@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/orcl")
cursor = con.cursor()
'''
try:
    print(con.version)

    cursor=con.cursor()
    cursor.execute("create table demographic(country_name varchar2(30),country_code varchar2(20),birth_rate integer,internet_users integer,income_group varchar2(30))")
    print("Table Created successfully")
    
    
except cx_Oracle.DatabaseError as e:
    print("Problem in oracle database",e)
'''
###################    read from excel

file_read=pd.read_csv("C:\\Users\\Dell\\Desktop\\P4-Demographic-Data.csv")
data_frame= pd.DataFrame(file_read)
l=data_frame.values
#print(l)

for i in l:
    cursor.execute("INSERT INTO demographic VALUES(:1,:2,:3,:4,:5)",(i[0], i[1],i[2],i[3],i[4]))



'''
for row in data_frame.itertuples():
    cursor.execute("INSERT INTO demographic(country_name,country_code,birth_rate,internet_users,income_group)VALUES (:1,:2,:3,:4,:5)",
                   (row.CountryName,row.CountryCode,row.Birthrate,row.Internetusers,row.IncomeGroup)
                   )
  
#con.commit()
'''
cursor.close()