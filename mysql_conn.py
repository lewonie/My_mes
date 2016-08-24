import mysql.connector
 
conn = mysql.connector.connect(
         user='root',
         password='123456',
         host='127.0.0.1',
         database='test')
 
cur = conn.cursor()

query = ("SELECT * FROM mytable")
 
cur.execute(query)
 
for (name, quantity, date, person) in cur:
    print("{}, {}, {}, {}".format(name, quantity, date, person))
 
cur.close()
conn.close()

