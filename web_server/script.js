const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Web Server\n');
});

const port = 3500;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
