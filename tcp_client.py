import socket

with socket.create_connection(("127.0.0.1", 9000), timeout=5) as c:
    # data = b"A" * 100000
    c.sendall(b"Hello network")
    print(c.recv(4096))