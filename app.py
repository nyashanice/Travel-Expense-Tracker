import config.connection as db
from questions import questions
import inquirer


def viewTrips():
    sql = "SELECT * FROM trips"
    db.cursor.execute(sql)
    trips = db.cursor.fetchall()
    # use pandas to format as table?
    for trip in trips:
        print(trip)

    tripDataQuery = "SELECT destination FROM trips"
    db.cursor.execute(tripDataQuery)
    tripData = db.cursor.fetchall()
    print(tripData)
    
    # new prompt to ask user what they would like to do with the information given
    userAnswer = inquirer.prompt(questions['ViewTrips'])
    if userAnswer["all_trips"] == "Remove a trip":
        removeTrip(tripData)
    elif userAnswer["all_trips"] == "Add an expense":
        addExpense(tripData)
    else:
        chooseOption()

def viewCategories():
    sql = "SELECT * FROM categories"
    db.cursor.execute(sql)
    categories = db.cursor.fetchall()
    # use pandas to format as table?
    for category in categories:
        print(category)

    categoryDataQuery = "SELECT name FROM categories"
    db.cursor.execute(categoryDataQuery)
    categoryData = db.cursor.fetchall()
    print(categoryData)
    
    # new prompt to ask user what they would like to do with the information given
    userAnswer = inquirer.prompt(questions['ViewCategories'])
    if userAnswer["all_categories"] == "View expenses":
        viewExpenses(categoryData)
    else:
        chooseOption()

def viewExpenses(data):
    print(data)
    userAnswer = inquirer.prompt(questions['SingleCategory'](data))
    print(userAnswer)
    chooseOption()

def addTrip():
    userAnswer = inquirer.prompt(questions['AddTrip'])

    addTripQuery = "INSERT INTO trips (destination, description, start_date, end_date) VALUES (%s,%s,%s,%s)"
    tripValues = [userAnswer['trip_destination'], userAnswer['trip_description'], userAnswer['trip_start'], userAnswer['trip_end']]

    db.cursor.execute(addTripQuery, tripValues)
    db.db.commit()
    print("Added " + userAnswer['trip_destination'] + " trip to the database")
    chooseOption()

def removeTrip(data):
    print("bye")
    chooseOption()

def addExpense(data):
    userAnswer = inquirer.prompt(questions['AddExpense'](data))
    print(userAnswer)
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

