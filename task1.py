import os
import sys
from multiprocessing import Process

def child_process(i):
    print(f"Child {i+1}: PID = {os.getpid()}, Parent PID = {os.getppid()}, Message = Hello from child {i+1}")

def main():
    try:
        N = int(input("Enter the number of child processes: "))
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

    print(f"Parent process PID: {os.getpid()} creating {N} child processes...\n")

    processes = []
    for i in range(N):
        p = Process(target=child_process, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        print(f"Parent: Child with PID = {p.pid} finished")

if __name__ == "__main__":
    main()
