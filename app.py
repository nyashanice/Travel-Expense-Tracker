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

    # when user selects 'add a trip'
    inquirer.Text(
        "trip_destination",
        message="Where was your trip to?",
    ),
    inquirer.Text(
        "trip_description",
        message="What was the purpose of the trip?"
    ),
    inquirer.Text(
        "trip_start",
        message="What date did your trip start? YYYY/MM/DD"
    ),
    inquirer.Text(
        "trip_end",
        message="What date did your trip end? YYYY/MM/DD"
    ),

    # when user selects 'add an expense'
    inquirer.Text(
        "expense_amnt",
        message="How much was your expense? (numbers only)"
    ),
    inquirer.Text(
        "expense_note",
        message="What was the reason for your purchase?"
    ),
    inquirer.Text(
        "expense_date",
        message="What date did you make your purchase? YYYY/MM/DD"
    ),
    inquirer.List(
        "expense_category",
        message="What category does this expense belong to?",
        # populate categories data here (names only)
        choices=[]
    ),
    inquirer.List(
        "expense_category",
        message="What trip does this expense belong to?",
        # populate trip data here (destinations only)
        choices=[]
    ),
    # update trip
    # update expense
    # add another file to handle queries
    # show expenses from specific trip
    # show expenses in specific category
]

user_answer = inquirer.prompt(questions)
