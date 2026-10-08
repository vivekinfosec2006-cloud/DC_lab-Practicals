import socket

s = socket.socket()
s.connect(("localhost", 5000))

msg = input("Enter message: ")

s.send((msg + "\n").encode())

response = s.recv(1024).decode()

print("Server:", response)

s.close()