# cherrybone

## Usage

Instantiation Start server
```python
from cherrybone import Server

server = Server(app, port=8080)
```

List of parameters:
```python
port: int = 80
path: str = '/'
host: str = '0.0.0.0'
threads: int = multiprocessing.cpu_count()
max_body_bytes: int = 1073741824 # 1 GiB
max_header_bytes: int = 1048576 # 1 MiB
max_threads: int = -1
max_queued_connections: int = 10
connection_timeout: int = 10
max_queued_requests: int = -1
request_acceptance_timeout: int = 10
tcp_nodelay: bool = True
shutdown_timeout: int = 10
```

### Start server
```python
server.start()
```

### Stop server
```python
server.stop()
```
