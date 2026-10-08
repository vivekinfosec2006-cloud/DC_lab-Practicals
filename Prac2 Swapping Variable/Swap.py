import threading


class Data:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.lock = threading.Lock()

    def swap(self):
        with self.lock:
            self.a, self.b = self.b, self.a
            print(f"After swap: a = {self.a}, b = {self.b}")


d = Data()

t1 = threading.Thread(target=d.swap)

t2 = threading.Thread(
    target=lambda: print(f"Read values: a = {d.a}, b = {d.b}")
)

t1.start()
t1.join()

t2.start()
t2.join()