const express = require('express');
const app = express();
const port = 3000;

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'http://localhost'); // Replace with your frontend's URL
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

app.get('/', (req, res) => {
  res.send('Hello from the API Gateway!');
});

app.listen(port, () => {
  console.log(`API Gateway listening at <http://localhost:${port}>`)
});
