#!/usr/bin/env python3


import sqlite3


connection = sqlite3.connect("master.db", check_same_thread=False)
cursor = connection.cursor()

# Models the following relationship with SQLite database tables.
# A state has many cities and a state has many parks.
# A table that stores information about each state.
cursor.execute(
	"""CREATE TABLE states(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(100) UNIQUE
	);"""
)

# A table that stores information about each city.
cursor.execute(
	"""CREATE TABLE cities(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(100) UNIQUE,
		state VARCHAR(100),
		FOREIGN KEY(state) REFERENCES states(name)
	);"""
)

# A table that stores information about each park.
cursor.execute(
	"""CREATE TABLE parks(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(100) UNIQUE,
		state VARCHAR(100),
		FOREIGN KEY(state) REFERENCES states(name)
	);"""
)

# Models the following relationship with SQLite database tables.
# A doctor has many patients and a patient has many doctors.
# A table that stores information about each doctor.
cursor.execute(
	"""CREATE TABLE doctors(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(100) UNIQUE,
		age INTEGER,
		sex VARCHAR(10),
		area VARCHAR(100)
	);"""
)

# A table that stores information about each patient.
cursor.execute(
	"""CREATE TABLE patients(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(100) UNIQUE,
		age INTEGER,
		sex VARCHAR(10),
		illness VARCHAR(100)
	);"""
)

# A table that stores information about each doctor-patient relationship.
cursor.execute(
	"""CREATE TABLE relationships(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		doctor_name VARCHAR(100),
		patient_name VARCHAR(100),
		reason VARCHAR(100),
		start_date DATETIME,
		FOREIGN KEY(doctor_name) REFERENCES doctors(name),
		FOREIGN KEY(patient_name) REFERENCES patients(name),
		FOREIGN KEY(reason) REFERENCES patients(illness)
	);"""
)

# Models the following relationship with SQLite database tables.
# Have the following in one database:
# A user has a name, username, password, email, and many phone numbers.
# A admin has a name, username, password, email, and many phone numbers.
cursor.execute(
	"""CREATE TABLE users(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(100),
		username VARCHAR(32) UNIQUE,
		password VARCHAR(32),
		email VARCHAR(128)
	);"""
)

cursor.execute(
	"""CREATE TABLE phone_numbers(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		username VARCHAR(32),
		phone_number VARCHAR(16),
		FOREIGN KEY(username) REFERENCES users(username)
	);"""
)

cursor.close()
connection.close()
