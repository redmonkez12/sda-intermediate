from collections import deque


def processor(message):
    print("working...", message)


messages = []

while True:
    if messages:
        message = messages.pop()
        processor(message)
