-- create database and seed data
-- table for destination info (location, season, start and end date)
-- table for expenses data (food and drinks, excursions, transportation, lodging, nightlife, gifts)
-- same trip id for both tables to access info for specific trip? ont to one relationship

DROP DATABASE IF EXISTS expenses_db;
CREATE DATABASE expenses_db;

USE expenses_db;

CREATE TABLE destinations (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    season VARCHAR(6) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);