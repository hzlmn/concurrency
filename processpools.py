import os
from concurrent.futures import (ProcessPoolExecutor, ThreadPoolExecutor,
                                as_completed, wait)


def task(value):
    print(f"Executing task with value {value}")
    while True:
        value * value
        print(f"Work done from {value}")


if __name__ == "__main__":
    try:
        executor = ProcessPoolExecutor(max_workers=os.cpu_count())

        tasks = [executor.submit(task, i) for i in range(0, 1000)]

        for fut in as_completed(tasks):
            print(fut.result())
    finally:
        executor.shutdown()
