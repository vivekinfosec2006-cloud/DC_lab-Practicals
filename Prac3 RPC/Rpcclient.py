import socket

s = socket.socket()
s.connect(("localhost", 6000))

msg = input("You: ")

s.send((msg + "\n").encode())

response = s.recv(1024).decode()

print(response)

s.close()