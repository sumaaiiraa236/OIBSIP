import socket
import threading

def receive_messages(client):
    """Listen for incoming messages from the server"""
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(f"Server: {msg}")
        except:
            break

print("[CLIENT] Connecting to server...")  
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))
print("[CLIENT] Connected to server")    
threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
while True:
    msg = input()
    client.send(msg.encode())
