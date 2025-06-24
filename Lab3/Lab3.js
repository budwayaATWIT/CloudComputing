// make use of the http module
/*const http = require('http');
// configure HTTP server to respond with simple message to all requests
const server = http.createServer(function (request, response) {
response.writeHead(200, {"Content-Type": "text/plain"});
response.write("Hello this is our first node.js application");
response.end();
});
// Listen on port 8080 on localhost
const port = 8080;
server.listen(port);
// display a message on the terminal
console.log("Server running at port=" + port)
var express = require("express");
var app = express();
app.use("/static", express.static(path.join(__dirname, "public")));
app.listen(8080, () => { ... })
*/
const express = require("express");
const path = require("path");
const app = express();
const port = 8080; 
app.use(express.json());


app.get('/', (req, res) => {
    res.send('<h1>Welcome to the Home Page</h1>');
});
app.get('/about', (req, res) => {
    res.send('<h1>About Us</h1><p>This is Lab 3 of Cloud Computing</p>');
});
app.get('/contact', (req, res) => {
    res.send('<h1>Contact Us</h1> <p>Email:budwaya@wit.edu</p>');
});
app.get('/greet', (req, res) => {
    const name = req.query.name || 'Guest';
    res.send(`<h1>Hello, ${name}!</h1>`);
});
app.get('/htmlinfo', (req, res) => {
  const info = req.query.info || 'Nothing provided';
  res.send(`<p>You sent: <strong>${info}</strong></p>`);
});
app.get('/lang-greet', (req, res) => {
  const { lang } = req.query;
  const greetings = {
    en: 'Hello!',
    es: '¡Hola!',
    fr: 'Bonjour!',
    de: 'Hallo!'
  };
  res.send(greetings[lang] || 'Language not supported');
});
app.get('/multiply', (req, res) => {
  const x = parseFloat(req.query.x || 0);
  const y = parseFloat(req.query.y || 0);
  res.json({ product: x * y });
});
app.get('/divide', (req, res) => {
  const x = parseFloat(req.query.x || 1);
  const y = parseFloat(req.query.y || 1);
  if (y === 0) {
    return res.status(400).send('Cannot divide by zero');
  }
  res.json({ quotient: x / y });
});
app.get('/age-check', (req, res) => {
  const age = parseInt(req.query.age || '0');
  const category = age < 18 ? 'Minor' : 'Adult';
  res.json({ category });
});
app.get('/secure-data', (req, res) => {
  const apiKey = req.headers['x-api-key'];
  if (apiKey === 'secret123') {
    res.json({ data: 'Congratulations!.' });
  } else {
    res.status(403).json({ error: 'Forbidden: Invalid API Key' });
  }
});
app.post('/submit', (req, res) => {
  const { username, email } = req.body;
  res.json({
    message: `User ${username} with email ${email} submitted successfully!`
  });
});
app.listen(port, () => {
  console.log(`server  running at http://localhost:${port}`);
});


/*http://localhost:8080/age-check?age=22
http://localhost:8080/multiply?x=4&y=3
http://localhost:8080/divide?x=10&y=2
http://localhost:8080/lang-greet?lang=fr
http://localhost:8080/htmlinfo?info=Lab+3+is+fun
http://localhost:8080/greet?name=Aaron
http://localhost:8080/contact
http://localhost:8080/about
http://localhost:8080/
curl -Uri "http://localhost:8080/secure-data" -Headers @{ "x-api-key" = "secret123" }
$body = @{
username = "Budwaya"
email = "budwaya@wit.edu"    
} | ConvertTo-Json
 
(Invoke-WebRequest -Uri "http://localhost:8080/submit" `
-Method POST `
-Body $body `
-ContentType "application/json").Content
*/ 

