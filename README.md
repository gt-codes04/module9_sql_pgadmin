Module 9: Working with Raw SQL in pgAdmin
Objective

This project demonstrates how to:

Set up a Dockerized environment for FastAPI, PostgreSQL, and pgAdmin.

Execute raw SQL commands in pgAdmin to create, insert, query, update, and delete records.

Understand relational database operations and containerized development environments.

Project Structure
module9_sql_pgadmin/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── sql/
│   └── module9_raw_sql.sql
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

Setup Instructions
1. Clone the Repository
git clone https://github.com/gt-codes04/module9_sql_pgadmin.git
cd module9_sql_pgadmin

2. Build and Run Docker Containers
docker compose up --build


Once successful, you will see:

PostgreSQL ready on port 5432

pgAdmin running at http://localhost:5050

FastAPI running at http://localhost:8000

Container Services
Service	Description	Port
module9_fastapi_app	FastAPI web application	8000
module9_postgres_db	PostgreSQL database	5432
module9_pgadmin	pgAdmin web interface	5050
PostgreSQL Database Setup
Connect via pgAdmin

Go to http://localhost:5050

Log in using:

Email: admin@admin.com

Password: root

Create a new server:

Host name/address: db

Username: postgres

Password: postgres

Open Query Tool and execute all SQL commands from:

sql/module9_raw_sql.sql

SQL Commands Executed

Create Tables

users

calculations

Insert Records

Select and Join Queries

Update and Delete Records

Each query result was captured in the Word or PDF report with screenshots and short explanations.

Deliverables
File	Description
sql/module9_raw_sql.sql	Contains all SQL queries
docs/module9_pgadmin_report.pdf	Report with screenshots and query outputs
docker-compose.yml	Multi-container setup for FastAPI, PostgreSQL, and pgAdmin
Dockerfile	Defines the FastAPI app image
requirements.txt	Python dependencies
README.md	Documentation of the entire setup
Verification Steps

Access pgAdmin and verify the created tables under the fastapi_db database.

Execute all SQL commands successfully.

Open http://localhost:8000
 to confirm that FastAPI is running.

Run docker ps to verify that all three containers are active.

Reflection

This project helped reinforce concepts of integrating application backends (FastAPI) with relational databases (PostgreSQL).
Working with Docker Compose made it easier to manage multiple containers and understand service communication through shared networks.
Manually executing SQL commands through pgAdmin provided practical experience in relational data management and query execution.

Author

Guna Teja Abdas
Graduate Student, New Jersey Institute of Technology
Email: ga373@njit.edu

GitHub: gt-codes04