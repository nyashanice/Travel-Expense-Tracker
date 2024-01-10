-- show expenses
SELECT * FROM trips


-- show categories
SELECT * FROM categories


-- show expenses
SELECT e.amount, e.note, e.date, c.name AS category FROM expenses e LEFT JOIN categories c ON e.category_id = c.id WHERE e.trip_id=%s
SELECT e.amount, e.note, e.date, t.destination AS trip FROM expenses e LEFT JOIN trips t ON e.trip_id = t.id WHERE e.category_id=%s 


-- add trip
INSERT INTO trips (destination, description, start_date, end_date) VALUES (%s, %s, %s, %s)


-- add expense
INSERT INTO expenses (trip_id, amount, note, date, category_id) VALUES (%s,%s,%s,%s,%s)


-- update trip
UPDATE trips SET end_date=%s WHERE id=%s

