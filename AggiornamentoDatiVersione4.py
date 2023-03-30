import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "yourpassword",
    database = "mydatabase"
)
mycursor = mydb.cursor()

sql = "Update Alunni SET classe = %s Where classe = %s"
#%s serve per la sicurezza, volendo possiamo anche inserire i nomi 
#direttamente, ma è meno sicuro
val = ("GianMaria", "4a")
#la riga con val serve per la sicurezza e per evitare le SqlInjections

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")