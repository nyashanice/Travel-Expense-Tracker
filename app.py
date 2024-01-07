import mysql.connector
import inquirer

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="travel_db"
)

cursor = db.cursor()

def addTrip(data):
    return [
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
    ]

def addExpense(data): 
    return [
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
    ]

questions = {
    'Main_Q': [
    inquirer.List(
        "main",
        message="What would you like to do?",
        choices=["View all trips","View all categories","Add a trip"],
    ),
    ],
    'ViewTrips': [
        inquirer.List(
            "all_trips",
            message="What would you like to do?",
            choices=["Select a trip","Remove a trip", "Back to main menu"]
        )
    ],
      'SingleTrip': [
        inquirer.List(
            "single_trip",
            message="What would you like to do?",
            choices=["Update trip","Add an expense","Update an expense", "Back to main menu"]
        )
    ],
      'ViewCategories': [
        inquirer.List(
            "all_categories",
            message="What would you like to do?",
            choices=["Select a category","Back to main menu"]
        )
    ],
        'SingleCategory': [
        inquirer.List(
            "single_category",
            message="What would you like to do?",
            choices=["Back to previous screen","Back to main menu"]
        )
    ],
    # when user selects 'add a trip'
    'AddTrip': addTrip,
    # when user selects 'add an expense'
    'AddExpense': addExpense

    # update trip
    # update expense
    # add another file to handle queries
    # show expenses from specific trip
    # show expenses in specific category
}

user_answer = inquirer.prompt(questions)
