## Conceptual Understanding Questions

**What's the key difference between parallelism and concurrency? Give an example of each.**  
Parallelism is the division of tasks into multiple processing units that execute simultaneously (at the same exact time), while concurrency involves tasks being executed interweavingly but not necessarily at the same time.  
*Example*: Parallelism - image processing where each CPU core processes different pixels simultaneously.  
Concurrency - a web server handling multiple requests by switching between them.

**Why are Embarrassingly Parallel Problems called "embarrassing"? What makes them ideal for parallelization?**  
EPP (Embarrassingly Parallel Problems) are called "embarrassing" because they are embarrassingly easy to parallelize. They don't present challenges because tasks are completely independent with no race conditions, deadlocks, or synchronization issues. You can use simple methods like parallel() or parallelStream().

**Explain the trade-off between fine-grained and coarse-grained task granularity. When would you choose each?**  
**Fine-grained**: Small chunks -> Many small tasks. Provides better load balancing but has more context switching overhead. Use for slow/variable tasks.  
**Coarse-grained**: Large chunks -> Few large tasks. Less overhead but worse load balancing. Use for fast/uniform tasks.

## Critical Thinking Questions

**You have 1000 very fast tasks and 1000 very slow tasks. How would you chunk them differently and why?**
For fast tasks, a coarse-grained approach would be preferable due to less overhead.
For slower tasks, a fine-grained approach is perfect due to splitting it into smaller tasks.

**Why is the "Poison Pill" pattern necessary in Master/Worker implementations? What would happen without it?**
The Master/Worker implementation relies on the Master providing its Workers with tasks in a continuous fashion. When there are no more tasks to do, the Threads/resources must be released. If there were no "Poison Pill" the Workers would stay allocated and waiting on more tasks. This would increase resource usage.

**A Fork/Join task keeps splitting work until it has 10,000 tiny subtasks. Is this good or bad? Explain.**
This is bad due to excessive overhead from task creation and management. However, Fork/Join doesn't create new threads for each subtask - it uses a fixed thread pool (ForkJoinPool) and work-stealing queues. The problem is the overhead of creating, scheduling, and joining too many tiny tasks, which outweighs the parallel benefit.

## Problem-Solving Scenarios

**You're processing a large image (like converting to black and white). Which programming design pattern would you choose: Master/Worker, Fork/Join, or Loop-level parallelism? Justify your choice.**
**Loop-level parallelism** would be best. Image processing is a classic embarrassingly parallel problem - each pixel can be processed independently with the same operation. This maps perfectly to loop-level parallelism (e.g., `parallelStream()` over pixels). Fork/Join is overkill since there's no recursive subdivision needed, and Master/Worker adds unnecessary complexity for this uniform workload.

**Your application has 90% reads and 10% writes to shared data. Which synchronization primitive would be most efficient and why?**
**ReadWriteLock** would be most efficient. It allows multiple readers to access simultaneously while giving writers exclusive access. Since 90% of operations are reads, many threads can read concurrently without blocking each other. Spinlock would cause unnecessary contention between readers.

**You need to ensure exactly 5 threads start processing simultaneously after all initialization is complete. Which synchronization primitive(s) would you use?**
**CyclicBarrier** with count=5 would be ideal. All 5 threads call `await()` and are blocked until all have reached the barrier, then they're all released simultaneously. CountDownLatch could work but is typically used when one thread waits for others to complete, not for mutual synchronization.

## Technical Details Questions

**What are the four necessary conditions for a deadlock to occur? How can you prevent each one?**
**Conditions**: Mutual exclusion, Hold and Wait, No preemption, and Circular wait.  
**Prevention**:

- **Mutual exclusion**: Use lock-free algorithms or make resources shareable
- **Hold and Wait**: Acquire all needed resources at once (all-or-nothing)
- **No preemption**: Allow resource preemption (timeout mechanisms)
- **Circular Wait**: Order resources and always acquire in the same order

**Compare Spinlock vs Mutex vs Futex. When would you use each?**
Spinlock is implemented simply and is good for low contention, very low latency. Mutex is a general purpose lock with a high context-switch/syscall overhead, can be fair or unfair. Futex is a fast hybrid but complex version of Mutex, that tries to do context-switching in the userspace, and if it can't, tries kernel-space.  

Usually Spinlock is used when the operations are very short, Mutex for general usages and Futex is used in **synchronized** and **Lock** implementations.

**Why can't you reuse a CountDownLatch but you can reuse a CyclicBarrier?**
CountDownLatch is a one-time-use mechanism, while a CyclicBarrier resets every time it hits the set count.  

## Implementation Questions

**In MapReduce, which phases are embarrassingly parallel and which aren't? Explain why.**
The mapping and reducing phase are both EP due to no concurrency issues arrising. Shuffling, however, needs Threads to be concurrent-safe, as it's joining the results of every single one to then be merged in the reduce phase.

**You're using BlockingQueue with producers faster than consumers. What happens to the queue? How does BlockingQueue handle this?**
The queue fills up to its capacity limit. When full, **producers** get blocked (not put in a queue) until consumers remove items, creating space. This provides automatic backpressure - producers are forced to wait, preventing memory overflow. The blocking is handled fairly (FIFO order for waiting producers).

