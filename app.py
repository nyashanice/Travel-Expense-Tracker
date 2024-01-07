import config as db
import questions
import inquirer

cursor = db.cursor()

def viewTrips():
    sql = "SELECT * FROM trips"
    cursor.execute(sql)
    chooseOption


async def chooseOption():
    userAnswer = await inquirer.prompt(questions.menu)
    print(userAnswer)
    if userAnswer["main"] == "View all trips":
        viewTrips
    elif userAnswer["main"] == "View all categories":
        ViewCategories
    elif userAnswer["main"] == "Add a trip":
        addTrip
    else:
        quit()