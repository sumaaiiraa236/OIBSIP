import socket
import threading
def receive_messages(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(f"Server: {msg}")
        except:
            break
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))
threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    msg = input()
    client.send(msg.encode())
