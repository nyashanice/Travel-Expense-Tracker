import config.connection as db
from questions import questions
import inquirer


def viewTrips():
    sql = "SELECT * FROM trips"
    db.cursor.execute(sql)
    trips = db.cursor.fetchall()
    print(trips)
    chooseOption()

def viewCategories():
    print("hi")
    chooseOption()

def addTrip():
    print("hello")
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

