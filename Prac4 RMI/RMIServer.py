from xmlrpc.server import SimpleXMLRPCServer


def sayHello(name):
    return "Hello " + name + " from RMI Server"


server = SimpleXMLRPCServer(("localhost", 1099))

server.register_function(sayHello, "sayHello")

print("RMI Server ready")
server.serve_forever()