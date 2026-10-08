state = {}


def stateful(client):
    count = state.get(client, 0) + 1
    state[client] = count
    print(f"Stateful {client}: request {count}")


def stateless(client):
    print(f"Stateless {client}: request handled")


stateful("C1")
stateful("C1")

stateless("C1")
stateless("C1")