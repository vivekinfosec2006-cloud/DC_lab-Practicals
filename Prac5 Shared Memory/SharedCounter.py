import threading


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1


c = Counter()


def job():
    for i in range(1000):
        c.increment()


t1 = threading.Thread(target=job)
t2 = threading.Thread(target=job)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final counter =", c.value)