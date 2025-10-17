Conclusion:
The simulation demonstrates how using a lock ensures data consistency during concurrent access to shared resources. When multiple threads deposit money without synchronization, the final account balance becomes incorrect due to race conditions. However, with a lock mechanism, each transaction executes safely and sequentially, maintaining the correct final balance.

Difference:

Without Lock: Threads access and update the shared balance simultaneously, causing inconsistent or lost updates. The final balance may be incorrect.

With Lock: Only one thread updates the balance at a time, preventing data corruption. The correct final balance is achieved, though execution takes slightly longer due to sequential processing.
