-- db_setup.sql
-- Create database and tables for the Reservation Project
CREATE DATABASE IF NOT EXISTS hotel;
USE hotel;

-- pdata: customer booking data (fields used by PROJECT.py)
CREATE TABLE IF NOT EXISTS pdata (
  id INT AUTO_INCREMENT PRIMARY KEY,
  custname VARCHAR(255) NOT NULL,
  addr TEXT,
  jrdate DATE,
  source VARCHAR(100),
  destination VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- food: id, name, price (PROJECT.py expects row[0], row[1], row[2])
CREATE TABLE IF NOT EXISTS food (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price INT NOT NULL
);

-- luggage: id, weight_limit (kg), charge_per_kg (PROJECT.py expects row[1] = kg, row[2] = per kg)
CREATE TABLE IF NOT EXISTS luggage (
  id INT PRIMARY KEY,
  weight_limit INT NOT NULL,
  charge_per_kg INT NOT NULL
);

-- Sample rows for food and luggage
INSERT INTO food (id, name, price) VALUES
  (1, 'Veg Sandwich', 150),
  (2, 'Chicken Meal', 250),
  (3, 'Pasta', 200)
ON DUPLICATE KEY UPDATE name=VALUES(name), price=VALUES(price);

INSERT INTO luggage (id, weight_limit, charge_per_kg) VALUES
  (1, 5, 100),
  (2, 10, 90),
  (3, 20, 80)
ON DUPLICATE KEY UPDATE weight_limit=VALUES(weight_limit), charge_per_kg=VALUES(charge_per_kg);

-- Optional: create local user (only run if you have admin rights and want these credentials)
-- Uncomment and run if you want the script to also create the user 'Shriya' with password 'lino'
-- CREATE USER 'Shriya'@'localhost' IDENTIFIED BY 'lino';
-- GRANT ALL PRIVILEGES ON hotel.* TO 'Shriya'@'localhost';
-- FLUSH PRIVILEGES;
