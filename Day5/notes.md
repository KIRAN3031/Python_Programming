=============================================================================
----------------------------------DAY5---------------------------------------
=============================================================================

# PostgreSQL
-----------------------------------------------------------------------------

## Introduction to Databases & SQL
    . What is a database, DBMS, RDBMS
    . Difference between SQL & NoSQL
    . SQL categories : DDL, DML, DCL, TCL

## DDL (Data Defination language)
    . CREATE DATABASE, CREATE TABLE
    . DATA TYPES (INT, VARCHAR, DATE, DECIMAL, etc)
    . Constraints
        - PRIMARY KEY
        - FOREIGN KEY
        - NOT NULL
        - UNIQUE
        - CHECK
        - DEFAULT
    . ALTER TALBLE (ADD/MODIFY/DROP COLUMN)
    . DROP TABLE, TRUNCATE


## DML (Data Manipulation Language)
    . INSERT INTO (single row, multiple rows)
    . UPDATE (with WHERE)
    . DELETE vs TRUNCATE


## Basic Queries
    . SELECT basics
    . WHERE conditions (comparison, logical operators, BETWEEN, IN, LIKE)
    . Sorting: ORDER BY (ASC/DESC)
    . Limiting results: LIMIT, TOP (depends on DB)
    . Removing duplicates: DISTINCT

## Aggregate Functions
    . COUNT, SUM, AVG, MIN, MAX
    . GROUP BY
    . HAVING (difference between WHERE and HAVING)

## Joins
    types of Join:
        . INNER JOIN
        . LEFFT JOIN / RIGHT JOIN
        . FULL JOIN
        . CROSS JOIN
    SELF JOIN
    USING MULTIPLE JOINS


## Subqueries
    . Simple subquery in WHERE
    . Subquery in FROM


## Scenario based questions:

    1. Scenario: Design the database for a hospital.
    Tasks:


    Create a table Patients with columns: patient_id, name, email, phone, city.
    patient_id should be primary key.
    email must be unique.
    phone cannot be NULL.


    Create a table Doctors with columns: doctor_id, name, specialization, phone, fees.
    doctor_id primary key.
    fees > 0 (CHECK). 


    Create a table Appointments with columns: appointment_id, patient_id, doctor_id, appointment_date.
    appointment_id → primary key.
    patient_id references Patients(patient_id).
    doctor_id references Doctors(doctor_id).


    Alter table Patients to add column age.



    2. Scenario: Manage hospital data.
        Tasks:

        .Insert 5 patients, 5 doctors.

        .Update the fees of one doctor.

        .Delete one patient (be careful of FK constraints).

        .Increase fees of all cardiologists by 200



    3. Basic Queries (SELECT / WHERE / ORDER BY / DISTINCT / LIMIT)
        Scenario: Fetch hospital info.
        Tasks:
        1. List all patients from Hyderabad.

        2. Show all doctors who charge more than 1000.

        3. List unique cities of patients.

        4. Show top 3 most expensive doctors (highest fees).

        5. Show all patients ordered alphabetically by name.
    

    Aggregate Functions + GROUP BY + HAVING

    4. Scenario: Analyze hospital activities.
    Tasks:
        1. Find total number of patients.

        2. Find total revenue from all appointments (sum of doctor fees).

        3. Find average doctor consultation fee.

        4. Show total appointments handled by each doctor.
                SELECT doctor_id, COUNT(*) AS total_appointments
                FROM Appointments
                GROUP BY doctor_id;


        5. Show doctors who handled more than 3 appointments (HAVING).
                SELECT doctor_id, COUNT(*) AS total_appointments
                FROM Appointments
                GROUP BY doctor_id having Count(*)>1;



    Joins (INNER, LEFT, RIGHT, FULL)

    5. Scenario: Combine data across tables.
        Tasks:
        1. Show all appointments with patient name and doctor name.

        2. List all patients who consulted "Dr. Ramesh".

        3. Find patients who never booked any appointment (LEFT JOIN).

        4. Show doctor names along with total patients consulted.
                    SELECT d.name AS doctor_name, COUNT(DISTINCT a.patient_id) AS total_patients
                    FROM Doctors d
                    LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
                    GROUP BY d.name;


        5. Show all doctors and their patients (FULL JOIN, if supported).
                    SELECT d.name AS doctor_name, p.name AS patient_name
                    FROM Doctors d
                    FULL JOIN Appointments a ON d.doctor_id = a.doctor_id
                    FULL JOIN Patients p ON a.patient_id = p.patient_id
                    ORDER BY d.name NULLS LAST, p.name NULLS LAST;



    Subqueries

    6. Scenario: Advanced lookups.
        Tasks:
        1. Find doctors who charge above the average consultation fee.
                    SELECT * FROM Doctors
                    WHERE fees > (SELECT AVG(fees) FROM Doctors);


        2. Find patients who consulted "Cardiologist".
                    SELECT DISTINCT p.patient_id, p.name
                    FROM Appointments a
                    JOIN Patients p ON a.patient_id = p.patient_id
                    JOIN Doctors d ON a.doctor_id = d.doctor_id
                    WHERE d.specialization = 'Cardiologist';


        3. Get the doctor with the maximum fee (using subquery).
                    SELECT * FROM Doctors
                    WHERE fees = (SELECT MAX(fees) FROM Doctors);


        4. List patients who booked appointments with the top 3 doctors (by appointment count).
                    ```WITH TopDoctors AS (
                    SELECT doctor_id
                    FROM Appointments
                    GROUP BY doctor_id
                    ORDER BY COUNT(*) DESC
                    LIMIT 3
                    )
                    SELECT DISTINCT p.patient_id, p.name
                    FROM Appointments a
                    JOIN Patients p ON a.patient_id = p.patient_id
                    WHERE a.doctor_id IN (SELECT doctor_id FROM TopDoctors);```
               


        5. Show all doctors who never got any appointment.
                ```SELECT d.doctor_id, d.name
                FROM Doctors d
                LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
                WHERE a.appointment_id IS NULL;```







