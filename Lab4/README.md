**Introduction:**

This project demonstrates how to containerize a FastAPI application using Docker. It includes multiple routes showcasing various FastAPI features, 
including query parameters, path parameters, Pydantic validation, and date/time processing.

**Project Description:** 

A FastAPI web service with multiple endpoints

Packaged using Docker for easy deployment

Allows remote access into the container for interaction and debugging

**Project Design:**

FastAPI Features:


Query parameters (/Hello, /greet, /reverse, etc.)

Path parameters (/hello/{name}/{age}, /user/{user_id})

Pydantic input validation (/hello_personclass)

Date/time handling (/time)

Boolean logic and basic computation (/status, /Square)

Docker Features:

Uses a Dockerfile to containerize the FastAPI app

Runs with uvicorn as the ASGI server

Exposes port 8080

**How to Run**
Install Docker
git clone https://github.com/budwayaATWIT/CloudComputing.git

**Build Docker Image:**

docker build -t lab4 .

**Run Docker Container:** 

docker run -d -p 8080:8080 --name lab4-container lab4

**Remote into Docker Container**
docker exec -it lab4-container /bin/sh


