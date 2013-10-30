import psycopg2 as dbapi
import sys
import csv

dbServer='localhost'
dbPass='postgres'
dbSchema='public'
dbUser='postgres'
port = '6543'

#dbQuery='SELECT * FROM mapi_location'
dbQuery='SELECT * FROM auth_user'

db=dbapi.connect(host=dbServer,user=dbUser,password=dbPass, port=port)
cur=db.cursor()
cur.execute(dbQuery)
result=cur.fetchall()

c = csv.writer(open("temp.csv","wb"))

i = 0

# Write data
for row in result:
    if i == 0:
        c.writerow(row.keys)
        i = 1
    else:
        c.writerow(row)




