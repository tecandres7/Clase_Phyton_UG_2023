DDL_QUERY =  

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS travel_DB DEFAULT CHARACTER SET utf8 ;
USE travel_DB ;


-- -----------------------------------------------------
-- Table travel_DB.users
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS travel_DB.users (
  user_id INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  gender VARCHAR(15) NOT NULL,
  age INT NOT NULL,
  company VARCHAR(15) NOT NULL,
  PRIMARY KEY (user_id))

-- -----------------------------------------------------
-- Table Table travel_DB.flights
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS travel_DB.flights (
  flight_id INT NOT NULL AUTO_INCREMENT,
  departure VARCHAR(30) NOT NULL,
  arrival VARCHAR(30) NOT NULL,
  flightType VARCHAR(15) NOT NULL,
  agency VARCHAR(20) NOT NULL,
  date DATETIME NOT NULL,
  flight_date INT NOT NULL,
  flight_price FLOAT NOT NULL,
  flight_time DECIMAL(3,2) NOT NULL,
  flight_distance FLOAT NOT NULL
  PRIMARY KEY (flight_id)

-- -----------------------------------------------------
-- Table travel_DB.hotels
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS travel_DB.hotels (
  id_hotel INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  place VARCHAR(45) NOT NULL,
  hotel_date DATETIME NOT NULL,
  hotel_days INT NOT NULL,
  hotel_price FLOAT NOT NULL,
  hotel_price_total FLOAT NOT NULL,
  
  PRIMARY KEY (id_hotel)
  
   CONSTRAINT fk_travel_id
      FOREIGN KEY (travel_id)
            REFERENCES travels(travel_id)
);

