const http = require('http');
const httpProxy = require('http-proxy');

const proxy = httpProxy.createProxyServer({target: "http://web:5000", changeOrigin: true});

const server = http.createServer((req, res) => {
  // Set up CORS headers here
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  // Proxy the request to the target server
  proxy.web(req, res);
});

server.listen(3000, () => {
  console.log('Proxy server listening on port 3000');
});