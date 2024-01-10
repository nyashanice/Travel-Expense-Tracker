DROP DATABASE IF EXISTS travel_db;
CREATE DATABASE travel_db;

USE travel_db;

CREATE TABLE trips (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    destination VARCHAR(100) NOT NULL,
    description VARCHAR(1000),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE categories (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE expenses (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(6,2) NOT NULL,
    note TEXT,
    date DATE NOT NULL,
    -- references id in categories table
    category_id INT,
    FOREIGN KEY (category_id)
    REFERENCES categories(id)
    ON DELETE SET NULL,
    trip_id INT,
    FOREIGN KEY (trip_id)
    REFERENCES trips(id)
    ON DELETE SET NULL
)