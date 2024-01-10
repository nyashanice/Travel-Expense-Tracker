import config.connection as db
from questions import questions
import inquirer
from prettytable import from_db_cursor

# view a table of all trips in database
def viewTrips():
    sql = "SELECT * FROM trips"
    db.cursor.execute(sql)
    print(from_db_cursor(db.cursor))

    # gathers the id and destination of all trips to be used in inquirer list 
    # to choose a single trip to update, remove, or view expenses or to add a new expense
    tripDataQuery = "SELECT destination, id AS value FROM trips"
    db.cursor.execute(tripDataQuery)
    tripData = db.cursor.fetchall()

    #  gathers id and name of all categories to be used to add a new expense
    categoryDataQuery = "SELECT name, id AS value FROM categories"
    db.cursor.execute(categoryDataQuery)
    categoryData = db.cursor.fetchall()
    
    # new prompt to ask user what they would like to do with the information given
    userAnswer = inquirer.prompt(questions['ViewTrips'])
    if userAnswer["all_trips"] == "Remove a trip":
        removeTrip(tripData)
    elif userAnswer["all_trips"] == "Add an expense":
        addExpense(tripData, categoryData)
    elif userAnswer["all_trips"] == "View expenses":
        viewTripExpenses(tripData)
    elif userAnswer['all_trips'] == "Update trip":
        updateTrip(tripData)
    else:
        chooseOption()


# view a table of all categories in database
def viewCategories():
    sql = "SELECT * FROM categories"
    db.cursor.execute(sql)
    print(from_db_cursor(db.cursor))

    # gathers id and name of all categories to be used in inquirer list to 
    # view expenses in a single category
    categoryDataQuery = "SELECT name, id AS value FROM categories"
    db.cursor.execute(categoryDataQuery)
    categoryData = db.cursor.fetchall()
    print(categoryData)
    
    # new prompt to ask user what they would like to do with the information given
    userAnswer = inquirer.prompt(questions['ViewCategories'])
    if userAnswer["all_categories"] == "View expenses":
        viewCategoryExpenses(categoryData)
    else:
        chooseOption()


# add a new trip to database
def addTrip():
    userAnswer = inquirer.prompt(questions['AddTrip'])

    addTripQuery = "INSERT INTO trips (destination, description, start_date, end_date) VALUES (%s,%s,%s,%s)"
    tripValues = [userAnswer['trip_destination'], userAnswer['trip_description'], userAnswer['trip_start'], userAnswer['trip_end']]

    # executes sql query with the values given by the user
    db.cursor.execute(addTripQuery, tripValues)
    db.db.commit()

    print("Added " + userAnswer['trip_destination'] + " trip to the database!")
    chooseOption()


# add a new expense to database
def addExpense(tripData, categoryData):
    userAnswer = inquirer.prompt(questions['AddExpense'](tripData, categoryData))

    # executes sql query with the values given by the user
    sql = "INSERT INTO expenses (trip_id, amount, note, date, category_id) VALUES (%s,%s,%s,%s,%s)"
    expenseValues = [userAnswer['expense_trip'], userAnswer['expense_amnt'], userAnswer['expense_note'], userAnswer['expense_date'],userAnswer['expense_category']]
    db.cursor.execute(sql, expenseValues)
    db.db.commit()

    print("Expense added!")
    chooseOption()


# view expenses from a single trip
def viewTripExpenses(data):
    userAnswer = inquirer.prompt(questions['SingleTrip'](data))

    # shows expenses and the category they belong to in a table format
    sql = "SELECT e.amount, e.note, e.date, c.name AS category FROM expenses e LEFT JOIN categories c ON e.category_id = c.id WHERE e.trip_id=%s"
    tripSelect = [userAnswer['choose_trip']]
    db.cursor.execute(sql, tripSelect)
    print(from_db_cursor(db.cursor))

    chooseOption()


# view expenses from a single category
def viewCategoryExpenses(data):
    userAnswer = inquirer.prompt(questions['SingleCategory'](data))

    # shows expenses and the trip they belong to in a table format
    sql = "SELECT e.id, e.amount, e.note, e.date, t.destination AS trip FROM expenses e LEFT JOIN trips t ON e.trip_id = t.id WHERE e.category_id=%s "
    categorySelect = [userAnswer['choose_category']]
    db.cursor.execute(sql, categorySelect)
    print(from_db_cursor(db.cursor))

    chooseOption()


# removes a trip from the database
def removeTrip(data):
    userAnswer = inquirer.prompt(questions['RemoveTrip'](data))

    sql = "DELETE FROM trips WHERE destination=%s"
    userDelete = userAnswer['remove_trip']

    db.cursor.execute(sql, userDelete)
    db.db.commit()

    print("Trip removed!")
    chooseOption()


# updates the end date for a single trip
def updateTrip(data):
    userAnswer = inquirer.prompt(questions['UpdateTrip'](data))

    # updates the end date of the trip the user selected
    sql = "UPDATE trips SET end_date=%s WHERE id=%s"
    userUpdate = [userAnswer['trip_new_end'], userAnswer['choose_trip']]
    db.cursor.execute(sql, userUpdate)
    db.db.commit()

    print("Trip updated!")
    chooseOption()

# main menu that users see when entering the expense tracker
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

# first function call to begin user session
chooseOption()