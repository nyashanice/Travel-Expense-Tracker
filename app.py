import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="travel_db"
)

mycursor = db.cursor()

db.commit()
db.close()

print("Connection successful!")