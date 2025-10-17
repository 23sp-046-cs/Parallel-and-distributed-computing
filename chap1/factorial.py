import time
import multiprocessing
import threading

def heavy_task(size):
    total = 0
    for i in range(size):
        total += i * i
    return total

def run_test(size, proc_num, thread_num):
    print(f"\nRunning with {proc_num} processes and {thread_num} threads (size={size})")

    # Multiprocessing part
    jobs = []
    start_time = time.time()
    for _ in range(proc_num):
        process = multiprocessing.Process(target=heavy_task, args=(size,))
        jobs.append(process)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()

    end_time = time.time()
    print(f"Multiprocessing time with {proc_num} processes: {end_time - start_time:.4f} seconds")

    # Multithreading part
    jobs = []
    start_time = time.time()
    for _ in range(thread_num):
        thread = threading.Thread(target=heavy_task, args=(size,))
        jobs.append(thread)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()

    end_time = time.time()
    print(f"Multithreading time with {thread_num} threads: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    size = 10000000

    # Run tests with 5, 10, and 15 processes and threads
    for num in [5, 10, 15]:
        run_test(size, proc_num=num, thread_num=num)
