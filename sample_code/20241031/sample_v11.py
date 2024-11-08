import time

# ANSI Terminal Colors
BLUE = '\033[94m'
RED = '\033[91m'
CLEAR = '\033[0m'

msg = "Hello, World!"

# Typewriter Effect

for char in msg:
    print(BLUE, char, sep='', end='', flush=True)
    time.sleep(0.1)

msg = "Happy Halloween!"
sleep = 0.5
print("\r", end='')
# Typewriter Effect

for char in msg:
    print(RED, char, sep='', end='', flush=True)
    time.sleep(0.1)

print(CLEAR)