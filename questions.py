import config as db
import inquirer



# def addTrip():
#      [
#     inquirer.Text(
#         "trip_destination",
#         message="Where was your trip to?",
#     ),
#     inquirer.Text(
#         "trip_description",
#         message="What was the purpose of the trip?"
#     ),
#     inquirer.Text(
#         "trip_start",
#         message="What date did your trip start? YYYY/MM/DD"
#     ),
#     inquirer.Text(
#         "trip_end",
#         message="What date did your trip end? YYYY/MM/DD"
#     ),
#     ]

def addExpense(data): 
    return [
    inquirer.List (
         "expense_trip",
         message="Please choose a trip",
         choices=data
    ),
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

def singleTrip(data): 
        return [
        inquirer.List(
             "select_trip",
             message="Please select a trip",
             choices=data
        ),
        inquirer.List(
            "single_trip",
            message="What would you like to do?",
            choices=["Update trip", "Add an expense", "Update an expense", "Back to main menu"]
        ),
    ]

questions = {
    'Main_Q': [
        inquirer.List(
            "main",
            message="What would you like to do?",
            choices=["View all trips", "View all categories", "Add a trip", "Exit"],
        ),
    ],
    'ViewTrips': [
        inquirer.List(
            "all_trips",
            message="What would you like to do?",
            choices=["Remove a trip", "Add an expense", "Back to main menu"]
        ),
    ],
    'ViewCategories': [
        inquirer.List(
            "all_categories",
            message="What would you like to do?",
            choices=["View expenses", "Back to main menu"]
        ),
    ],
    'SingleCategory': [
        inquirer.List(
            "single_category",
            message="What would you like to do?",
            choices=["Back to previous screen", "Back to main menu"]
        ),
    ],
    'SingleTrip': singleTrip,
    # when user selects 'add a trip'
    'AddTrip': [
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
    ],
    # when user selects 'add an expense'
    'AddExpense': addExpense

    # update expense
    # add another file to handle queries
    # show expenses from specific trip
    # show expenses in specific category

}
