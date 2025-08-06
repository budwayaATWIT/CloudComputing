# Lab 6 – Containerized MySQL Guitar Shop Database

## Introduction  
A containerized MySQL database implementation with an accompanying SQL script containing 13 queries for a guitar shop database.

---

## 📄 Description  
This lab builds on Lab 5 by containerizing a MySQL database using Docker and Docker Compose. The project includes:
- A Docker Compose configuration that deploys a MySQL 8.0 instance.
- An initialization script (`createguitar.sql`) to set up the schema and sample data.
- A query script (`guitar_shop_queries.sql`) featuring 13 SQL queries.
- Supporting files in the `/Lab6` directory of the Lab 1 repository.

Queries range from basic table selects to complex joins and group-by aggregations that analyze customer, product, and order data.

---

## Design  

- **Docker Compose** uses the official MySQL 8.0 image.
- The `init` folder contains the `createguitar.sql` and the `my_guitar_shop` file, which is executed automatically on container startup to set up the database.
- The queries were written in DBeaver and designed specifically for the MySQL engine.
- Query Breakdown:
  - 13 SQL queries covering selects, joins, group-by, and functions.

---

## How to Run This Project  

1. **Install Docker**  
   Download and install Docker Desktop from [https://www.docker.com](https://www.docker.com) and ensure it's running.

2. **Clone the Repository**  
   git clone https://github.com/your-username/CloudComputing.git
   cd CloudComputing/Lab6
   
   **Starting Container**
   docker-compose up -d
   docker ps
   docker exec -it mysql_guitar_shop mysql -u root -p
    # Enter password: rootpassword
    USE my_guitar_shop;

