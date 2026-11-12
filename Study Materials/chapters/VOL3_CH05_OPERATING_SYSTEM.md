# Volume 3 — Chapter 5: Operating System

- **Source PDF**: [filter1_volume3.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume3.pdf)
- **Total GATE Questions in Chapter**: **343**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **5.2** | Best Fit | 1 |
| **5.3** | Context Switch | 4 |
| **5.4** | DMA | 1 |
| **5.5** | Deadlock Prevention Avoidance Detection | 4 |
| **5.6** | Demand Paging | 3 |
| **5.7** | Disk | 30 |
| **5.9** | File System | 7 |
| **5.11** | IO Handling | 7 |
| **5.12** | Input Output | 1 |
| **5.13** | Inter Process Communication | 1 |
| **5.15** | Least Recently Used | 1 |
| **5.16** | Linked Allocation | 1 |
| **5.17** | Memory Management | 9 |
| **5.18** | Multilevel Paging | 1 |
| **5.19** | OS Protection | 3 |
| **5.20** | Page Replacement | 31 |
| **5.21** | Precedence Graph | 3 |
| **5.23** | Process Scheduling | 49 |
| **5.24** | Process Synchronization | 52 |
| **5.25** | Resource Allocation | 27 |
| **5.27** | Round Robin Scheduling | 1 |
| **5.28** | Semaphore | 11 |
| **5.29** | Srtf | 1 |
| **5.30** | System Calls | 1 |
| **5.31** | Threads | 10 |
| **5.32** | Translation Lookaside Buffer | 2 |
| **5.33** | Virtual Memory | 43 |


---

## 2. Comprehensive GATE CSE Operating System Reference (Expanded Research & Formulas)

### 2.1 Process Management, `fork()` & CPU Scheduling
- **`fork()` System Call**:
  - $n$ unconditional consecutive `fork()` calls create **$2^n$ total processes** ($1$ parent + $2^n - 1$ child processes).
  - `fork()` returns **$0$ to the child process** and the **child's positive PID ($> 0$) to the parent process**.
- **CPU Scheduling Metrics**:
  - **Completion Time ($CT$)** $\rightarrow$ **Turnaround Time**: $\text{TAT} = \text{CT} - \text{AT}$
  - **Waiting Time**: $\text{WT} = \text{TAT} - \text{BT}$ (plus I/O wait if applicable)
  - **Response Time**: $\text{RT} = \text{First CPU Allocation Time} - \text{AT}$
  - **SRTF (Preemptive SJF)**: Provably **optimal (minimum) average Waiting Time**.
  - **Highest Response Ratio Next (HRRN)**: $\text{Response Ratio} = \frac{W + S}{S} = 1 + \frac{W}{S}$ (prevents starvation of long jobs while favoring short jobs).

### 2.2 Process Synchronization & Semaphores
- **Critical Section Requirements**:
  1. **Mutual Exclusion** (Mandatory)
  2. **Progress** (Mandatory: No deadlock when CS is free; only processes wanting to enter decide)
  3. **Bounded Waiting** (Prevents starvation; wait bounded by at most $N-1$ turns)
- **Peterson's 2-Process Solution** (`flag[2]`, `turn`): Satisfies **all 3** (Mutual Exclusion, Progress, Bounded Waiting).
- **Counting Semaphore ($S$)**:
  - If initial value is $S_0$, after $p$ `P(wait)` operations and $v$ `V(signal)` operations:
    $$S_{\text{final}} = S_0 - p + v$$
  - If $S_{\text{final}} < 0$, then $|S_{\text{final}}|$ is the **exact number of blocked processes** in the semaphore wait queue!

### 2.3 Deadlocks & Banker's Algorithm
- **4 Coffman Necessary Conditions**: (1) Mutual Exclusion, (2) Hold and Wait, (3) No Preemption, (4) Circular Wait.
- **Deadlock-Free Resource Threshold (Golden GATE Formula!)**:
  - If $n$ processes each need a maximum of $k_i$ instances of a single resource type, the system is **guaranteed deadlock-free** iff total instances $R$ satisfy:
    $$R \ge \sum_{i=1}^{n} (k_i - 1) + 1 = \left(\sum_{i=1}^{n} k_i\right) - n + 1$$
  - For identical max need $k$: Deadlock-free if $R \ge n(k - 1) + 1$; Max resources where deadlock is still possible: $R_{\max\text{ deadlock}} = n(k - 1)$.

### 2.4 Memory Management, Paging, TLB & Virtual Memory
- **Paging Address Translation** (Logical Address $= m$ bits, Physical Address $= f$ bits, Page Size $= P = 2^p$ bytes):
  - **Page Offset**: $p = \log_2 P$ bits (identical in logical and physical address!).
  - **Number of Pages in Process**: $2^{m - p}$; **Number of Frames in RAM**: $2^{f - p}$.
  - **Page Table Size (Single-Level)**: $2^{m - p} \times \text{PTE size}$.
  - **Multi-Level Paging**: If page table is split so each outer page table fits inside **1 page** ($P$ bytes), then entries per page table page $= \frac{P}{\text{PTE size}} = 2^k$, so each level consumes $k$ bits of the virtual page number.
- **Effective Memory Access Time (EMAT)**:
  - **With TLB** (Hit ratio $\alpha$, TLB access $t_{\text{TLB}}$, memory access $t_m$, $L$-level page table):
    $$\text{EMAT} = \alpha(t_{\text{TLB}} + t_m) + (1 - \alpha)\big(t_{\text{TLB}} + (L + 1)t_m\big)$$
  - **With Demand Paging / Page Faults** (Page fault rate $p$, page fault service time $S_{\text{pf}}$):
    $$\text{EMAT} = (1 - p) \times t_{\text{mem}} + p \times S_{\text{pf}}$$
