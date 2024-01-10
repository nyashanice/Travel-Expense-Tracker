import config.connection as db
from questions import questions
import inquirer

# completed
def viewTrips():
    sql = "SELECT * FROM trips"
    db.cursor.execute(sql)
    trips = db.cursor.fetchall()
    # use pandas to format as table?
    for trip in trips:
        print(trip)

    tripDataQuery = "SELECT destination, id AS value FROM trips"
    db.cursor.execute(tripDataQuery)
    tripData = db.cursor.fetchall()

    categoryDataQuery = "SELECT name, id AS value FROM categories"
    db.cursor.execute(categoryDataQuery)
    categoryData = db.cursor.fetchall()
    
    # new prompt to ask user what they would like to do with the information given
    userAnswer = inquirer.prompt(questions['ViewTrips'])
    if userAnswer["all_trips"] == "Remove a trip":
        removeTrip(tripData)
    elif userAnswer["all_trips"] == "Add an expense":
        addExpense(tripData, categoryData)
    else:
        chooseOption()

# completed
def viewCategories():
    sql = "SELECT * FROM categories"
    db.cursor.execute(sql)
    categories = db.cursor.fetchall()
    # use pandas to format as table?
    for category in categories:
        print(category)

    categoryDataQuery = "SELECT name, id AS value FROM categories"
    db.cursor.execute(categoryDataQuery)
    categoryData = db.cursor.fetchall()
    print(categoryData)
    
    # new prompt to ask user what they would like to do with the information given
    userAnswer = inquirer.prompt(questions['ViewCategories'])
    if userAnswer["all_categories"] == "View expenses":
        viewExpenses(categoryData)
    else:
        chooseOption()

# completed
def addTrip():
    userAnswer = inquirer.prompt(questions['AddTrip'])

    addTripQuery = "INSERT INTO trips (destination, description, start_date, end_date) VALUES (%s,%s,%s,%s)"
    tripValues = [userAnswer['trip_destination'], userAnswer['trip_description'], userAnswer['trip_start'], userAnswer['trip_end']]

    db.cursor.execute(addTripQuery, tripValues)
    db.db.commit()
    print("Added " + userAnswer['trip_destination'] + " trip to the database")
    chooseOption()

# completed
def removeTrip(data):
    userAnswer = inquirer.prompt(questions['RemoveTrip'](data))

    sql = "DELETE FROM trips WHERE destination=%s"
    userDelete = userAnswer['remove_trip']

    db.cursor.execute(sql, userDelete)
    db.db.commit()
    print("Trip removed")
    chooseOption()

# completed
def viewExpenses(data):
    userAnswer = inquirer.prompt(questions['SingleCategory'](data)[0])

    sql = "SELECT e.id, e.amount, e.note, e.date, t.destination AS trip FROM expenses e LEFT JOIN trips t ON e.trip_id = t.id WHERE e.category_id=%s "
    categorySelect = [userAnswer['choose_category']]
    db.cursor.execute(sql, categorySelect)
    expenses = db.cursor.fetchall()
    for expense in expenses:
        print(expense)

    chooseOption()

# completed
def addExpense(tripData, categoryData):
    userAnswer = inquirer.prompt(questions['AddExpense'](tripData, categoryData))

    sql = "INSERT INTO expenses (trip_id, amount, note, date, category_id) VALUES (%s,%s,%s,%s,%s)"
    expenseValues = [userAnswer['expense_trip'], userAnswer['expense_amnt'], userAnswer['expense_note'], userAnswer['expense_date'],userAnswer['expense_category']]
    db.cursor.execute(sql, expenseValues)
    db.db.commit()
    print("Expense added!")
    chooseOption()

def chooseOption():
    userAnswer = inquirer.prompt(questions['Main_Q'])
    if userAnswer["main"] == "View all trips":
        viewTrips()
    elif userAnswer["main"] == "View all categories":
        viewCategories()
    elif userAnswer["main"] == "Add a trip":
        addTrip()
    else:
        quit()


chooseOption()