import socket
import time

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

srv.bind(("127.0.0.1", 9000))
srv.listen(128)
print("Listening on 9000")

while True:
    conn, addr = srv.accept()
    with conn:
        conn.settimeout(5.0)
        while True:
            data = conn.recv(4096)
            print(len(data))
            if not data:
                time.sleep(2)
                break
            conn.sendall(data)