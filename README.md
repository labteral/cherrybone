# cherrybone

## Usage

Instantiation Start server
```python
from cherrybone import Server

server = Server(app, port=8080)
```

List of parameters:
```python
port: int
path: str
host: str
threads: int
max_body_bytes: int
max_header_bytes: int
max_threads: int
max_queued_connections: int
connection_timeout: int
max_queued_requests: int
request_acceptance_timeout: int
tcp_nodelay: bool
shutdown_timeout: int
```

### Start server
```python
server.start()
```

### Stop server
```python
server.stop()
```
