import queue
import random
import time


def generate_request(q):
    request_id = random.randint(1000, 9999)
    print(f"Generating new request: {request_id}")
    q.put(request_id)


def process_request(q):
    if not q.empty():
        request = q.get()
        print(f"Processing the request: {request}")
    else:
        print("Queue is empty")


q = queue.Queue()


while True:
    generate_request(q)
    process_request(q)
    time.sleep(1)
