import sqlite3
import json
con= sqlite3.connect("test.db")
print("Successfully opened database")

cursor=con.cursor
try:
    cursor.execute("Creating Table Nagesh"
                  "("
                  + "dictinary BLOB,"
                  + "list BLOB,"
                  + "tuple BLOB,"
                  + "string varchar(50),"
                  + "Integer INTEGER,"
                  + "flo FLOAT,"
                  + "bool BOOLEAN,"
                  + "None BLOB"
                      ");")
except Exception as e:
    print("ERROR :",e)
else:
    print("Table Created successfully")


datafile = open("samplesql.json","r")
dataset = json.load(datafile)
dataframe = []
for row in dataset:
    data = (str(row[0]),str(row[1]),str(row[2]),str(row[3]),int(row[4]),float(row[5]),bool(row[6]),row[7])
    dataframe.append(data)
try:
    cursor.executemany("Insert into Nagesh values (?,?,?,?,?,?,?,?)",dataframe)
except Exception as e:
    print("Error : ",e)
else:
    con.commit()
    print("DATA inserted")
    
try:
    cursor.execute("SELECT * from Nagesh")
except Exception as e:
    print("Error :",e)
else:
    for row in cursor.fetchall():
        print(row)
        
con.close()    
        
    
