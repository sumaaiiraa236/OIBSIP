A basic Python project demonstrating TCP socket communication between a client and a server.
1.Features
a.Server:
  - Listens for incoming connections.
  - Sends a welcome message to connected clients.
b.Client:
  - Connects to the server.
  - Receives and displays the server message.

->How to Run
1. Start the server in one terminal:
python server.py
2.Start the client in second terminal:
python client.py


Server output:
[SERVERSTARTED] Waiting for connection...
 [CONNECTED]Client from ('127.0.0.1', 64245)
[NEWCONNECTION]('127.0.0.1', 64245)CONNECTED.
Client output:
{WILL BE INTIMIATED IN THE SERVER TERMINAL}
