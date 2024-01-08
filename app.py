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
    print("hi")
    chooseOption()

def addTrip():
    print("hello")
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

