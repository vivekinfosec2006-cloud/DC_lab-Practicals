import socket

server = socket.socket()
server.bind(("localhost", 6000))
server.listen(1)

print("RPC Server started")

client, address = server.accept()

msg = client.recv(1024).decode()

print("Client:", msg)

client.send(("Server received: " + msg + "\n").encode())

client.close()
server.close()