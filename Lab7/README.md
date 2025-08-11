# Lab 7 – Interactive SQL Query Driver with Containerized MySQL

## Introduction

This project builds upon **Lab 6** by combining a containerized MySQL database with a Python-based interactive command-line driver.  
The driver allows the user to run predefined SQL queries against the live database by selecting them from a menu.  

---

## Description

The project includes:
- A **Docker Compose** file that runs a MySQL 8.0 container and initializes it with:
  - `createguitar.sql` – creates the `my_guitar_shop` schema and populates data
  - `guitar_shop_queries.sql` – contains 13 SQL queries
- A **Python driver (`driver.py`)** that:
  - Connects to the MySQL container
  - Loads the queries from `guitar_shop_queries.sql`
  - Displays them as a numbered menu
  - Executes the selected query and displays the results

This setup simulates a development workflow where a CLI tool can be used to test or explore database queries in real-time.

---

## Design

- **Database Layer**: MySQL 8.0 running in a Docker container.
- **Initialization**: All SQL files are placed in the `init/` folder and automatically executed when the container starts.
- **Driver**:
  - Reads queries from the SQL file
  - Presents them as a numbered menu
  - Runs the selected query against the database
  - Displays results or success messages
- **Port Mapping**: `3306:3306` so MySQL is accessible on the default port.

---

## How to Run

### 1. Install Prerequisites
- [Docker Desktop](https://www.docker.com/)
- Python 3
- MySQL connector for Python:
  ```bash
  pip install mysql-connector-python

## Clone Repository 
git clone https://github.com/your-username/CloudComputing.git
cd CloudComputing/Lab7

## Start MYSQL container
docker-compose up -d
docker ps
python driver.py

## Select Queries to Run
