import multiprocessing
import time
import os

def infinite_task():
    print(f"Process {os.getpid()} started infinite task")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    process = multiprocessing.Process(target=infinite_task)
    process.start()
    print(f"Started process with PID: {process.pid}")

    time.sleep(3)  # Let it run a bit

    print("Terminating the process...")
    process.terminate()
    process.join()

    print("Process terminated successfully")