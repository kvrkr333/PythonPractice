from timeit import timeit
from collections import deque
from simplequeue import SimpleQueue

SIZE = 1000000
TIMES = 10


def measure(function):
    time = timeit(function, number=TIMES)
    time_str = f"Execution time: {time/TIMES:.7f} seconds"
    settings = f"(SIZE: {SIZE}, TIMES: {TIMES}, {function.__name__})"
    print(time_str, settings)


def fifo_deque():
    a_queue = deque(range(SIZE))
    while a_queue:
        a_queue.popleft()


def fifo_simple_queue():
    a_queue = SimpleQueue()
    for i in range(SIZE):
        a_queue.append(i)
    while a_queue.popleft() is not None:
        pass


measure(fifo_deque)
measure(fifo_simple_queue)