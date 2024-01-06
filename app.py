import mysql.connector
import inquirer

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="travel_db"
)

cursor = db.cursor()

questions = [
    inquirer.List(
        "main",
        message="What would you like to do?",
        choices=["View all trips","View all categories","View all expenses","Add a trip","Add an expense","Update a trip","Update an expense"],
    ),
]

user_answer = inquirer.prompt(questions)
