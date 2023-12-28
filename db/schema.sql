-- create database and seed data
-- table for destination info (location, season, start and end date)
-- table for expenses data (food and drinks, excursions, transportation, lodging, nightlife, gifts, trip preparation like clothing, hair, nails, etc.)
-- same trip id for both tables to access info for specific trip? ont to one relationship

DROP DATABASE IF EXISTS travel_db;
CREATE DATABASE travel_db;

USE travel_db;

CREATE TABLE destinations (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    season VARCHAR(6) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE expenses (
    food_drinks INT NOT NULL,
    excursions INT NOT NULL,
    transportation INT NOT NULL,
    lodging INT NOT NULL,
    nightlife INT NOT NULL,
    gifts INT NOT NULL,
    preperation INT NOT NULL,
    -- references id in destinations table
    destination_id INT,
    FOREIGN KEY (destination_id)
    REFERENCES destinations(id)
    ON DELETE SET NULL
)