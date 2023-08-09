const express = require('express');
const httpProxy = require('http-proxy');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'http://localhost');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

// Create a proxy server
const proxy = httpProxy.createProxyServer();

// Define routes to forward requests to the web service
app.get('/', (req, res) => {
  proxy.web(req, res, { target: 'http://web:5000' });
});

app.post('/new-post', (req, res) => {
  proxy.web(req, res, { target: 'http://web:5000' });
});

app.delete('/', (req, res) => {
  proxy.web(req, res, { target: 'http://web:5000' });
});


// Handle errors from the proxy server
proxy.on('error', (err, req, res) => {
  console.error('Proxy error:', err);
  res.status(500).send('Proxy error');
});

app.listen(port, () => {
  console.log(`API Gateway listening on port ${port}`);
});
