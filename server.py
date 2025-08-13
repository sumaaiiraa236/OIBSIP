import socket
import threading
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"Client: {msg}")
        except:
            break
    conn.close()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen(1)
print("[SERVER STARTED] Waiting for a connection...")

conn, addr = server.accept()
print(f"[CONNECTED] Client connected from {addr}")
threading.Thread(target=handle_client, args=(conn, addr)).start()
while True:
    msg = input()
    conn.send(msg.encode())
