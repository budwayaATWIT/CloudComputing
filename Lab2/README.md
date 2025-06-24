**Introduction**



This lab builds upon Lab 1's FastAPI service by introducing:
A Python command-line driver to invoke all API routes.
A comprehensive unit testing suite using Python’s unittest.
New routes that demonstrate usage of header and cookie parameters.
It serves as a complete testing and automation utility for validating web API functionality in a local environment.

**Project Description:**



This project enhances the previous FastAPI application with:
Command-line interface (CLI) for testing each endpoint.
Automated testing with descriptive outputs.
Support for HTTP headers and cookies via new endpoints.
The main FastAPI application is extended to now fully support real-world API interactions, making this lab more representative of modern web services.

**Project Design:**



FastAPI App – 12+ routes including query, path, header, and cookie params
Command Line Driver – lets you manually run all endpoints
Unittest Suite – tests each route individually with success/failure feedback

**How to run Project:**




Clone the repo: git clone https://github.com/budwayaATWIT/CloudComputing.git cd Lab2
Install dependicies: pip install fastapi uvicorn requests
*Running Server uvicorn Lab1:app --port 8080 --reload
**Running command line driver**
python Lab2.py


**Routes Overview**
| Method | Route                 | Description                                |
| ------ | --------------------- | ------------------------------------------ |
| GET    | `/`                   | Root greeting                              |
| GET    | `/Hello`              | Query string greeting                      |
| GET    | `/hello/{name}/{age}` | Path param greeting                        |
| POST   | `/hello_personclass`  | JSON body via Pydantic                     |
| GET    | `/time`               | Returns current server time                |
| GET    | `/greet`              | Greeting with name and city                |
| GET    | `/Square`             | Returns square of a number                 |
| GET    | `/reverse`            | Reverses a string                          |
| GET    | `/status`             | Online/Offline status via query param      |
| GET    | `/user/{user_id}`     | Retrieves user info from static dictionary |
| GET    | `/header-info`        | Reads `User-Agent` from request header     |
| GET    | `/cookie-info`        | Reads `session_id` from request cookie     |
