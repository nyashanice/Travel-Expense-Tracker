INSERT INTO trips (destination, description, start_date, end_date)
VALUES ("Aruba","birthday trip",'2023-04-01','2023-04-08'),
       ("Miami, FL","sister's birthday",'2023-08-10','2023-08-14'),
       ("Charlotte, NC","business trip",'2023-11-07','2023-11-10'),
       ("Las Vegas, NV","John Legend concert",'2023-12-12','2023-12-14')


INSERT INTO categories (name, description)
VALUES ("Transportation","flight, train, bus, rideshare/taxi, gas, rental car"),
       ("Accommodation","hotel, AirBnb, hostel, vacation rental"),
       ("Meals","restaurants, cafes, fast food, groceries"),
       ("Entertainment","event tickets, tours, attractions"),
       ("Communication","SIM card, phone plan"),
       ("Business","conference fees, business meals"),
       ("Currency Exchange/ATM Fees","fees related to currency exchange or ATM withdrawl"),
       ("Emergencies","medical expenses, unforseen expenses"),
       ("Miscellaneous","travel insurance, tips/gratuities, souvenirs, laundry")


INSERT INTO expenses (amount, note, date, category_id, trip_id)
VALUES (843, "Delta flight", '2023-04-01',1,1),
       (34.19, "room service", '2023-08-11',3,2)