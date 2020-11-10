import time

for i in reversed(range(1,11)):
    # ANSI escape "\033[K" to clear till end of line
    print('\033[K', end='\r', flush=True)
    print('*'*i, end='\r')
    time.sleep(1)