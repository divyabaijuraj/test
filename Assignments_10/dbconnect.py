import cx_Oracle
import pandas as pd

con = cx_Oracle.connect("feb22_divya/feb22_divya@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/orcl")
print(con.version)

cursor=con.cursor()
#cursor.execute("create table cust (cust_id integer primary key,cust_name varchar2(30))")
#cursor.execute("insert into cust values(11,'Ammu')")
#cursor.execute("insert into cust values(12,'testcust')")
#cursor.execute('commit')
cursor.execute("select * from cust")
record_found=False
for row in cursor:
    print(row)
    record_found=True
if not record_found:
  print("No record found")
cursor.close
