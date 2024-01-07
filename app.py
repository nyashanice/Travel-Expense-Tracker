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
    
    userAnswer = inquirer.prompt(questions['ViewTrips'])
    if userAnswer["all_trips"] == "Select a trip":
        selectOneTrip()
    elif userAnswer["all_trips"] == "Remove a trip":
        removeTrip()
    else:
        chooseOption()

def viewCategories():
    print("hi")
    chooseOption()

def addTrip():
    print("hello")
    chooseOption()

def selectOneTrip():
    print('yooo')
    chooseOption()

def removeTrip():
    print("bye")
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