**Why does work stealing in Fork/Join provide better load balancing than static work distribution?**
Because it ensures that, if a Thread gets stuck on some work, other Threads can come by and steal work on its queue, preventing it from slowing down the rest of the process.

## Java-Specific Questions

**What's the difference between synchronized and ReentrantLock? When would you choose one over the other?**
**synchronized**: Built-in, simpler syntax, automatic lock release, but limited features.
**ReentrantLock**: More flexible - supports timeouts, interruption, condition variables, fair/unfair modes, and try-lock operations.
**Choose synchronized** for simple cases due to ease of use.
**Choose ReentrantLock** when you need advanced features like timeouts, multiple conditions, or fair locking.

**When should you use parallelStream() vs manual thread management with ExecutorService?**
**Use parallelStream()** for embarrassingly parallel problems with simple operations on collections (map, filter, reduce).
**Use ExecutorService** for complex tasks, long-running operations, custom thread pools, or when you need fine control over thread lifecycle and task management. ExecutorService is better for continuous/complex workloads.

**How does the Java Memory Model affect visibility between threads? What keyword helps with this?**
The JMM allows CPU caches and compiler optimizations that can cause threads to see stale data. Changes made by one thread might not be immediately visible to other threads due to caching.
**The `volatile` keyword** ensures visibility by forcing reads/writes to go directly to main memory, bypassing caches.

## Design Pattern Comparison

**Compare Master/Worker vs Scatter/Gather. What are the key differences in terms of load balancing and synchronization?**
**Master/Worker**: Dynamic load balancing - workers pull tasks as they become available, providing good load distribution. Continuous synchronization via BlockingQueue. Uses Poison Pill for shutdown.
**Scatter/Gather**: Static load balancing - work divided upfront with no redistribution. Explicit synchronization barrier - waits for all tasks to complete. Resources released when all futures resolve.

**You have a recursive algorithm to process a tree structure. Should you use Fork/Join or Master/Worker? Why?**
A Fork/Join, as we don't know how big the tree structure is, as well as branching paths that Fork/Join naturally implements, while M/W would have a high overhead managing all the Threads.

## Performance & Optimization

**Your parallel program is slower than the sequential version. List 5 possible reasons why this might happen.**

1. **Thread creation/management overhead** exceeds work benefit
2. **Too small dataset** - parallelization overhead > actual work
3. **Lock contention** - threads spending time waiting for locks
4. **False sharing** - threads modifying adjacent memory locations
5. **Poor load balancing** - some threads finish early while others are still working

**How do you decide the optimal thread pool size for an ExecutorService?**
**CPU-bound tasks**: Number of cores (or cores + 1)  
**I/O-bound tasks**: Much higher (cores × blocking factor, often 2-50× cores)  
**Mixed workloads**: Profile and test different sizes
Consider memory constraints and context switching overhead. Start with cores and adjust based on monitoring.  

**Context switching is expensive. How does this affect your choice of scheduling strategy (Static/Dynamic/Guided)?**  
When context switching is expensive, prefer **Static** scheduling - work is divided once at the beginning, minimizing runtime overhead and context switches.  
**Dynamic** has more context switching due to frequent task assignments.  
**Guided** starts with large chunks (like static) then decreases, providing a compromise.

## Error-Prone Scenarios

**Why is semaphore usage "error-prone"? Give an example of incorrect usage.**
Semaphores are error-prone due to wrong acquire/release order and mismatched operations.
**Example**: Thread calls `acquire()` twice but only `release()` once, or calls `release()` without prior `acquire()`. This leads to permit leaks or deadlocks.
**Correct pattern**: Always pair acquire/release in try-finally blocks to ensure proper cleanup.

**What's a "spurious wakeup" in condition variables and how do you handle it?**
A spurious wakeup occurs when a thread is woken up from `wait()` even though no other thread called `notify()` or `notifyAll()`. This can happen due to OS-level interruptions.
**Solution**: Always use `wait()` in a while loop (not if), checking the condition again after wakeup:

```java
while (!condition) {
    wait();
}
```

## Real-World Application

**You're building a web crawler that needs to download 1 million web pages. Design a solution using the patterns from your notes. Which pattern(s) would you combine and why?**
**Master/Worker with ExecutorService** would be ideal:

- **Master**: Manages URL queue, handles discovered links, avoids duplicates
- **Workers**: Download pages, extract links, send results back
- **BlockingQueue**: Thread-safe URL distribution
- **I/O-bound tasks**: Use large thread pool (much more than CPU cores) since threads spend time waiting for network responses
- **Poison Pill**: Graceful shutdown when no more URLs to process

**Your system processes bank transactions. They must be processed in order for each account but can be parallel across different accounts. How would you design this?**
**Account-based partitioning with multiple single-threaded queues**:

- **One BlockingQueue per account**: Each account gets its own queue ensuring FIFO order
- **Worker threads**: Each worker processes one account's queue sequentially
- **Router/Dispatcher**: Distributes incoming transactions to correct account queue based on account ID
- **Dynamic load balancing**: When a worker finishes an account's transactions, it can pick up another account's queue
- **Hash partitioning**: Use account ID hash to assign accounts to worker threads consistently
