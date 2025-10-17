# Parallel-and-distributed-computing


![image alt](https://github.com/23sp-046-cs/Parallel-and-distributed-computing/blob/main/chap1/output.png?raw=true)



The conclusion from the results is that multiprocessing outperforms multithreading, especially when dealing with CPU-bound tasks or heavy computations.

Based on the observations:

With 5 processes and 5 threads, multiprocessing took around 1.8376 seconds, while multithreading took 4.3044 seconds.

As the number of workers increased, multiprocessing consistently performed better — e.g., 10 processes took 3.3026 seconds vs. 7.7333 for threads, and 15 processes took 4.9134 seconds vs. 11.9831 for threads.

This shows that multiprocessing can leverage multiple CPU cores more efficiently than threads, which are limited by Python’s Global Interpreter Lock (GIL) in CPU-bound scenarios.

However, the best approach still depends on your specific use case — including the nature of the task, system resources, and communication overhead between processes or threads.
