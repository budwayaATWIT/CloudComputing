**CloudComputing Lab 1**

**Project Introduction:**



This project is a basic web API service built using FastAPI, a fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
It demonstrates fundamental web API features such as:
Basic routing
Query and path parameters
Data validation with Pydantic
JSON responses
Simple dynamic functionality


**Project Description:**



The application exposes 10+ API routes covering:
Simple text responses,
Query string inputs,
Path variable parameters,
POST requests using Pydantic for data validation,
Utility operations (reverse string, square of a number),
Status checks and time display,
This project is ideal for beginners learning FastAPI and understanding how to structure RESTful endpoints.

**Project Design:**



FastAPI is used to set up the web service.
Each route is mapped to a clear functional purpose.
Pydantic is used for data validation in POST requests.
Routes are grouped by their behavior:
Basic Responses,
Query Parameters,
Path Parameters,
JSON Body Input,
Logic-based Responses (math, string manipulation),
User Lookup Simulation

**How to run Project:**


1. **Clone the repo:** 

 
 git clone https://github.com/budwayaATWIT/CloudComputing.git
 cd Lab1

2. **Install dependicies:**
pip install fastapi uvicorn


3. **Running Server:** uvicorn Lab1:app --port 8080 --reload

**Routes Overview**:
| Method | Route                          | Description                        |
| ------ | ------------------------------ | ---------------------------------- |
| GET    | `/`                            | Root route greeting                |
| GET    | `/Hello?name=Aaron&age=22`     | Query param greeting               |
| GET    | `/hello/Aaron/22`              | Path param greeting                |
| POST   | `/hello_personclass`           | Pydantic-based JSON greeting       |
| GET    | `/time`                        | Returns current timestamp          |
| GET    | `/greet?name=Aaron&city=Boston`| Custom greeting with name and city |
| GET    | `/Square?number=5`             | Returns square of a number         |
| GET    | `/reverse?string=test`         | Reverses the input string          |
| GET    | `/status?is_online=true`       | Returns status: Online or Offline  |
| GET    | `/user/1`                      | Returns user info by ID            |

curl -X POST "http://localhost:8080/hello_personclass" \
-H "Content-Type: application/json" \
-d '{"name": "Aaron", "age": 22}'

