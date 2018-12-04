import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from threading import Lock

sharable = {}


def task1(value, lock):
    with lock:
        print("Executing task1")
        time.sleep(3)
        sharable[value] = value
        print(sharable)
        return sharable


def task2(value, lock):
    with lock:
        print("executing task2")
        sharable[value] = value
        print(sharable)
        return sharable


def main():
    executor = ThreadPoolExecutor(max_workers=10)

    lock = Lock()

    jobs = [executor.submit(task1, "a", lock),
            executor.submit(task2, "b", lock)]

    results = as_completed(jobs)

    for fut in results:
        pass

    executor.shutdown()


if __name__ == "__main__":
    main()
