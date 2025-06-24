**Introduction:**


This project is a Node.js service built using the Express framework. It demonstrates the ability to handle various types of HTTP routes including HTML responses, query parameters, headers, and body inputs.

**Project Description:**
The service provides 11 routes:

5+ HTML content routes

5+ routes using query parameters 

1 route using header parameters 

1 route using POST with body data

The application runs on port 8080.

**Project Design:**

HTML Routes: Return static or dynamic HTML using res.send()

Query Params: Parse user inputs from the URL (req.query)

Header Params: Secured route requires a custom header x-api-key

Body Inputs: Accepts JSON data via POST using express.json


**How to Run** 
git clone https://github.com/budwayaATWIT/CloudComputing.git

**Install Dependicies:**
Node.js
npm install express

**Run Server:**

Node Lab3.js
localhost:8080

**Routes Overview**
| Route          | Method | Example / Command                                                                       |
| -------------- | ------ | --------------------------------------------------------------------------------------- |
| `/age-check`   | GET    | `http://localhost:8080/age-check?age=22`                                                |
| `/multiply`    | GET    | `http://localhost:8080/multiply?x=4&y=3`                                                |
| `/divide`      | GET    | `http://localhost:8080/divide?x=10&y=2`                                                 |
| `/lang-greet`  | GET    | `http://localhost:8080/lang-greet?lang=fr`                                              |
| `/htmlinfo`    | GET    | `http://localhost:8080/htmlinfo?info=Lab+3+is+fun`                                      |
| `/greet`       | GET    | `http://localhost:8080/greet?name=Aaron`                                                |
| `/contact`     | GET    | `http://localhost:8080/contact`                                                         |
| `/about`       | GET    | `http://localhost:8080/about`                                                           |
| `/` (home)     | GET    | `http://localhost:8080/`                                                                |
| `/secure-data` | GET    | `curl -Uri "http://localhost:8080/secure-data" -Headers @{ "x-api-key" = "secret123" }` |
| `/submit`      | POST   | $body = @{ username = "Budwaya" email = "budwaya@wit.edu" } | ConvertTo-Json            |
|                            Invoke-WebRequest -Uri "http://localhost:8080/submit" `-Method POST `-Body $body `     |
|                            -ContentType "application/json"                                                        |
