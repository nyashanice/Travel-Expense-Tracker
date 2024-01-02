-- create database and seed data
-- table for destination info (location, season, start and end date)
-- table for expenses data (food and drinks, excursions, transportation, lodging, nightlife, gifts, trip preparation like clothing, hair, nails, etc.)
-- same trip id for both tables to access info for specific trip? ont to one relationship

DROP DATABASE IF EXISTS travel_db;
CREATE DATABASE travel_db;

USE travel_db;

CREATE TABLE trips (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    destination VARCHAR(100) NOT NULL,
    season VARCHAR(6) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE categories (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(1000)
);

CREATE TABLE expenses (
    food_drinks INT NOT NULL,
    excursions INT NOT NULL,
    transportation INT NOT NULL,
    lodging INT NOT NULL,
    nightlife INT NOT NULL,
    gifts INT NOT NULL,
    preparation INT NOT NULL,
    -- references id in trips table
    trip_id INT,
    FOREIGN KEY (trip_id)
    REFERENCES trips(id)
    ON DELETE SET NULL
)