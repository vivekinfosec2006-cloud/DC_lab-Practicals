import socket
import threading

def handle(client):
    try:
        while True:
            msg = client.recv(1024).decode()

            if not msg:
                break

            print("Client:", msg)
            client.send(("Echo: " + msg).encode())

    except:
        print("Client disconnected")

    finally:
        client.close()


server = socket.socket()
server.bind(("0.0.0.0", 5001))
server.listen()

print("Server started on port 5001")

while True:
    client, address = server.accept()
    threading.Thread(target=handle, args=(client,)).start()