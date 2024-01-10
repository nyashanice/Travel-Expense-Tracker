import inquirer

# completed
def singleCategory(data):
      return [
        inquirer.List(
          "choose_category",
          message="Please choose a category",
          choices=data    
        )
      ]


def singleTrip(data):
      return [
        inquirer.List(
          "choose_trip",
          message="Please choose a trip",
          choices=data    
        )
      ]


def addExpense(tripData, categoryData): 
    return [
    inquirer.List (
        "expense_trip",
        message="Please choose a trip",
        # populate trips here (destinations only)
        choices=tripData
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
        choices=categoryData
    ),
    ]


def removeTrip(data):
      return[
            inquirer.List(
                  "remove_trip",
                  message="Select a trip to remove",
                  # populate trips here (destinations only)
                  choices=data
            )
      ]


def updateTrip(data):
      return[
        inquirer.List(
          "choose_trip",
          message="Please choose a trip",
          # populate trips here (destinations only)
          choices=data    
        ),
        inquirer.Text(
        "trip_new_end",
        message="What is the new end date? YYYY/MM/DD"
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
            choices=["Remove a trip", "Add an expense","View expenses", "Update trip", "Back to main menu"]
        ),
    ],

    'ViewCategories': [
        inquirer.List(
            "all_categories",
            message="What would you like to do?",
            choices=["View expenses", "Back to main menu"]
        ),
    ],

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

    'AddExpense': addExpense,

    'SingleTrip': singleTrip,

    'SingleCategory': singleCategory,

    'RemoveTrip': removeTrip,

    'UpdateTrip': updateTrip
}
