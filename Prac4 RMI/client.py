import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:1099")

print(server.sayHello("Student"))