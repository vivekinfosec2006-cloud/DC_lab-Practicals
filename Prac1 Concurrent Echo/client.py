import socket

s = socket.socket()
s.connect(("localhost", 5001))

while True:
    msg = input("Enter message: ")

    if msg.lower() == "exit":
        break

    s.send((msg + "\n").encode())

    response = s.recv(1024).decode()
    print("Server:", response)

s.close()