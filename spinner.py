import threading
import time
import sys
import contextlib

class Spinner(threading.Thread, contextlib.AbstractContextManager):
    actions = ['|','/','-','\\']
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        i = 0
        while self.running:
            i = i % 4
            print(self.actions[i], end='\r')
            time.sleep(0.1)
            i += 1
    
    def stop(self):
        self.running = False
    
    def __enter__(self):
        self.start()
    
    def __exit__(self, *exc):
        self.stop()
    
    # Should be able to replace with something in contextlib for newer python version 3.6+
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        
        return wrapper

spinner = Spinner()

@spinner
def worker():
    for i in range(5):
        print(f"Main thread {i}")
        time.sleep(0.5)

if __name__ == '__main__':
    print("First try - with normal setup")
    s = Spinner()
    s.start()

    for i in range(5):
        print(f"Main thread {i}")
        time.sleep(0.5)

    s.stop()

    print('='*10)
    time.sleep(2)
    print("Second try - with context manager")

    with Spinner():
        for i in range(5):
            print(f"Main thread {i}")
            time.sleep(0.5)

    time.sleep(2)
    print("Third try - with context manager decorator")

    worker()