- **Page Replacement Algorithms**:
  - **FIFO**: Suffers from **Belady's Anomaly** (for reference string `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`, 3 frames $\to 9$ faults, 4 frames $\to 10$ faults!).
  - **Optimal (OPT / Belady's MIN)** & **LRU (Least Recently Used)**: **Stack Algorithms** ($M(m, t) \subseteq M(m+1, t)$) $\implies$ **NEVER suffer from Belady's Anomaly**!

### 2.5 Disk Architecture, Scheduling & File Systems (Inodes)
- **Disk Access Time**:
  $$T_{\text{access}} = T_{\text{seek}} + T_{\text{rotational\_latency}} + T_{\text{transfer}} + T_{\text{controller}}$$
  where **Average Rotational Latency** $= \frac{1}{2} \times T_{\text{one\_rotation}} = \frac{1}{2} \times \frac{60}{\text{RPM}}$ seconds.
- **Disk Scheduling Algorithms**: `FCFS`, `SSTF` (Greedy shortest seek from current head; can cause starvation), `SCAN` (Elevator: goes to end of disk then reverses), `C-SCAN` (goes to end, jumps to other end without servicing on return), `LOOK` / `C-LOOK` (reverses at last request instead of physical disk end).
- **Unix Inode Maximum File Size**:
  - With block size $B$, block pointer size $p$, so $k = \lfloor B / p \rfloor$ pointers per indirect block, and $d$ direct, $1$ single-indirect, $1$ double-indirect, $1$ triple-indirect pointers:
    $$\text{Max File Size} = \big(d + k + k^2 + k^3\big) \times B$$

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

5 Operating System (343)
System calls, Processes, Threads, Inter‐process communication, Concurrency and synchronization.
Deadlock. CPU scheduling. Memory management and Virtual memory. File systems. Disks is also under this
Welcome to the Operating System (OS) chapter of your GATE Computer Science preparation! This section is designed
as a comprehensive, exam-focused reference to help you master the core concepts, formulas, and problem-solving
techniques essential for excelling in the GATE exam. Operating Systems form the bedrock of computing, managing
hardware and software resources to provide a stable and efficient environment for applications. For GATE CS, OS is a
high-scoring subject, typically carrying a weightage of 8-12 marks. Questions range from conceptual understanding of
OS principles, numerical problems on scheduling, memory management, and disk I/O, to analytical questions on
deadlock and synchronization. A strong grasp of this subject is crucial not only for GATE but also for a fundamental
understanding of computer science.
Topic-wise Key Concepts
Bankers Algorithm
The Banker's Algorithm is a deadlock avoidance algorithm that checks for a safe state before granting a resource
request. It ensures that the system can always find a sequence of processes that can complete their execution without
leading to a deadlock.
Important Formulas/Theorems:
1. Need Matrix: For each process and resource type , represents the remaining resources may still request.
2. Safety Algorithm:
Initialize and for all processes.
Find an such that and .
If such an exists, then and If no such exists, the system is in a safe state if 3. Resource-Request Algorithm:
If , proceed to step 2. Otherwise, error.
If , proceed to step 3. Otherwise, must wait.
Pretend to allocate resources: ,
. This
. Go to step 2.
for all .
, .
Run Safety Algorithm. If safe, grant request. If unsafe, revert allocation and waits.
Key Properties:
Ensures deadlock avoidance by maintaining the system in a safe state.
Requires prior knowledge of maximum resource needs for each process.
Less conservative than deadlock prevention, allowing higher resource utilization.
Common Pitfalls:
Confusing safe state with deadlock-free state (safe implies deadlock-free, but unsafe doesn't necessarily imply
deadlock).
Incorrectly calculating the Need matrix or updating Available/Allocation vectors.
Not checking all conditions in the Safety Algorithm or Resource-Request Algorithm.
Standard Problem-Solving Techniques:
Systematically trace the Safety Algorithm step-by-step, updating and arrays.
For resource requests, first check against and then against , then temporarily allocate and run
the Safety Algorithm.
Best Fit
Best Fit is a dynamic memory allocation algorithm that allocates the smallest available memory hole (partition) that is
large enough to satisfy a request. Its goal is to minimize the amount of internal fragmentation.

*(PDF Page 365)*

Key Properties:
Tends to produce the smallest leftover hole, which might be useful for future small requests.
Suffers from external fragmentation, where total free memory is sufficient but not contiguous.
Requires searching the entire list of free partitions to find the best fit, making it slower than First Fit.
Common Pitfalls:
Confusing it with First Fit or Worst Fit.
Incorrectly identifying the "smallest" suitable hole, especially when multiple holes have the same size.
Standard Problem-Solving Techniques:
Maintain a sorted list of free memory blocks (or iterate through all) and select the one with the smallest size
greater than or equal to the request.
Draw memory maps to visualize allocation and fragmentation.
Context Switch
A context switch is the mechanism by which the CPU saves the state of the currently executing process or thread and
restores the state of another process or thread. This allows multiple processes/threads to share a single CPU.
Key Properties:
Involves saving the Process Control Block (PCB) of the current process and loading the PCB of the next process.
An overhead operation, as the CPU is not performing useful work during the switch.
Latency is the time taken for a context switch.
More frequent context switches (e.g., small time quantum in Round Robin) increase overhead.
Common Pitfalls:
Underestimating the overhead of context switching in performance calculations.
Not understanding *what* exactly is saved (CPU registers, program counter, stack pointer, etc.).
DMA (Direct Memory Access)
DMA is a feature of computer systems that allows certain hardware subsystems (like disk drive controllers or network
cards) to access main system memory (RAM) independently of the central processing unit (CPU). This significantly
improves I/O performance by offloading data transfer from the CPU.
Key Properties:
Reduces CPU overhead for large data transfers, allowing the CPU to perform other tasks.
DMA controller manages the transfer, initiating an interrupt only upon completion.
"Cycle stealing" occurs when the DMA controller temporarily takes control of the system bus from the CPU to
transfer data.
Requires careful setup by the CPU (source, destination, size).
Common Pitfalls:
Thinking DMA eliminates CPU involvement entirely (CPU still initiates and handles completion).
Not understanding the concept of cycle stealing and its impact on CPU performance.
Deadlock Prevention Avoidance Detection
These are strategies to deal with deadlocks. Prevention aims to ensure that at least one of the four necessary
conditions for deadlock never holds. Avoidance dynamically grants resources only if the system remains in a safe state.
Detection allows deadlocks to occur and then finds and resolves them.
Important Formulas/Theorems:
1. Necessary Conditions for Deadlock (Coffman Conditions):
: Mutual Exclusion: At least one resource must be held in a non-sharable mode.
: Hold and Wait: A process holding at least one resource is waiting to acquire additional resources held
by other processes.
: No Preemption: Resources cannot be preempted; they can only be released voluntarily by the process
holding them.
: Circular Wait: A set of processes exists such that is waiting for a resource held
by , is waiting for a resource held by , ..., is waiting for a resource held by , and is
waiting for a resource held by .
2. Deadlock Prevention: Break one or more of the four conditions.
Break : Spooling (for printers), virtualizing resources.
Break : Request all resources at once, or release all resources before requesting new ones.
Break : Allow preemption of resources (e.g., CPU, memory).

*(PDF Page 366)*

Break : Impose a total ordering of resource types; processes must request resources in increasing order.
3. Deadlock Avoidance: Banker's Algorithm (for multiple instances of resources), Resource-Allocation Graph
Algorithm (for single instances).
4. Deadlock Detection:
If resources have single instances, use a Wait-For Graph. A cycle implies deadlock.
If resources have multiple instances, use an algorithm similar to Banker's Safety Algorithm.
Key Properties:
Prevention is conservative, often leading to low resource utilization.
Avoidance is more flexible but requires future knowledge of resource requests.
Detection allows higher concurrency but incurs overhead for detection and recovery.
Common Pitfalls:
Confusing which condition each prevention strategy addresses.
Incorrectly applying RAG for multiple instance resources (a cycle in RAG with multiple instances does not
necessarily imply deadlock).
Not understanding the trade-offs between the three strategies.
Standard Problem-Solving Techniques:
For prevention, identify which condition is being broken.
For avoidance, apply Banker's Algorithm.
For detection, draw the RAG or Wait-For Graph and look for cycles.
Demand Paging
Demand Paging is a virtual memory technique where pages are loaded into main memory only when they are
referenced (demanded) by the CPU. This allows for larger virtual address spaces than physical memory and reduces
I/O overhead by not loading unused pages.
Important Formulas/Theorems:
1. Effective Access Time (EAT):
Where is the page fault rate. includes time for interrupt, saving process state, reading
page from disk, updating page table, restoring process state.
Key Properties:
Leverages locality of reference to achieve good performance.
Reduces physical memory requirements for processes.
Introduces page faults, which are expensive operations.
Can lead to thrashing if the page fault rate becomes too high.
Common Pitfalls:
Incorrectly calculating EAT, especially the components of page fault overhead.
Misunderstanding the concept of locality of reference.
Confusing demand paging with simple paging.
Standard Problem-Solving Techniques:
Calculate EAT by plugging in given values for page fault rate, memory access time, and page fault overhead.
Analyze scenarios for thrashing.
Disk
A disk (hard disk drive) is a non-volatile storage device that stores data on rotating platters. It is characterized by its
physical structure and the time it takes to access data.
Important Formulas/Theorems:
1. Disk Access Time:
Seek Time: Time taken for the disk arm to move the read/write heads to the correct track.
Rotational Latency: Time taken for the desired sector to rotate under the read/write head (average is half a
rotation).
Transfer Time: Time taken to transfer the actual data.

*(PDF Page 367)*

Key Properties:
Data is stored in sectors, which are grouped into tracks, and tracks are stacked into cylinders.
Seek time is typically the most significant component of disk access time.
Mechanical components make disk access orders of magnitude slower than RAM access.
Common Pitfalls:
Incorrectly calculating average rotational latency (usually half a rotation).
Forgetting to include all three components of access time.
Standard Problem-Solving Techniques:
Break down the problem into calculating each component (seek, rotational, transfer) and then sum them up.
Disk Scheduling
Disk scheduling algorithms aim to minimize the total head movement of the disk arm, thereby reducing the average disk
access time and improving I/O throughput. They reorder pending disk I/O requests.
Important Formulas/Theorems:
1. Total Head Movement: Sum of absolute differences between consecutive track numbers accessed.
Algorithms:
FCFS (First-Come, First-Served): Processes requests in the order they arrive. Simple but inefficient.
SSTF (Shortest Seek Time First): Selects the request with the minimum seek time from the current head
position. Can lead to starvation.
SCAN (Elevator Algorithm): The disk arm moves from one end of the disk to the other, servicing requests
along the way. When it reaches an end, it reverses direction.
C-SCAN (Circular SCAN): Similar to SCAN, but when the arm reaches one end, it immediately returns to the
other end without servicing requests on the return trip. Provides more uniform wait times.
LOOK: Similar to SCAN, but the arm only goes as far as the last request in each direction, then reverses.
C-LOOK: Similar to C-SCAN, but the arm only goes as far as the last request in each direction, then returns to
the first request in the other direction without going to the absolute end.
Key Properties:
SSTF is optimal for average seek time but can cause starvation.
SCAN/C-SCAN/LOOK/C-LOOK provide better fairness and prevent starvation.
C-SCAN/C-LOOK are preferred for heavy loads as they provide more uniform service.
Common Pitfalls:
Incorrectly calculating head movement, especially for SCAN/C-SCAN/LOOK/C-LOOK where direction matters.
Forgetting to include the initial head position in the calculation.
Confusing SCAN with C-SCAN or LOOK with C-LOOK.
Standard Problem-Solving Techniques:
Draw a number line representing tracks and mark request positions. Trace the head movement for each
algorithm.
Carefully track the current head position and the direction of movement.
File System
A file system is an OS component that controls how data is stored and retrieved. It organizes files into a hierarchical
structure, manages file attributes, and provides mechanisms for accessing and protecting files.
Key Properties:
File Attributes: Name, type, location, size, protection, time/date, user ID.
File Operations: Create, write, read, reposition, delete, truncate.
Directory Structure: Single-level, two-level, tree-structured, acyclic-graph, general graph.
Allocation Methods: Contiguous, Linked, Indexed.
Free Space Management: Bit vector, linked list, grouping, counting.
Common Pitfalls:
Confusing file allocation methods (e.g., linked vs. indexed).
Not understanding the trade-offs of different directory structures (e.g., sharing, path length).
Fork System Call
The fork() system call creates a new process (child process) that is a duplicate of the calling process (parent process).
Both processes then execute concurrently from the point of the fork() call.
Key Properties:

*(PDF Page 368)*

The child process receives a copy of the parent's address space, including code, data, and stack segments
(often implemented using copy-on-write).
The child process gets a unique Process ID (PID).
fork() returns 0 to the child process, the child's PID to the parent process, and -1 on failure.
Child process inherits open file descriptors, signals, etc.
Common Pitfalls:
Incorrectly predicting the output of programs involving multiple fork() calls due to confusion about which process
is executing which part of the code.
Not understanding the return values of fork() in parent vs. child.
Assuming parent and child share memory directly (they get copies, though copy-on-write optimizes this).
Standard Problem-Solving Techniques:
Trace the execution path for both parent and child processes separately after each fork().
Keep track of the number of processes created. For fork() calls in a sequence, processes are created. If
fork() is in a loop, it's more complex.
IO Handling
I/O handling refers to the mechanisms and techniques used by the operating system to manage data transfer between
the CPU/memory and peripheral devices. Efficient I/O handling is crucial for system performance.
Key Properties:
Polling: CPU repeatedly checks the status of an I/O device. Simple but inefficient, wastes CPU cycles.
Interrupt-driven I/O: Device notifies the CPU via an interrupt when I/O is complete or ready. More efficient for
sporadic I/O.
DMA (Direct Memory Access): Device controller transfers data directly to/from memory without CPU
intervention. Most efficient for large data transfers.
Buffering: Using temporary memory areas to hold data during transfer, smoothing out speed differences.
Spooling: Holding data for a device (e.g., printer) in a buffer until the device is ready.
Common Pitfalls:
Confusing the efficiency and use cases of polling vs. interrupts vs. DMA.
Not understanding the role of device controllers.
Input Output
Input/Output (I/O) refers to the communication between an information processing system (like a computer) and the
outside world, possibly a human or another information processing system. It involves the transfer of data to and from
peripheral devices.
Key Properties:
Can be synchronous (CPU waits for I/O completion) or asynchronous (CPU continues processing while I/O
operates in background).
Managed by device controllers and device drivers.
Performance is often a bottleneck in overall system performance.
Inter Process Communication (IPC)
IPC refers to mechanisms provided by the operating system that allow independent processes to communicate and
synchronize their actions. This is essential for cooperative processes and distributed systems.
Key Properties:
Shared Memory: Processes share a region of memory for direct data exchange. Fastest IPC, but requires
explicit synchronization.
Message Passing: Processes communicate by sending and receiving messages. Simpler to implement for
small data transfers, easier to use in distributed systems.
Pipes: Unidirectional (ordinary pipes) or bidirectional (named pipes/FIFOs) communication channels.
Sockets: For network communication, allowing processes on different machines to communicate.
Semaphores/Mutexes/Monitors: Primarily for synchronization, but can indirectly facilitate communication by
coordinating access to shared resources.
Common Pitfalls:
Confusing shared memory with message passing (shared memory requires explicit synchronization, message
passing often has built-in synchronization).
Not understanding the difference between pipes and named pipes.

*(PDF Page 369)*

Interrupts
An interrupt is a signal to the CPU from a hardware device or a software program that indicates an event has occurred
and requires immediate attention. It causes the CPU to temporarily suspend its current task and execute a special
routine called an interrupt handler.
Key Properties:
Hardware Interrupts: Generated by I/O devices (e.g., disk completion, keyboard input).
Software Interrupts (Traps/Exceptions): Generated by programs (e.g., system calls, division by zero, page
fault).
Interrupt Vector: A table containing the addresses of interrupt service routines (ISRs) for various interrupt
types.
Maskable Interrupts: Can be temporarily ignored by the CPU.
Non-maskable Interrupts (NMI): Critical events that cannot be ignored (e.g., memory parity error).
Involves saving the CPU's context (registers, PC) before executing the ISR and restoring it afterward.
Common Pitfalls:
Confusing hardware interrupts with software interrupts (traps).
Not understanding the role of the interrupt vector.
Forgetting the context saving/restoring overhead.
Least Recently Used (LRU)
LRU is a page replacement algorithm that replaces the page that has not been used for the longest period of time. It is
based on the principle of temporal locality, assuming that pages recently used are likely to be used again soon.
Key Properties:
Generally performs well, approximating the optimal algorithm.
Does not suffer from Belady's anomaly (increasing page faults with more frames).
Difficult to implement efficiently in hardware, as it requires tracking the exact usage time of each page.
Approximations like Second Chance or Clock algorithm are often used in practice.
Common Pitfalls:
Incorrectly identifying the "least recently used" page, especially in complex sequences.
Confusing it with FIFO or LFU.
Standard Problem-Solving Techniques:
Maintain a "time stamp" or "counter" for each page, or conceptually keep a stack where the most recently used
page is at the top. When a page is referenced, move it to the top. When a page fault occurs, remove the page at
the bottom.
Trace the page references and page frames step-by-step.
Linked Allocation
Linked allocation is a file allocation method where each file is stored as a linked list of disk blocks. Each block contains
a pointer to the next block in the file.
Key Properties:
No external fragmentation, as any free block can be used.
Files can grow dynamically.
Sequential access is efficient, but direct access (random access) is very slow due to pointer traversal.
Pointer overhead: a portion of each disk block is used for the pointer, reducing data storage capacity.
Reliability issue: a lost or damaged pointer can lead to the loss of the rest of the file.
Common Pitfalls:
Confusing it with contiguous or indexed allocation.
Overlooking the performance impact on random access or the pointer overhead.
Memory Management
Memory management is the operating system's function of handling primary memory. It allocates memory to processes,
protects processes from each other, and provides an abstraction of a large, uniform memory space.
Key Properties:
Relocation: Mapping logical addresses to physical addresses.
Protection: Preventing processes from accessing each other's memory.

*(PDF Page 370)*

Sharing: Allowing processes to share memory regions.
Logical Organization: Segmentation, paging.
Physical Organization: Contiguous allocation, non-contiguous allocation.
Techniques: Paging, segmentation, virtual memory.
Common Pitfalls:
Confusing internal vs. external fragmentation.
Not understanding the difference between logical and physical addresses.
Multilevel Paging
Multilevel paging (or hierarchical paging) is a technique used in virtual memory systems to reduce the size of the page
table. Instead of a single, large page table, it uses a tree-like structure of page tables, where the outer page table points
to inner page tables, which then point to physical frames.
Important Formulas/Theorems:
1. Effective Access Time (EAT) for N-level Paging:
(Assuming no TLB and page tables are in memory).
2. Number of Bits for Page Number: If a logical address is bits and page size is bytes, then page offset is
bits, and page number is bits.
3. Number of Entries in Page Table: .
4. Size of Page Table: .
Key Properties:
Reduces the amount of physical memory required for page tables, especially for sparse address spaces.
Increases memory access time because multiple memory accesses are needed to find a physical address (one
for each level of page table).
Can be combined with TLB to mitigate increased access time.
Common Pitfalls:
Incorrectly calculating the number of bits for each level of the page table.
Forgetting to account for all memory accesses when calculating EAT without TLB.
Standard Problem-Solving Techniques:
Break down the virtual address into segments corresponding to each level of the page table and the page offset.
Calculate the number of page table entries and the size of each page table level.
OS Protection
OS protection mechanisms ensure that system resources (CPU, memory, files, I/O devices) are used only in ways
authorized by the operating system. This prevents malicious or erroneous programs from harming the system or other
programs.
Key Properties:
Dual-Mode Operation: User mode (restricted privileges) and Kernel mode (full privileges). A mode bit indicates
the current mode.
Privileged Instructions: Instructions that can only be executed in kernel mode (e.g., I/O instructions, setting
timer).
System Calls: User programs request OS services, transitioning from user to kernel mode.
Memory Protection: Base and limit registers, paging, segmentation.
Access Control Lists (ACLs): For files and other resources, specifying who can access what and how.
Capabilities: Tokens that grant specific access rights to a resource.
Common Pitfalls:
Confusing the purpose of dual-mode operation with memory protection.
Not understanding how system calls facilitate a controlled transition to kernel mode.
Page Replacement
Page replacement algorithms decide which page to remove from main memory when a page fault occurs and no free
frames are available. The goal is to minimize the number of page faults.
Important Formulas/Theorems:

*(PDF Page 371)*

1. Hit Ratio:
2. Miss Ratio (Page Fault Rate):
3.
Algorithms:
FIFO (First-In, First-Out): Replaces the page that has been in memory the longest. Simple but can suffer from
Belady's anomaly.
Optimal (OPT/MIN): Replaces the page that will not be used for the longest period of time in the future.
Impossible to implement in practice, used as a benchmark.
LRU (Least Recently Used): Replaces the page that has not been used for the longest time. Generally good
performance, does not suffer from Belady's anomaly, but complex to implement.
LFU (Least Frequently Used): Replaces the page with the smallest count of references.
MFU (Most Frequently Used): Replaces the page with the largest count of references (less common).
Second Chance (Clock): A FIFO variant that gives a page a "second chance" if its reference bit is set.
Key Properties:
Belady's anomaly: For some algorithms (like FIFO), increasing the number of available page frames can
increase the number of page faults.
Optimal algorithm provides the theoretical minimum number of page faults.
Common Pitfalls:
Incorrectly applying the rules for each algorithm, especially for LRU and Optimal.
Forgetting to count the initial page loads as page faults.
Misinterpreting Belady's anomaly.
Standard Problem-Solving Techniques:
Trace the page reference string through the page frames for each algorithm, step-by-step, marking hits and
faults.
Keep track of the state of each page (e.g., arrival time for FIFO, last used time for LRU, future use for Optimal).
Precedence Graph
A precedence graph (or process graph) is a directed acyclic graph (DAG) used to represent the execution order and
dependencies among a set of tasks or processes. An edge from task A to task B means task A must complete before
task B can start.
Key Properties:
Nodes represent tasks/processes, edges represent dependencies.
Helps in identifying potential parallelism and critical paths.
Used in scheduling to ensure correct execution order.
Must be acyclic to represent a valid execution sequence.
Common Pitfalls:
Drawing cycles, which implies an impossible dependency.
Misinterpreting the meaning of an edge (A -> B means A must finish before B starts, not just that B follows A).
Process
A process is a program in execution. It is an active entity, unlike a program, which is a passive entity. Each process has
its own address space, resources, and execution context.
Key Properties:
Process Control Block (PCB): Contains all information about a process (state, PC, registers, memory limits,
open files, etc.).
Process States:
New: Process being created.
Ready: Waiting to be assigned to a processor.
Running: Instructions are being executed.
Waiting (Blocked): Waiting for some event (e.g., I/O completion, signal).
Terminated: Process has finished execution.
Each process has its own virtual address space, including code, data, and stack segments.
Processes are typically heavy-weight compared to threads.
Common Pitfalls:
Confusing a process with a program or a thread.
Incorrectly identifying transitions between process states.

*(PDF Page 372)*

Process Scheduling
Process scheduling is the activity of the operating system that selects which process to run next from the ready queue
and allocates the CPU to it. The goal is to optimize various performance metrics.
Important Formulas/Theorems:
1. Turnaround Time (TAT):
2. Waiting Time (WT):
3. Response Time (RT):
4. Throughput: Number of processes completed per unit time.
5. CPU Utilization: Percentage of time the CPU is busy.
Algorithms:
FCFS (First-Come, First-Served): Non-preemptive. Simple, but can have high average waiting time (convoy
effect).
SJF (Shortest Job First): Non-preemptive. Optimal for minimum average waiting time. Requires knowing future
burst times.
SRTF (Shortest Remaining Time First): Preemptive version of SJF. Optimal for minimum average waiting
time.
Priority Scheduling: Can be preemptive or non-preemptive. Processes with higher priority run first. Can lead to
starvation (low-priority processes never run).
Round Robin (RR): Preemptive. Each process gets a small unit of CPU time (time quantum). Fair, good for
interactive systems.
Key Properties:
Preemptive: CPU can be taken away from a running process.
Non-preemptive: CPU is held until process completes or blocks.
Starvation: A process may wait indefinitely.
Aging: Gradually increasing the priority of processes that wait for a long time to prevent starvation.
Common Pitfalls:
Incorrectly drawing Gantt charts, especially for preemptive algorithms.
Mistakes in calculating TAT, WT, or RT.
Confusing preemptive vs. non-preemptive versions of algorithms.
Not handling arrival times correctly.
Standard Problem-Solving Techniques:
Draw a Gantt chart for each algorithm, carefully marking arrival, start, and completion times.
Systematically calculate TAT, WT, and RT for each process and then their averages.
For preemptive algorithms, check for preemption at every arrival or completion event.
Process Synchronization
Process synchronization refers to the coordination of multiple processes to ensure that they access shared resources or
critical sections in a controlled manner, preventing race conditions and maintaining data consistency.
Important Formulas/Theorems:
1. Critical Section Problem Requirements:
Mutual Exclusion: Only one process can be in its critical section at any time.
Progress: If no process is in its critical section and some processes want to enter, only those not in their
remainder section can participate in the decision, and this decision cannot be postponed indefinitely.
Bounded Waiting: There is a limit on the number of times other processes can enter their critical sections
after a process has made a request to enter its critical section and before that request is granted.
Mechanisms:
Semaphores: Integer variables accessed only through atomic wait() (P) and signal() (V) operations. Can be
binary (mutex) or counting.
Mutex Locks: A simpler binary semaphore, used for mutual exclusion.
Monitors: High-level synchronization construct that encapsulates shared data and procedures that operate on
the data, ensuring mutual exclusion and providing condition variables for waiting.
Hardware Solutions: TestAndSet, Swap instructions.
Key Properties:
Race Condition: When multiple processes access and modify shared data concurrently, and the final result
depends on the order of execution.
Deadlock: Can occur with improper use of synchronization primitives (e.g., two processes waiting for each
other's resources).
Common Pitfalls:

*(PDF Page 373)*

Incorrectly using wait() and signal() operations, leading to deadlock or starvation.
Not ensuring atomicity of synchronization primitives.
Confusing mutexes with counting semaphores.
Standard Problem-Solving Techniques:
Trace the execution flow of multiple processes accessing shared resources, observing the values of semaphores
or mutexes.
Identify potential race conditions and propose synchronization solutions.
Analyze classic synchronization problems (Producer-Consumer, Readers-Writers, Dining Philosophers).
Resource Allocation
Resource allocation is the process by which the operating system assigns available resources (CPU, memory, I/O
devices, files) to processes. This is a fundamental task of the OS, impacting system performance and stability.
Key Properties:
Resources can be preemptable (e.g., CPU) or non-preemptable (e.g., printer).
Proper resource allocation is critical to prevent deadlocks and ensure fairness.
Involves policies for granting requests and reclaiming resources.
Resource Allocation Graph (RAG)
A Resource Allocation Graph is a directed graph used to depict the state of a system regarding resources and
processes. It helps in visualizing resource allocation and detecting deadlocks.
Key Properties:
Nodes: Processes (circles) and Resource types (rectangles).
Edges:
Request Edge: From process to resource type (e.g., ), indicating is requesting an instance of
.
Assignment Edge: From resource type to process (e.g., ), indicating an instance of has been
allocated to .
If the RAG contains a cycle, and each resource type has only one instance, then a deadlock exists.
If the RAG contains a cycle, and some resource types have multiple instances, a deadlock may exist (further
analysis needed).
Common Pitfalls:
Incorrectly drawing request vs. assignment edges.
Assuming a cycle always implies deadlock, especially for multiple-instance resources.
Not understanding the difference between RAG and Wait-For Graph.
Standard Problem-Solving Techniques:
Draw the RAG based on the given process and resource states.
Identify cycles in the graph.
If cycles exist, determine if they lead to deadlock based on resource instance counts.
Round Robin Scheduling
Round Robin (RR) is a preemptive process scheduling algorithm designed for time-sharing systems. Each process is
given a small unit of CPU time, called a time quantum (or time slice). When the quantum expires, the process is
preempted and added to the end of the ready queue.
Important Formulas/Theorems:
1. Turnaround Time (TAT):
2. Waiting Time (WT):
3. Number of Context Switches: Depends on the number of processes and the time quantum.
Key Properties:
Fair scheduling, as every process gets a chance to run.
Good for interactive systems, providing quick response times.
Performance heavily depends on the time quantum:
Small quantum: High context switch overhead, good response time.
Large quantum: Approaches FCFS, lower overhead, potentially poor response time.
Common Pitfalls:
Incorrectly handling the time quantum and preemption points.
Mistakes in calculating TAT or WT, especially when processes arrive at different times.

*(PDF Page 374)*

Forgetting to account for context switch overhead if specified in the problem.
Standard Problem-Solving Techniques:
Draw a Gantt chart, carefully allocating CPU time in quantum chunks and moving processes to the end of the
ready queue upon preemption.
Keep track of remaining burst times for each process.
Semaphore
A semaphore is a synchronization primitive, a protected integer variable that can only be accessed and modified by two
atomic operations: wait() (also known as P or down) and signal() (also known as V or up).
Important Formulas/Theorems:
1. wait(S) operation:
wait(S) {
S--;
while (S <= 0); // busy wait
}
(Alternatively, block the process if 2. signal(S) operation:
).
signal(S) {
S++;
}
(Alternatively, wake up a blocked process if any).
Key Properties:
Counting Semaphore: Can range over an unrestricted domain. Used to control access to a resource with
multiple instances.
Binary Semaphore (Mutex): Can only be 0 or 1. Used for mutual exclusion (like a lock).
Can be used for both mutual exclusion and process synchronization (ordering of events).
Improper use can lead to deadlock or starvation.
Common Pitfalls:
Swapping the order of wait() and signal() operations, leading to incorrect synchronization.
Using busy-waiting semaphores in a single-processor system (wastes CPU cycles).
Not initializing semaphores correctly.
Standard Problem-Solving Techniques:
Trace the values of semaphores as processes execute wait() and signal() operations.
Identify critical sections and shared resources to determine appropriate semaphore usage.
Solve classic synchronization problems using semaphores.
SRTF (Shortest Remaining Time First)
SRTF is a preemptive version of the Shortest Job First (SJF) scheduling algorithm. The CPU is allocated to the process
with the smallest remaining burst time. If a new process arrives with a shorter burst time than the currently running
process's remaining time, the current process is preempted.
Important Formulas/Theorems:
1. Turnaround Time (TAT):
2. Waiting Time (WT):
Key Properties:
Optimal for minimizing average waiting time.
Requires knowing the remaining burst time of all processes, which is difficult in practice.
High overhead due to frequent context switches, especially with many short jobs or frequent arrivals.
Can suffer from starvation if a continuous stream of short jobs keeps arriving.
Common Pitfalls:
Incorrectly determining when preemption occurs (at every arrival or when a shorter job becomes ready).
Mistakes in calculating remaining burst times.
Overlooking processes that arrive later but have very short burst times.
Standard Problem-Solving Techniques:
Create a Gantt chart, carefully tracking the remaining burst time of all ready processes at each time unit.
At each time unit, check for new arrivals and select the process with the minimum remaining burst time.

*(PDF Page 375)*

System Calls
System calls provide an interface between a running program and the operating system. They allow user-level
programs to request services from the OS kernel, such as file I/O, process creation, memory allocation, and device
access.
Key Properties:
Transition from user mode to kernel mode (privileged mode).
Typically invoked through a software interrupt (trap).
Provide a controlled and secure way for user programs to access protected resources.
Examples: fork(), exec(), read(), write(), open(), close(), wait(), exit().
Common Pitfalls:
Confusing system calls with library calls (library calls are user-level functions that may or may not invoke system
calls).
Not understanding the mode switch involved.
Threads
A thread (or lightweight process) is a basic unit of CPU utilization within a process. Multiple threads within the same
process share the same code section, data section, and other OS resources (like open files, signals), but each has its
own program counter, register set, and stack.
Key Properties:
Faster Context Switching: Switching between threads in the same process is faster than switching between
processes.
Resource Sharing: Threads within a process share memory and resources, facilitating communication.
Concurrency: Multiple threads can execute concurrently, improving application responsiveness and throughput
on multi-core systems.
User-level Threads: Managed by a user-level library, faster to create/manage, but if one thread blocks, the
entire process blocks.
Kernel-level Threads: Managed by the OS kernel, slower to create/manage, but if one thread blocks, others
can still run.
Many-to-One, One-to-One, Many-to-Many models: Different mappings between user and kernel threads.
Common Pitfalls:
Confusing threads with processes (threads share memory, processes do not).
Forgetting that synchronization is still required for shared data among threads.
Misunderstanding the implications of user-level vs. kernel-level threads.
Translation Lookaside Buffer (TLB)
The TLB is a small, fast hardware cache that stores recent virtual-to-physical address translations. It is used to speed
up memory access in paged virtual memory systems by avoiding multiple memory accesses to the page table.
Important Formulas/Theorems:
1. Effective Access Time (EAT) with TLB:
Where is the time to access the page table in main memory. If the page table is
also in memory, this is another .
Key Properties:
Significantly reduces the average memory access time if the hit ratio is high.
A TLB miss requires a page table walk (accessing the page table in main memory).
TLB entries are flushed on context switches between processes (though some TLBs support ASIDs to avoid
this).
Common Pitfalls:
Incorrectly calculating EAT, especially the components for a TLB miss (TLB access + memory access for page
table + memory access for data).
Forgetting to include TLB access time even on a hit.
Standard Problem-Solving Techniques:
Carefully plug values into the EAT formula, ensuring all access times are accounted for.
Understand how a TLB miss impacts the total access time.

*(PDF Page 376)*

Virtual Memory
Virtual memory is a memory management technique that provides an application with an illusion of a contiguous, large
address space, even if the physical memory is fragmented or smaller than the virtual address space. It separates logical
memory from physical memory.
Key Properties:
Allows programs to be larger than physical memory.
Enables efficient sharing of memory among multiple processes.
Provides memory protection.
Commonly implemented using paging (demand paging) and swapping.
Introduces the concept of page faults.
Important Formulas/Theorems:
1. Effective Access Time (EAT): (See Demand Paging and TLB sections for detailed formulas).
Common Pitfalls:
Confusing virtual memory with physical memory.
Not understanding the role of the MMU (Memory Management Unit) in address translation.
Misinterpreting the benefits and overheads of virtual memory.
Quick Formula Reference
Banker's Algorithm:
Need Matrix:
Demand Paging / Virtual Memory EAT (without TLB):
where is page fault rate.
Disk Access Time:
Multilevel Paging EAT (without TLB):
for -level paging, assuming page tables are in memory.
Page Replacement:
Hit Ratio:
Miss Ratio (Page Fault Rate):
Process Scheduling Metrics:
Turnaround Time (TAT):
Waiting Time (WT):
Response Time (RT):
TLB EAT:
Important Tips for GATE
1. Master Numerical Problems: A significant portion of OS questions in GATE are numerical, especially from Process
Scheduling (FCFS, SJF, SRTF, RR), Memory Management (Paging, Page Replacement, TLB EAT), and Disk
Scheduling. Practice drawing Gantt charts and calculating metrics meticulously.
2. Understand Preemption: Pay close attention to whether a scheduling algorithm is preemptive or non-preemptive.

*(PDF Page 377)*

This is a common source of error in Gantt chart construction. For preemptive algorithms, always check for new
arrivals at each time unit.
3. Trace Algorithms Systematically: For complex algorithms like Banker's, Page Replacement, or Disk Scheduling,
trace the steps methodically. Draw diagrams (RAG, memory maps, Gantt charts) to visualize the state changes.
4. Differentiate Similar Concepts: Be clear on the distinctions between processes and threads, mutexes and
semaphores, internal and external fragmentation, logical and physical addresses, and different deadlock strategies
(prevention, avoidance, detection).
5. Read Questions Carefully: Look for keywords like "average,
" "minimum,
" "maximum,
" "at least,
" "at most,
"
"preemptive,
" "non-preemptive,
" and specific units (ms, ns). A small detail can change the entire answer.
6. Focus on Trade-offs: Many OS concepts involve trade-offs (e.g., performance vs. fairness in scheduling, memory
usage vs. access time in paging). Understand why certain design choices are made and their implications.
7. Review Formulas Regularly: Keep the key formulas for EAT, scheduling metrics, and disk access time handy and
review them frequently. Understand the components of each formula.
8. Practice with GATE Previous Year Questions: This will help you understand the common question patterns,
difficulty levels, and time management strategies specific to the GATE exam.
Bankers Algorithm (2)

---

## 4. Complete Question Index & Answer Key Record (342 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `5.1.1` | Bankers Algorithm: GATE CSE 2018 \| Question: 39 | **A** |
| `5.1.2` | Bankers Algorithm: GATE CSE 2026 \| Set 1 \| Question: 19 | **A;C** |
| `5.2.1` | Best Fit: GATE CSE 2026 \| Set 2 \| Question: 45 | **3:3** |
| `5.3.1` | Context Switch: GATE CSE 1999 \| Question: 2.12 | **C** |
| `5.3.2` | Context Switch: GATE CSE 2000 \| Question: 1.20, ISRO2008-47 | **B** |
| `5.3.3` | Context Switch: GATE CSE 2011 \| Question: 6, UGCNET-June2013-III: 62 | **C** |
| `5.3.4` | Context Switch: GATE CSE 2024 \| Set 2 \| Question: 15 | **A;B** |
| `5.4.1` | DMA: GATE CSE 2001 \| Question: 8 | **800** |
| `5.5.1` | Deadlock Prevention Avoidance Detection: GATE CSE 2018 \| Question: 24 | **2** |
| `5.5.2` | Deadlock Prevention Avoidance Detection: GATE CSE 2021 \| Set 2 \| Question: 43 | **A;B;C** |
| `5.5.3` | Deadlock Prevention Avoidance Detection: GATE CSE 2026 \| Set 1 \| Question: 25 | **06** |
| `5.5.4` | Deadlock Prevention Avoidance Detection: GATE IT 2004 \| Question: 63 | **A** |
| `5.6.1` | Demand Paging: GATE CSE 2022 \| Question: 54 | **0.6** |
| `5.6.2` | Demand Paging: GATE CSE 2025 \| Set 1 \| Question: 4 | **A** |
| `5.6.3` | Demand Paging: GATE CSE 2025 \| Set 2 \| Question: 37 | **D** |
| `5.7.1` | Disk: GATE CSE 1990 \| Question: 7-c | **N/A** |
| `5.7.2` | Disk: GATE CSE 1993 \| Question: 6.7 | **N/A** |
| `5.7.3` | Disk: GATE CSE 1993 \| Question: 7.8 | **B** |
| `5.7.4` | Disk: GATE CSE 1995 \| Question: 14 | **N/A** |
| `5.7.5` | Disk: GATE CSE 1996 \| Question: 23 | **N/A** |
| `5.7.6` | Disk: GATE CSE 1997 \| Question: 74 | **9.006** |
| `5.7.7` | Disk: GATE CSE 1998 \| Question: 2-9 | **D** |
| `5.7.8` | Disk: GATE CSE 1998 \| Question: 25-a | **N/A** |
| `5.7.9` | Disk: GATE CSE 1998 \| Question: 25b | **N/A** |
| `5.7.10` | Disk: GATE CSE 1999 \| Question: 2-18, ISRO2008-46 | **D** |
| `5.7.11` | Disk: GATE CSE 2001 \| Question: 1.22 | **D** |
| `5.7.12` | Disk: GATE CSE 2003 \| Question: 25, ISRO2009-12 | **A** |
| `5.7.13` | Disk: GATE CSE 2004 \| Question: 49 | **C** |
| `5.7.14` | Disk: GATE CSE 2005 \| Question: 21 | **B** |
| `5.7.15` | Disk: GATE CSE 2007 \| Question: 11, ISRO2009-36, ISRO2016-21 | **A** |
| `5.7.16` | Disk: GATE CSE 2008 \| Question: 32 | **B** |
| `5.7.17` | Disk: GATE CSE 2009 \| Question: 51 | **C** |
| `5.7.18` | Disk: GATE CSE 2009 \| Question: 52 | **C** |
| `5.7.19` | Disk: GATE CSE 2011 \| Question: 44 | **B** |
| `5.7.20` | Disk: GATE CSE 2012 \| Question: 41 | **B** |
| `5.7.21` | Disk: GATE CSE 2013 \| Question: 29 | **D** |
| `5.7.22` | Disk: GATE CSE 2014 \| Set 2 \| Question: 20 | **99.55** |
| `5.7.23` | Disk: GATE CSE 2015 \| Set 1 \| Question: 48 | **14020** |
| `5.7.24` | Disk: GATE CSE 2015 \| Set 2 \| Question: 49 | **6.1** |
| `5.7.25` | Disk: GATE CSE 2024 \| Set 1 \| Question: 44 | **4096** |
| `5.7.26` | Disk: GATE CSE 2024 \| Set 2 \| Question: 43 | **30.06** |
| `5.7.27` | Disk: GATE IT 2005 \| Question: 63 | **C** |
| `5.7.28` | Disk: GATE IT 2005 \| Question: 81-a | **D** |
| `5.7.29` | Disk: GATE IT 2005 \| Question: 81-b | **B** |
| `5.7.30` | Disk: GATE IT 2007 \| Question: 44, ISRO2015-34 | **D** |
| `5.8.1` | Disk Scheduling: GATE CSE 1989 \| Question: 4-xii | **N/A** |
| `5.8.2` | Disk Scheduling: GATE CSE 1990 \| Question: 9b | **N/A** |
| `5.8.3` | Disk Scheduling: GATE CSE 1995 \| Question: 20 | **N/A** |
| `5.8.4` | Disk Scheduling: GATE CSE 1997 \| Question: 3.6 | **C** |
| `5.8.5` | Disk Scheduling: GATE CSE 1999 \| Question: 1.10 | **B** |
| `5.8.6` | Disk Scheduling: GATE CSE 2001 \| Question: 20 | **A** |
| `5.8.7` | Disk Scheduling: GATE CSE 2004 \| Question: 12 | **D** |
| `5.8.8` | Disk Scheduling: GATE CSE 2009 \| Question: 31 | **B** |
| `5.8.9` | Disk Scheduling: GATE CSE 2014 \| Set 1 \| Question: 19 | **3** |
| `5.8.10` | Disk Scheduling: GATE CSE 2015 \| Set 1 \| Question: 30 | **10** |
| `5.8.11` | Disk Scheduling: GATE CSE 2016 \| Set 1 \| Question: 48 | **346** |
| `5.8.12` | Disk Scheduling: GATE CSE 2018 \| Question: 53 | **85** |
| `5.8.13` | Disk Scheduling: GATE CSE 2020 \| Question: 35 | **B** |
| `5.8.14` | Disk Scheduling: GATE IT 2004 \| Question: 62 | **C** |
| `5.8.15` | Disk Scheduling: GATE IT 2007 \| Question: 82 | **B** |
| `5.8.16` | Disk Scheduling: GATE IT 2007 \| Question: 83 | **C** |
| `5.9.1` | File System: GATE CSE 2002 \| Question: 2.22 | **C** |
| `5.9.2` | File System: GATE CSE 2008 \| Question: 20 | **D** |
| `5.9.3` | File System: GATE CSE 2017 \| Set 2 \| Question: 08 | **D** |
| `5.9.4` | File System: GATE CSE 2019 \| Question: 42 | **4.0** |
| `5.9.5` | File System: GATE CSE 2021 \| Set 1 \| Question: 15 | **A;C** |
| `5.9.6` | File System: GATE CSE 2022 \| Question: 53 | **153** |
| `5.9.7` | File System: GATE IT 2004 \| Question: 67 | **B** |
| `5.10.1` | Fork System Call: GATE CSE 2005 \| Question: 72 | **C** |
| `5.10.2` | Fork System Call: GATE CSE 2008 \| Question: 66 | **B** |
| `5.10.3` | Fork System Call: GATE CSE 2012 \| Question: 8 | **C** |
| `5.10.4` | Fork System Call: GATE CSE 2019 \| Question: 17 | **31** |
| `5.10.5` | Fork System Call: GATE CSE 2023 \| Question: 13 | **C;D** |
| `5.10.6` | Fork System Call: GATE CSE 2024 \| Set 1 \| Question: 47 | **14** |
| `5.10.7` | Fork System Call: GATE CSE 2026 \| Set 1 \| Question: 53 | **4** |
| `5.10.8` | Fork System Call: GATE IT 2004 \| Question: 64 | **C** |
| `5.11.1` | IO Handling: GATE CSE 1996 \| Question: 1.20, ISRO2008-56 | **A** |
| `5.11.2` | IO Handling: GATE CSE 1998 \| Question: 1.29 | **B** |
| `5.11.3` | IO Handling: GATE CSE 2005 \| Question: 19 | **C** |
| `5.11.4` | IO Handling: GATE CSE 2005 \| Question: 20 | **A** |
| `5.11.5` | IO Handling: GATE CSE 2018 \| Question: 9 | **A** |
| `5.11.6` | IO Handling: GATE IT 2004 \| Question: 11, ISRO2011-33 | **B** |
| `5.11.7` | IO Handling: GATE IT 2006 \| Question: 8 | **C** |
| `5.12.1` | Input Output: GATE CSE 2025 \| Set 1 \| Question: 19 | **21:21** |
| `5.13.1` | Inter Process Communication: GATE CSE 1997 \| Question: 3.7 | **B** |
| `5.14.2` | Interrupts: GATE CSE 1997 \| Question: 3.8 | **D** |
| `5.14.3` | Interrupts: GATE CSE 1998 \| Question: 1.18 | **A** |
| `5.14.4` | Interrupts: GATE CSE 1999 \| Question: 1.9 | **C** |
| `5.14.5` | Interrupts: GATE CSE 2001 \| Question: 1.12 | **C** |
| `5.14.6` | Interrupts: GATE CSE 2011 \| Question: 11 | **D** |
| `5.15.1` | Least Recently Used: GATE CSE 2023 \| Question: 47 | **4096** |
| `5.16.1` | Linked Allocation: GATE CSE 2025 \| Set 1 \| Question: 41 | **65468:65468** |
| `5.17.1` | Memory Management: GATE CSE 1992 \| Question: 12-b | **3.2** |
| `5.17.2` | Memory Management: GATE CSE 1995 \| Question: 5 | **N/A** |
| `5.17.3` | Memory Management: GATE CSE 1996 \| Question: 2.18 | **B** |
| `5.17.4` | Memory Management: GATE CSE 1998 \| Question: 2.16 | **B** |
| `5.17.5` | Memory Management: GATE CSE 2014 \| Set 2 \| Question: 55 | **10000** |
| `5.17.6` | Memory Management: GATE CSE 2015 \| Set 2 \| Question: 30 | **A** |
| `5.17.7` | Memory Management: GATE CSE 2020 \| Question: 11 | **C** |
| `5.17.8` | Memory Management: GATE IT 2006 \| Question: 56 | **B** |
| `5.17.9` | Memory Management: GATE IT 2007 \| Question: 11 | **B** |
| `5.18.1` | Multilevel Paging: GATE CSE 2025 \| Set 2 \| Question: 48 | **11:11** |
| `5.19.1` | OS Protection: GATE CSE 1999 \| Question: 1.11, UGCNET-Dec2015-II: 44 | **A** |
| `5.19.2` | OS Protection: GATE CSE 2001 \| Question: 1.13 | **C** |
| `5.19.3` | OS Protection: GATE IT 2005 \| Question: 19, UGCNET-June2012-III: 57 | **B** |
| `5.20.1` | Page Replacement: GATE CSE 1993 \| Question: 21 | **N/A** |
| `5.20.2` | Page Replacement: GATE CSE 1994 \| Question: 1.13 | **B** |
| `5.20.3` | Page Replacement: GATE CSE 1994 \| Question: 1.24 | **B** |
| `5.20.4` | Page Replacement: GATE CSE 1995 \| Question: 1.8 | **C** |
| `5.20.5` | Page Replacement: GATE CSE 1995 \| Question: 2.7 | **C** |
| `5.20.6` | Page Replacement: GATE CSE 1997 \| Question: 3.10, ISRO2008-57, ISRO2015-64 | **A** |
| `5.20.7` | Page Replacement: GATE CSE 1997 \| Question: 3.5 | **B** |
| `5.20.8` | Page Replacement: GATE CSE 1997 \| Question: 3.9 | **C** |
| `5.20.9` | Page Replacement: GATE CSE 2001 \| Question: 1.21 | **C** |
| `5.20.10` | Page Replacement: GATE CSE 2002 \| Question: 1.23 | **B** |
| `5.20.11` | Page Replacement: GATE CSE 2004 \| Question: 21, ISRO2007-44 | **A** |
| `5.20.12` | Page Replacement: GATE CSE 2005 \| Question: 22, ISRO2015-36 | **C** |
| `5.20.13` | Page Replacement: GATE CSE 2007 \| Question: 56 | **B** |
| `5.20.14` | Page Replacement: GATE CSE 2007 \| Question: 82 | **A** |
| `5.20.15` | Page Replacement: GATE CSE 2007 \| Question: 83 | **C** |
| `5.20.16` | Page Replacement: GATE CSE 2009 \| Question: 9, ISRO2016-52 | **A** |
| `5.20.17` | Page Replacement: GATE CSE 2010 \| Question: 24 | **A** |
| `5.20.18` | Page Replacement: GATE CSE 2012 \| Question: 42 | **B** |
| `5.20.19` | Page Replacement: GATE CSE 2014 \| Set 1 \| Question: 33 | **7** |
| `5.20.20` | Page Replacement: GATE CSE 2014 \| Set 2 \| Question: 33 | **D** |
| `5.20.21` | Page Replacement: GATE CSE 2014 \| Set 3 \| Question: 20 | **6** |
| `5.20.22` | Page Replacement: GATE CSE 2015 \| Set 1 \| Question: 47 | **A** |
| `5.20.23` | Page Replacement: GATE CSE 2016 \| Set 1 \| Question: 49 | **1** |
| `5.20.24` | Page Replacement: GATE CSE 2016 \| Set 2 \| Question: 20 | **D** |
| `5.20.25` | Page Replacement: GATE CSE 2017 \| Set 1 \| Question: 40 | **B** |
| `5.20.26` | Page Replacement: GATE CSE 2021 \| Set 1 \| Question: 11 | **A;C** |
| `5.20.27` | Page Replacement: GATE CSE 2021 \| Set 2 \| Question: 48 | **4108** |
| `5.20.28` | Page Replacement: GATE CSE 2025 \| Set 1 \| Question: 44 | **6:6** |
| `5.20.29` | Page Replacement: GATE IT 2007 \| Question: 12 | **C** |
| `5.20.30` | Page Replacement: GATE IT 2007 \| Question: 58 | **A** |
| `5.20.31` | Page Replacement: GATE IT 2008 \| Question: 41 | **B** |
| `5.21.1` | Precedence Graph: GATE CSE 1989 \| Question: 11b | **N/A** |
| `5.21.2` | Precedence Graph: GATE CSE 1991 \| Question: 01-xii | **N/A** |
| `5.21.3` | Precedence Graph: GATE CSE 1992 \| Question: 12-a | **N/A** |
| `5.22.1` | Process: GATE CSE 1996 \| Question: 1.18 | **B** |
| `5.22.2` | Process: GATE CSE 2001 \| Question: 2.20 | **C** |
| `5.22.3` | Process: GATE CSE 2002 \| Question: 2.21 | **B** |
| `5.22.4` | Process: GATE CSE 2023 \| Question: 12 | **B;C;D** |
| `5.22.5` | Process: GATE IT 2006 \| Question: 13 | **B** |
| `5.23.1` | Process Scheduling: GATE CSE 1988 \| Question: 2xa | **N/A** |
| `5.23.2` | Process Scheduling: GATE CSE 1988 \| Question: 2xb | **N/A** |
| `5.23.3` | Process Scheduling: GATE CSE 1990 \| Question: 1-vi | **N/A** |
| `5.23.4` | Process Scheduling: GATE CSE 1993 \| Question: 7.10 | **C** |
| `5.23.5` | Process Scheduling: GATE CSE 1995 \| Question: 1.15 | **B** |
| `5.23.6` | Process Scheduling: GATE CSE 1995 \| Question: 2.6 | **A** |
| `5.23.7` | Process Scheduling: GATE CSE 1996 \| Question: 2.20, ISRO2008-15 | **D** |
| `5.23.8` | Process Scheduling: GATE CSE 1998 \| Question: 2.17, UGCNET-Dec2012-III: 43 | **A** |
| `5.23.9` | Process Scheduling: GATE CSE 1998 \| Question: 24 | **N/A** |
| `5.23.10` | Process Scheduling: GATE CSE 1998 \| Question: 7-b | **19** |
| `5.23.11` | Process Scheduling: GATE CSE 2002 \| Question: 1.22 | **B** |
| `5.23.12` | Process Scheduling: GATE CSE 2003 \| Question: 77 | **D** |
| `5.23.13` | Process Scheduling: GATE CSE 2004 \| Question: 46 | **A** |
| `5.23.14` | Process Scheduling: GATE CSE 2006 \| Question: 06, ISRO2009-14 | **B** |
| `5.23.15` | Process Scheduling: GATE CSE 2006 \| Question: 64 | **A** |
| `5.23.16` | Process Scheduling: GATE CSE 2006 \| Question: 65 | **B** |
| `5.23.17` | Process Scheduling: GATE CSE 2007 \| Question: 16 | **A** |
| `5.23.18` | Process Scheduling: GATE CSE 2007 \| Question: 55 | **B** |
| `5.23.19` | Process Scheduling: GATE CSE 2009 \| Question: 32 | **C** |
| `5.23.20` | Process Scheduling: GATE CSE 2010 \| Question: 25 | **D** |
| `5.23.21` | Process Scheduling: GATE CSE 2011 \| Question: 35 | **A** |
| `5.23.22` | Process Scheduling: GATE CSE 2012 \| Question: 31 | **C** |
| `5.23.23` | Process Scheduling: GATE CSE 2013 \| Question: 10 | **B** |
| `5.23.24` | Process Scheduling: GATE CSE 2014 \| Set 1 \| Question: 32 | **7.2** |
| `5.23.25` | Process Scheduling: GATE CSE 2014 \| Set 2 \| Question: 32 | **1000** |
| `5.23.26` | Process Scheduling: GATE CSE 2014 \| Set 3 \| Question: 32 | **5.5** |
| `5.23.27` | Process Scheduling: GATE CSE 2015 \| Set 1 \| Question: 46 | **12** |
| `5.23.28` | Process Scheduling: GATE CSE 2015 \| Set 3 \| Question: 1 | **D** |
| `5.23.29` | Process Scheduling: GATE CSE 2015 \| Set 3 \| Question: 34 | **C** |
| `5.23.30` | Process Scheduling: GATE CSE 2016 \| Set 1 \| Question: 20 | **A** |
| `5.23.31` | Process Scheduling: GATE CSE 2016 \| Set 2 \| Question: 47 | **8.25** |
| `5.23.32` | Process Scheduling: GATE CSE 2017 \| Set 1 \| Question: 24 | **3** |
| `5.23.33` | Process Scheduling: GATE CSE 2017 \| Set 2 \| Question: 51 | **29** |
| `5.23.34` | Process Scheduling: GATE CSE 2019 \| Question: 41 | **2** |
| `5.23.35` | Process Scheduling: GATE CSE 2020 \| Question: 12 | **C** |
| `5.23.36` | Process Scheduling: GATE CSE 2020 \| Question: 50 | **5.25:5.26** |
| `5.23.37` | Process Scheduling: GATE CSE 2021 \| Set 1 \| Question: 25 | **12** |
| `5.23.38` | Process Scheduling: GATE CSE 2021 \| Set 2 \| Question: 14 | **A;C;D** |
| `5.23.39` | Process Scheduling: GATE CSE 2023 \| Question: 17 | **C;D** |
| `5.23.40` | Process Scheduling: GATE CSE 2024 \| Set 1 \| Question: 15 | **B;C** |
| `5.23.41` | Process Scheduling: GATE CSE 2024 \| Set 2 \| Question: 27 | **B** |
| `5.23.42` | Process Scheduling: GATE CSE 2025 \| Set 1 \| Question: 28 | **A** |
| `5.23.43` | Process Scheduling: GATE CSE 2026 \| Set 1 \| Question: 54 | **9.5** |
| `5.23.44` | Process Scheduling: GATE CSE 2026 \| Set 2 \| Question: 13 | **B** |
| `5.23.45` | Process Scheduling: GATE IT 2005 \| Question: 60 | **D** |
| `5.23.46` | Process Scheduling: GATE IT 2006 \| Question: 12 | **D** |
| `5.23.47` | Process Scheduling: GATE IT 2006 \| Question: 54 | **B** |
| `5.23.48` | Process Scheduling: GATE IT 2007 \| Question: 26 | **D** |
| `5.23.49` | Process Scheduling: GATE IT 2008 \| Question: 55 | **C** |
| `5.24.1` | Process Synchronization: GATE CSE 1987 \| Question: 1-xvi | **D** |
| `5.24.2` | Process Synchronization: GATE CSE 1987 \| Question: 8a | **N/A** |
| `5.24.3` | Process Synchronization: GATE CSE 1988 \| Question: 10iib | **N/A** |
| `5.24.4` | Process Synchronization: GATE CSE 1990 \| Question: 2-iii | **N/A** |
| `5.24.5` | Process Synchronization: GATE CSE 1991 \| Question: 11,a | **N/A** |
| `5.24.6` | Process Synchronization: GATE CSE 1991 \| Question: 11,b | **N/A** |
| `5.24.7` | Process Synchronization: GATE CSE 1993 \| Question: 22 | **N/A** |
| `5.24.8` | Process Synchronization: GATE CSE 1994 \| Question: 27 | **N/A** |
| `5.24.9` | Process Synchronization: GATE CSE 1995 \| Question: 19 | **N/A** |
| `5.24.10` | Process Synchronization: GATE CSE 1996 \| Question: 1.19, ISRO2008-61 | **C** |
| `5.24.11` | Process Synchronization: GATE CSE 1996 \| Question: 2.19 | **C** |
| `5.24.12` | Process Synchronization: GATE CSE 1996 \| Question: 21 | **N/A** |
| `5.24.13` | Process Synchronization: GATE CSE 1997 \| Question: 6.8 | **D** |
| `5.24.14` | Process Synchronization: GATE CSE 1997 \| Question: 73 | **N/A** |
| `5.24.15` | Process Synchronization: GATE CSE 1998 \| Question: 1.30 | **B** |
| `5.24.16` | Process Synchronization: GATE CSE 1999 \| Question: 20-a | **N/A** |
| `5.24.17` | Process Synchronization: GATE CSE 1999 \| Question: 20-b | **N/A** |
| `5.24.18` | Process Synchronization: GATE CSE 2000 \| Question: 1.21 | **B** |
| `5.24.19` | Process Synchronization: GATE CSE 2000 \| Question: 20 | **N/A** |
| `5.24.20` | Process Synchronization: GATE CSE 2001 \| Question: 2.22 | **B** |
| `5.24.21` | Process Synchronization: GATE CSE 2002 \| Question: 18-a | **N/A** |
| `5.24.22` | Process Synchronization: GATE CSE 2002 \| Question: 18-b | **N/A** |
| `5.24.23` | Process Synchronization: GATE CSE 2002 \| Question: 20 | **N/A** |
| `5.24.24` | Process Synchronization: GATE CSE 2003 \| Question: 80 | **B** |
| `5.24.25` | Process Synchronization: GATE CSE 2003 \| Question: 81 | **C** |
| `5.24.26` | Process Synchronization: GATE CSE 2004 \| Question: 48 | **D** |
| `5.24.27` | Process Synchronization: GATE CSE 2006 \| Question: 61 | **A** |
| `5.24.28` | Process Synchronization: GATE CSE 2006 \| Question: 78 | **B** |
| `5.24.29` | Process Synchronization: GATE CSE 2006 \| Question: 79 | **B** |
| `5.24.30` | Process Synchronization: GATE CSE 2007 \| Question: 58 | **D** |
| `5.24.31` | Process Synchronization: GATE CSE 2009 \| Question: 33 | **A** |
| `5.24.32` | Process Synchronization: GATE CSE 2010 \| Question: 23 | **A** |
| `5.24.33` | Process Synchronization: GATE CSE 2010 \| Question: 45 | **A** |
| `5.24.34` | Process Synchronization: GATE CSE 2012 \| Question: 32 | **B** |
| `5.24.35` | Process Synchronization: GATE CSE 2013 \| Question: 34 | **D** |
| `5.24.36` | Process Synchronization: GATE CSE 2013 \| Question: 39 | **C** |
| `5.24.37` | Process Synchronization: GATE CSE 2014 \| Set 2 \| Question: 31 | **C** |
| `5.24.38` | Process Synchronization: GATE CSE 2015 \| Set 1 \| Question: 9 | **3** |
| `5.24.39` | Process Synchronization: GATE CSE 2015 \| Set 3 \| Question: 10 | **A** |
| `5.24.40` | Process Synchronization: GATE CSE 2016 \| Set 1 \| Question: 50 | **A** |
| `5.24.41` | Process Synchronization: GATE CSE 2016 \| Set 2 \| Question: 48 | **C** |
| `5.24.42` | Process Synchronization: GATE CSE 2017 \| Set 1 \| Question: 27 | **D** |
| `5.24.43` | Process Synchronization: GATE CSE 2018 \| Question: 40 | **C** |
| `5.24.44` | Process Synchronization: GATE CSE 2019 \| Question: 23 | **80** |
| `5.24.45` | Process Synchronization: GATE CSE 2024 \| Set 2 \| Question: 36 | **B;C** |
| `5.24.46` | Process Synchronization: GATE IT 2004 \| Question: 65 | **D** |
| `5.24.47` | Process Synchronization: GATE IT 2005 \| Question: 41 | **A** |
| `5.24.48` | Process Synchronization: GATE IT 2005 \| Question: 42 | **B** |
| `5.24.49` | Process Synchronization: GATE IT 2006 \| Question: 55 | **A** |
| `5.24.50` | Process Synchronization: GATE IT 2007 \| Question: 10 | **C** |
| `5.24.51` | Process Synchronization: GATE IT 2007 \| Question: 56 | **C** |
| `5.24.52` | Process Synchronization: GATE IT 2008 \| Question: 53 | **D** |
| `5.25.1` | Resource Allocation: GATE CSE 1988 \| Question: 11 | **N/A** |
| `5.25.2` | Resource Allocation: GATE CSE 1989 \| Question: 11a | **N/A** |
| `5.25.3` | Resource Allocation: GATE CSE 1992 \| Question: 02-xi | **A** |
| `5.25.4` | Resource Allocation: GATE CSE 1993 \| Question: 7.9, UGCNET-Dec2012-III: 41 | **D;E** |
| `5.25.5` | Resource Allocation: GATE CSE 1994 \| Question: 28 | **N/A** |
| `5.25.6` | Resource Allocation: GATE CSE 1996 \| Question: 22 | **N/A** |
| `5.25.7` | Resource Allocation: GATE CSE 1997 \| Question: 6.7 | **C** |
| `5.25.8` | Resource Allocation: GATE CSE 1997 \| Question: 75 | **N/A** |
| `5.25.9` | Resource Allocation: GATE CSE 1998 \| Question: 1.32 | **B** |
| `5.25.10` | Resource Allocation: GATE CSE 2000 \| Question: 2.23 | **C** |
| `5.25.11` | Resource Allocation: GATE CSE 2001 \| Question: 19 | **N/A** |
| `5.25.12` | Resource Allocation: GATE CSE 2005 \| Question: 71 | **C** |
| `5.25.13` | Resource Allocation: GATE CSE 2006 \| Question: 66 | **B** |
| `5.25.14` | Resource Allocation: GATE CSE 2007 \| Question: 57 | **C** |
| `5.25.15` | Resource Allocation: GATE CSE 2008 \| Question: 65 | **A** |
| `5.25.16` | Resource Allocation: GATE CSE 2009 \| Question: 30 | **A** |
| `5.25.17` | Resource Allocation: GATE CSE 2010 \| Question: 46 | **B** |
| `5.25.18` | Resource Allocation: GATE CSE 2013 \| Question: 16 | **B** |
| `5.25.19` | Resource Allocation: GATE CSE 2014 \| Set 1 \| Question: 31 | **B** |
| `5.25.20` | Resource Allocation: GATE CSE 2014 \| Set 3 \| Question: 31 | **7** |
| `5.25.21` | Resource Allocation: GATE CSE 2015 \| Set 2 \| Question: 23 | **D** |
| `5.25.22` | Resource Allocation: GATE CSE 2015 \| Set 3 \| Question: 52 | **D** |
| `5.25.23` | Resource Allocation: GATE CSE 2017 \| Set 2 \| Question: 33 | **B** |
| `5.25.24` | Resource Allocation: GATE CSE 2019 \| Question: 39 | **A** |
| `5.25.25` | Resource Allocation: GATE CSE 2022 \| Question: 16 | **A;D** |
| `5.25.26` | Resource Allocation: GATE IT 2005 \| Question: 62 | **C** |
| `5.25.27` | Resource Allocation: GATE IT 2008 \| Question: 54 | **B** |
| `5.26.1` | Resource Allocation Graph (1) | **C;D** |
| `5.27.1` | Round Robin Scheduling: GATE CSE 2022 \| Question: 32 | **D** |
| `5.28.1` | Semaphore: GATE CSE 1990 \| Question: 1-vii | **N/A** |
| `5.28.2` | Semaphore: GATE CSE 1992 \| Question: 02,x, ISRO2015-35 | **B** |
| `5.28.3` | Semaphore: GATE CSE 1998 \| Question: 1.31 | **B** |
| `5.28.4` | Semaphore: GATE CSE 2008 \| Question: 63 | **C** |
| `5.28.5` | Semaphore: GATE CSE 2016 \| Set 2 \| Question: 49 | **7** |
| `5.28.6` | Semaphore: GATE CSE 2020 \| Question: 34 | **A** |
| `5.28.7` | Semaphore: GATE CSE 2021 \| Set 1 \| Question: 46 | **A;B;D** |
| `5.28.8` | Semaphore: GATE CSE 2022 \| Question: 9 | **C** |
| `5.28.9` | Semaphore: GATE CSE 2023 \| Question: 28 | **C** |
| `5.28.10` | Semaphore: GATE CSE 2026 \| Set 2 \| Question: 41 | **A;B;C** |
| `5.28.11` | Semaphore: GATE IT 2006 \| Question: 57 | **D** |
| `5.29.1` | Srtf: GATE CSE 2025 \| Set 2 \| Question: 16 | **D** |
| `5.30.1` | System Calls: GATE CSE 2021 \| Set 1 \| Question: 14 | **A;C** |
| `5.31.1` | Threads: GATE CSE 2004 \| Question: 11 | **A** |
| `5.31.2` | Threads: GATE CSE 2007 \| Question: 17 | **D** |
| `5.31.3` | Threads: GATE CSE 2011 \| Question: 16, UGCNET-June2013-III: 65 | **C** |
| `5.31.4` | Threads: GATE CSE 2014 \| Set 1 \| Question: 20 | **D** |
| `5.31.5` | Threads: GATE CSE 2017 \| Set 1 \| Question: 18 | **D** |
| `5.31.6` | Threads: GATE CSE 2017 \| Set 2 \| Question: 07 | **B** |
| `5.31.7` | Threads: GATE CSE 2021 \| Set 2 \| Question: 42 | **A;D** |
| `5.31.8` | Threads: GATE CSE 2024 \| Set 1 \| Question: 14 | **D** |
| `5.31.9` | Threads: GATE CSE 2024 \| Set 1 \| Question: 30 | **A** |
| `5.31.10` | Threads: GATE IT 2004 \| Question: 14 | **A** |
| `5.32.1` | Translation Lookaside Buffer: GATE CSE 2022 \| Question: 28 | **C** |
| `5.32.2` | Translation Lookaside Buffer: GATE CSE 2026 \| Set 2 \| Question: 44 | **1536** |
| `5.33.1` | Virtual Memory: GATE CSE 1989 \| Question: 2-iv | **N/A** |
| `5.33.2` | Virtual Memory: GATE CSE 1990 \| Question: 1-v | **N/A** |
| `5.33.3` | Virtual Memory: GATE CSE 1990 \| Question: 7-b | **99.99** |
| `5.33.4` | Virtual Memory: GATE CSE 1991 \| Question: 03-xi | **B;C;E** |
| `5.33.5` | Virtual Memory: GATE CSE 1994 \| Question: 1.21 | **A** |
| `5.33.6` | Virtual Memory: GATE CSE 1995 \| Question: 1.7 | **A** |
| `5.33.7` | Virtual Memory: GATE CSE 1995 \| Question: 2.16 | **C** |
| `5.33.8` | Virtual Memory: GATE CSE 1996 \| Question: 7 | **N/A** |
| `5.33.9` | Virtual Memory: GATE CSE 1998 \| Question: 2.18, UGCNET-June2012-III: 48 | **A** |
| `5.33.10` | Virtual Memory: GATE CSE 1999 \| Question: 19 | **N/A** |
| `5.33.11` | Virtual Memory: GATE CSE 1999 \| Question: 2.10 | **A;C** |
| `5.33.12` | Virtual Memory: GATE CSE 1999 \| Question: 2.11 | **B;D** |
| `5.33.13` | Virtual Memory: GATE CSE 2000 \| Question: 2.22 | **D** |
| `5.33.14` | Virtual Memory: GATE CSE 2001 \| Question: 1.20 | **B** |
| `5.33.15` | Virtual Memory: GATE CSE 2001 \| Question: 1.8 | **D** |
| `5.33.16` | Virtual Memory: GATE CSE 2001 \| Question: 2.21 | **C** |
| `5.33.17` | Virtual Memory: GATE CSE 2002 \| Question: 19 | **N/A** |
| `5.33.18` | Virtual Memory: GATE CSE 2003 \| Question: 26 | **C** |
| `5.33.19` | Virtual Memory: GATE CSE 2003 \| Question: 78 | **D** |
| `5.33.20` | Virtual Memory: GATE CSE 2003 \| Question: 79 | **C** |
| `5.33.21` | Virtual Memory: GATE CSE 2006 \| Question: 62, ISRO2016-50 | **C** |
| `5.33.22` | Virtual Memory: GATE CSE 2006 \| Question: 63, UGCNET-June2012-III: 45 | **C** |
| `5.33.23` | Virtual Memory: GATE CSE 2008 \| Question: 67 | **D** |
| `5.33.24` | Virtual Memory: GATE CSE 2009 \| Question: 10 | **B** |
| `5.33.25` | Virtual Memory: GATE CSE 2009 \| Question: 34 | **B** |
| `5.33.26` | Virtual Memory: GATE CSE 2011 \| Question: 20, UGCNET-June2013-II: 48 | **B** |
| `5.33.27` | Virtual Memory: GATE CSE 2013 \| Question: 52 | **C** |
| `5.33.28` | Virtual Memory: GATE CSE 2013 \| Question: 53 | **C** |
| `5.33.29` | Virtual Memory: GATE CSE 2014 \| Set 3 \| Question: 33 | **122** |
| `5.33.30` | Virtual Memory: GATE CSE 2015 \| Set 1 \| Question: 12 | **4** |
| `5.33.31` | Virtual Memory: GATE CSE 2015 \| Set 2 \| Question: 25 | **22** |
| `5.33.32` | Virtual Memory: GATE CSE 2015 \| Set 2 \| Question: 47 | **36** |
| `5.33.33` | Virtual Memory: GATE CSE 2016 \| Set 1 \| Question: 47 | **384** |
| `5.33.34` | Virtual Memory: GATE CSE 2018 \| Question: 10 | **B** |
| `5.33.35` | Virtual Memory: GATE CSE 2019 \| Question: 33 | **B** |
| `5.33.36` | Virtual Memory: GATE CSE 2020 \| Question: 53 | **155:156** |
| `5.33.37` | Virtual Memory: GATE CSE 2023 \| Question: 48 | **5** |
| `5.33.38` | Virtual Memory: GATE CSE 2024 \| Set 1 \| Question: 52 | **6596** |
| `5.33.39` | Virtual Memory: GATE CSE 2024 \| Set 2 \| Question: 14 | **B;C;D** |
| `5.33.40` | Virtual Memory: GATE CSE 2024 \| Set 2 \| Question: 54 | **1028** |
| `5.33.41` | Virtual Memory: GATE IT 2004 \| Question: 66 | **D** |
| `5.33.42` | Virtual Memory: GATE IT 2008 \| Question: 16 | **C** |
| `5.33.43` | Virtual Memory: GATE IT 2008 \| Question: 56 | **D** |