----------------------------------------------------------------------------------------
# Python with database
## Requirements:
## 1) Python Program
## 2) Supabase Client
## 3) Supabase


```create table public.products (
  product_id serial not null,
  name text not null,
  sku text not null,
  price numeric(10, 2) not null,
  stock integer not null default 0,
  created_at timestamp with time zone null default now(),
  constraint products_pkey primary key (product_id),
  constraint products_sku_key unique (sku),
  constraint products_price_check check ((price > (0)::numeric))
) TABLESPACE pg_default;
```


# Project
# Online Library Management System (with Supabase/Postgres + Python):
        Build a command-line application in Python that connects to a Supabase Postgres database and performs all database operations as they happen in real life:
        Register students/members.
        Add/update/remove books.
        Borrow/return books (transaction).
        Generate reports (like overdue, most borrowed books).
        🗄️ Database Schema (create in Supabase → SQL Editor)
        -- Students / Members
        ```CREATE TABLE members (
            member_id serial PRIMARY KEY,
            name text NOT NULL,
            email text UNIQUE NOT NULL,
            join_date timestamptz DEFAULT NOW()
        );
        ```
        
        -- Books
        ```CREATE TABLE books (
            book_id serial PRIMARY KEY,
            title text NOT NULL,
            author text NOT NULL,
            category text,
            stock int NOT NULL DEFAULT 1
        );
        ```
        
        -- Transactions (Borrow/Return)
        ```CREATE TABLE borrow_records (
            record_id serial PRIMARY KEY,
            member_id int REFERENCES members(member_id),
            book_id int REFERENCES books(book_id),
            borrow_date timestamptz DEFAULT NOW(),
            return_date timestamptz
        );
        ```
        
        1. Create (Insert)
        Register new members (add_member(name, email)).
        Add new books (add_book(title, author, category, stock)).
        2. Read (Select)
        List all books with availability.
        Search books by title/author/category.
        Show member details and their borrowed books.
        3. Update
        Update book stock (e.g., when more copies are purchased).
        Update member info (e.g., change email).
        4. Delete
        Delete a member (only if no borrowed books).
        Delete a book (only if not borrowed).
 