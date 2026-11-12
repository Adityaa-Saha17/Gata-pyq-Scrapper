# Volume 3 — Chapter 1: CO & Architecture

- **Source PDF**: [filter1_volume3.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume3.pdf)
- **Total GATE Questions in Chapter**: **251**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **1.2** | Average Memory Access Time | 3 |
| **1.3** | Bit Vector | 1 |
| **1.4** | CISC RISC Architecture | 2 |
| **1.5** | Cache Memory | 69 |
| **1.7** | Control Unit | 1 |
| **1.8** | DMA | 8 |
| **1.10** | Data Dependency | 4 |
| **1.11** | Data Hazards | 1 |
| **1.12** | Data Path | 7 |
| **1.13** | Direct Mapping | 5 |
| **1.14** | Disk | 1 |
| **1.15** | Hazards | 1 |
| **1.16** | IO Handling | 8 |
| **1.17** | Instruction Execution | 7 |
| **1.19** | Instruction Set Architecture | 1 |
| **1.20** | Interrupts | 10 |
| **1.21** | Machine Instruction | 21 |
| **1.22** | Memory Interfacing | 6 |
| **1.23** | Microprogramming | 12 |
| **1.24** | Pipelining | 39 |
| **1.25** | Runtime Environment | 2 |
| **1.26** | Speedup | 6 |
| **1.27** | Stall | 1 |
| **1.28** | Virtual Memory | 3 |


---

## 2. Comprehensive GATE CSE CO & Architecture Reference (Expanded Research & Formulas)

### 2.1 Cache Memory Mapping & Address Bit Breakdown
Let Main Memory size $= 2^m$ bytes, Cache size $= C = S \times k \times B$ bytes, Block/Line size $= B = 2^b$ bytes, Number of cache lines $= N = C / B$, Associativity $= k$-way, Number of sets $= S = N / k = 2^s$:

| Mapping Scheme | Tag Bits | Index / Set Bits | Block Offset Bits | Tag Directory Size (Bits) |
| :--- | :---: | :---: | :---: | :---: |
| **Direct Mapped ($k = 1$)** | $m - n - b$ | $n = \log_2 N$ | $b = \log_2 B$ | $N \times (\text{Tag bits} + \text{Valid} + \text{Dirty})$ |
| **$k$-Way Set Associative** | $m - s - b$ | $s = \log_2(N / k)$ | $b = \log_2 B$ | $N \times (\text{Tag bits} + \text{Valid} + \text{Dirty})$ |
| **Fully Associative ($S = 1$)** | $m - b$ | $0$ | $b = \log_2 B$ | $N \times (\text{Tag bits} + \text{Valid} + \text{Dirty})$ |

- **Comparators Required for $k$-Way Set Associative Cache**: **$k$ comparators**, each of width $=$ **Tag bits**.
- **Average Memory Access Time (AMAT)**:
  - **Simultaneous / Parallel Access**: $\text{AMAT} = H_1 T_1 + (1 - H_1) T_m$
  - **Hierarchical / Serial Access**: $\text{AMAT} = T_1 + (1 - H_1) T_m$ (where $T_m$ is miss penalty / block transfer time).
  - **Write-Through vs Write-Back**:
    - **Write-Through**: Every write updates both cache and main memory; uses **no dirty bit**; often paired with **No-Write Allocate**.
    - **Write-Back**: Writes update only cache and set the **Dirty Bit** ($1$ bit per cache line); modified block is written to memory only upon eviction; paired with **Write Allocate**.

### 2.2 Instruction Pipelining, Speedup, CPI & Hazards
- **Execution Time for $n$ Instructions in a $k$-Stage Pipeline** (clock cycle time $\tau_p = \max(\tau_i) + \tau_{\text{latch}}$):
  $$T_{\text{pipe}} = \big(k + (n - 1) + \text{Total Stall Cycles}\big) \times \tau_p$$
- **Asymptotic Speedup ($n \to \infty$)**:
  $$S = \frac{T_{\text{non-pipe}}}{T_{\text{pipe}}} = \frac{\text{CPI}_{\text{ideal}} \times \tau_{\text{non-pipe}}}{(1 + \text{Stalls per Instruction}) \times \tau_p}$$
  - With ideal $\text{CPI} = 1$: $\text{CPI}_{\text{actual}} = 1 + \sum (\text{Branch/Hazard Frequency} \times \text{Penalty Cycles})$.
- **Pipeline Hazards**:
  1. **Structural Hazard**: Resource conflict (e.g., single unified memory for instruction fetch and data access).
  2. **Data Hazard** (on register $R$ between instruction $i$ followed by $j$):
     - **RAW (Read After Write — True Dependency)**: Solved by **Operand Forwarding (Bypassing)**, except Load-Use hazard which still requires $1$ stall cycle.
     - **WAR (Write After Read — Anti-Dependency)** & **WAW (Write After Write — Output Dependency)**: False (name) dependencies; solved by **Register Renaming** (only occur in out-of-order / variable-latency pipelines).
  3. **Control (Branch) Hazard**: Solved by branch prediction, delayed branching (delay slots), or early branch resolution.

### 2.3 Instruction Formats, Addressing Modes, I/O & DMA
- **Expanding Opcode Technique**:
  - If instruction length is $L$ bits and each address field is $a$ bits: after allocating $m_1$ 2-address instructions, remaining combinations for 1-address instructions $= \big(2^{L - 2a} - m_1\big) \times 2^a$.
- **DMA (Direct Memory Access)**:
  - **Cycle Stealing Mode**: Fraction of CPU time stolen $= \frac{T_{\text{DMA\_cycle}}}{T_{\text{byte\_arrival}}}$.
  - **Burst Mode**: Fraction of time CPU is blocked $= \frac{T_{\text{transfer}}}{T_{\text{prep}} + T_{\text{transfer}}}$.
- **Control Unit — Horizontal vs Vertical Microprogramming**:
  - **Horizontal**: Unencoded control signals (1 bit per control line) $\implies$ long control word, high parallelism, no decoder delay.
  - **Vertical**: Encoded control fields ($k$ mutually exclusive signals encoded into $\lceil \log_2(k+1) \rceil$ bits; $+1$ for `No-Op` if needed) $\implies$ short control word, requires external decoders.

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

1 CO & Architecture (251)
Machine instructions and Addressing modes. ALU, data‐path and control unit. Instruction pipelining. Pipeline
hazards, Memory hierarchy: cache, main memory and secondary storage; I/O interface (Interrupt and DMA
mode)
Welcome to the "Computer Organization & Architecture" chapter of your GATE Computer Science preparation. This
crucial subject delves into the fundamental design and operational principles of a computer system, from the lowest-
level hardware components to how instructions are executed and data is managed. Understanding COA is vital for any
computer scientist as it provides the bedrock knowledge for designing efficient systems, writing optimized code, and
comprehending the performance implications of software choices. In the GATE CS exam, COA typically carries a
weightage of 8-12 marks, with questions ranging from conceptual understanding of architectural principles (like CISC
vs. RISC, control unit types) to numerical problems involving cache memory, pipelining performance, virtual memory,
and disk access times. Expect a mix of Multiple Choice Questions (MCQs), Multiple Select Questions (MSQs), and
Numerical Answer Type (NAT) questions, often requiring precise calculations and a deep grasp of underlying
mechanisms.
Topic-wise Key Concepts
Addressing Modes
Addressing modes define how the effective address of an operand is calculated. They specify where the operand is
located, whether in a register, memory, or as part of the instruction itself, enabling flexible and efficient memory access.
Important Formulas & Concepts
Direct: Immediate: Operand is part of the instruction. . No memory access for operand.
(address field in instruction). One memory access to fetch operand.
(address field points to memory location containing EA). Two memory accesses (one
Indirect: for EA, one for operand).
Register: Operand is in a specified register. . No memory access.
Register Indirect: (register contains EA). One memory access to fetch operand.
Relative (PC-relative): (offset from Program Counter). Used for branch instructions.
Indexed: . Used for array access.
Base-Register: . Used for relocating programs.
Key Properties & Identities
Trade-offs exist between instruction length, execution speed, and flexibility.
Used to access data, implement control flow, and manage memory.
Common Pitfalls
Confusing direct and indirect addressing, especially regarding the number of memory accesses.
Standard Problem-Solving Techniques
Trace the instruction execution step-by-step to calculate the effective address for given register/memory contents.
Average Memory Access Time (AMAT)
AMAT is the average time taken to access memory, considering the presence of a cache and its hit/miss rates. It
quantifies the performance of the memory hierarchy.

*(PDF Page 14)*

Important Formulas & Concepts
For a single-level cache:
where is cache hit time, memory (main memory).
For a two-level cache (L1, L2):
is miss rate, and is the time to fetch data from the next level of
where L2), and is L1 hit time, is L1 miss rate, is main memory access time.
is L2 hit time, is L2 miss rate (local miss rate for
Key Properties & Identities
Lower AMAT indicates better memory system performance.
Affected by cache hit rate, miss penalty, and cache access times.
Common Pitfalls
Forgetting to add the hit time to the miss penalty when calculating total miss time.
Incorrectly applying local vs. global miss rates for multi-level caches.
Standard Problem-Solving Techniques
Draw the memory hierarchy and clearly identify access times and miss rates for each level.
Bit Vector
A bit vector (or bit array) is a data structure that efficiently stores a sequence of bits. Each bit typically represents a
boolean flag or the presence/absence of an element in a set.
Important Formulas & Concepts
Storage: bits require bytes of storage.
Bitwise operations: AND, OR, XOR, NOT, SHIFT for efficient manipulation.
Key Properties & Identities
Space-efficient for large sets of boolean flags.
Fast bitwise operations for checking, setting, or clearing flags.
Common Pitfalls
Misinterpreting bit positions or the effect of bitwise operations.
Standard Problem-Solving Techniques
Use bit masks to isolate or modify specific bits.
CISC RISC Architecture
CISC (Complex Instruction Set Computer) and RISC (Reduced Instruction Set Computer) are two contrasting
philosophies for designing instruction sets. They represent different approaches to instruction complexity and hardware
implementation.
Important Formulas & Concepts
CISC Characteristics:

*(PDF Page 15)*

Many complex instructions, often performing multiple operations (e.g., memory access and arithmetic).
Variable instruction length.
Microprogrammed control unit.
Fewer general-purpose registers, more memory-to-memory operations.
Complex addressing modes.
RISC Characteristics:
Few, simple, fixed-length instructions, typically one operation per instruction.
Hardwired control unit.
Many general-purpose registers, load/store architecture (only LOAD/STORE access memory).
Simple addressing modes.
Optimized for pipelining.
Key Properties & Identities
RISC generally achieves higher CPI (Cycles Per Instruction) but lower clock cycle time due to simpler instructions,
leading to better performance in many cases.
CISC aims for fewer instructions per program but higher CPI.
Common Pitfalls
Assuming one architecture is universally superior; their suitability depends on the application and compiler
technology.
Standard Problem-Solving Techniques
Compare and contrast features to identify the type of architecture described in a scenario.
Cache Memory
Cache memory is a small, fast memory component that stores copies of data from frequently used main memory
locations. Its purpose is to reduce the average time to access data, exploiting the principle of locality.
Important Formulas & Concepts
Address Breakdown: For a memory address of bits, a cache with bytes per block, and cache lines (or
sets):
Block Offset bits:
Number of Blocks in Main Memory:
Number of Cache Lines:
Direct Mapping:
Index bits:
Tag bits:
Set-Associative Mapping (S-way):
Number of Sets:
Index bits:
Tag bits:
Fully Associative Mapping:
No Index bits.
Tag bits:
Any block can go into any cache line.
Hit Rate ( ):
Miss Rate ( ):
Key Properties & Identities
Exploits temporal and spatial locality of reference.
Mapping techniques (Direct, Set-Associative, Fully Associative) determine where a block can be placed.
Write policies (Write-Through, Write-Back) determine when data is written to main memory.

*(PDF Page 16)*

Replacement policies (LRU, FIFO, LFU, Random) determine which block to evict on a miss.
Common Pitfalls
Incorrectly calculating the number of bits for Tag, Index, and Offset.
Confusing the total cache size with the number of cache lines.
Standard Problem-Solving Techniques
Draw the cache structure and trace memory accesses to determine hits/misses and cache contents.
Conflict Misses
Conflict misses occur in direct-mapped or set-associative caches when multiple memory blocks map to the same cache
line or set, and these blocks are actively used, causing them to evict each other even if other cache lines are empty.
Important Formulas & Concepts
These are a type of "capacity miss" specifically due to the mapping function.
Increasing associativity reduces conflict misses.
Key Properties & Identities
Occur when the cache is not full but the required block is evicted due to mapping constraints.
Distinguished from compulsory (first-time access) and capacity (cache too small) misses.
Common Pitfalls
Mistaking a conflict miss for a capacity miss or a compulsory miss.
Standard Problem-Solving Techniques
Analyze the memory access pattern and the cache mapping scheme to identify if multiple active blocks map to the
same location.
Control Unit
The control unit is the part of the CPU that directs the operation of the processor. It interprets instructions and
generates control signals to coordinate the activities of other components, such as the ALU, registers, and memory.
Important Formulas & Concepts
Hardwired Control: Implemented using combinational logic gates.
Faster execution.
Complex to design and modify for large instruction sets.
Used in RISC processors.
Microprogrammed Control: Implemented using a sequence of microinstructions stored in a control memory.
More flexible and easier to design/modify for complex instruction sets.
Slower execution due to memory access for microinstructions.
Used in CISC processors.
Key Properties & Identities
Determines the sequence of micro-operations for each machine instruction.
Generates timing and control signals for the entire system.
Common Pitfalls
Not understanding the trade-offs between hardwired and microprogrammed control in terms of speed, flexibility, and
design complexity.

*(PDF Page 17)*

Standard Problem-Solving Techniques
Relate the control unit type to the characteristics of CISC/RISC architectures.
DMA (Direct Memory Access)
DMA is a hardware feature that allows I/O devices to transfer data directly to and from main memory without involving
the CPU. This significantly reduces CPU overhead for data transfers, improving system performance.
Important Formulas & Concepts
DMA controller manages the data transfer.
Cycle Stealing: DMA controller takes control of the bus for one or more memory cycles to transfer data.
Burst Mode: DMA controller takes control of the bus and transfers an entire block of data before releasing the bus.
Key Properties & Identities
Frees the CPU to perform other tasks during I/O operations.
Requires a DMA controller chip.
Common Pitfalls
Misunderstanding that DMA completely bypasses the CPU; the CPU initiates and configures the DMA transfer.
Standard Problem-Solving Techniques
Analyze scenarios to determine when DMA is most beneficial compared to programmed I/O or interrupt-driven I/O.
DRAM (Dynamic Random Access Memory)
DRAM is the most common type of main memory used in computers. It stores each bit of data in a separate capacitor
within an integrated circuit, requiring periodic refreshing to maintain the charge and thus the data.
Important Formulas & Concepts
Data stored as charge in capacitors.
Requires refresh cycles to prevent data loss.
Key Properties & Identities
Volatile (data is lost when power is removed).
Higher density and lower cost per bit compared to SRAM.
Slower access times than SRAM due to refresh cycles and capacitor charging/discharging.
Common Pitfalls
Confusing DRAM characteristics with SRAM (Static RAM), which uses latches and does not require refreshing.
Standard Problem-Solving Techniques
Compare and contrast DRAM with SRAM based on cost, speed, density, and power consumption.
Data Dependency
A data dependency exists between two instructions when the second instruction requires data produced by the first
instruction, or when they both access the same memory location, potentially leading to incorrect results if executed out
of order.
Important Formulas & Concepts

*(PDF Page 18)*

RAW (Read After Write) / True Dependency: Instruction . This is the most common and critical dependency.
WAR (Write After Read) / Anti-dependency: Instruction from it. . Can be resolved by renaming.
WAW (Write After Write) / Output Dependency: Instruction writes to it. . Can be resolved by renaming.
tries to read a source before instruction writes to it.
tries to write to a destination before instruction reads
tries to write to a destination before instruction
Key Properties & Identities
RAW dependencies are true data dependencies and must be preserved.
WAR and WAW are name dependencies and can be eliminated by register renaming.
Common Pitfalls
Incorrectly identifying the type of dependency or missing a dependency.
Standard Problem-Solving Techniques
Analyze the read/write sets of instructions to identify dependencies.
Data Hazards
Data hazards occur in pipelined processors when an instruction attempts to access data before a preceding instruction
has made that data available. These hazards can lead to incorrect program execution if not handled.
Important Formulas & Concepts
Caused by RAW, WAR, and WAW dependencies.
Solutions:
Stalling (Bubbles/NOPs): Insert NOP instructions to delay the dependent instruction.
Forwarding (Bypassing): Route the result of an instruction directly from an internal pipeline register to the input
of a subsequent instruction's functional unit, bypassing the register file.
Compiler Scheduling: Reorder instructions at compile time to avoid hazards.
Key Properties & Identities
Increase the CPI (Cycles Per Instruction) of a pipeline, reducing ideal speedup.
Forwarding is the most common hardware solution to reduce stalls due to RAW hazards.
Common Pitfalls
Calculating the number of stalls incorrectly, especially when forwarding is present.
Not identifying all data dependencies in a given instruction sequence.
Standard Problem-Solving Techniques
Draw pipeline diagrams to visualize instruction flow and identify where stalls or forwarding are needed.
Data Path
The data path of a CPU consists of the functional units (like the ALU, registers, and multiplexers) and the buses that
connect them, through which data flows during instruction execution. It performs the actual data processing operations.
Important Formulas & Concepts
Key components: Program Counter (PC), Instruction Register (IR), Memory Address Register (MAR), Memory Data
Register (MDR), General Purpose Registers (GPRs), Arithmetic Logic Unit (ALU).
Key Properties & Identities

*(PDF Page 19)*

The data path is controlled by signals generated by the control unit.
Its design impacts the clock cycle time and the number of cycles per instruction.
Common Pitfalls
Not understanding how data moves between components for different instruction types.
Standard Problem-Solving Techniques
Trace the flow of data for a specific instruction (e.g., LOAD, ADD) through the datapath components.
Direct Mapping
Direct mapping is a cache organization technique where each block from main memory can only be placed into one
specific line in the cache. This mapping is determined by a simple modular arithmetic function of the memory block
address.
Important Formulas & Concepts
Cache Line Index:
Address Breakdown: A memory address is divided into three fields: Tag, Index, and Block Offset.
Block Offset bits:
Index bits:
Tag bits:
Key Properties & Identities
Simplest to implement and fastest for cache lookup.
Suffers from high conflict misses if frequently accessed blocks map to the same cache line.
Common Pitfalls
Incorrectly calculating the number of bits for the Tag, Index, or Block Offset fields.
Standard Problem-Solving Techniques
Given memory and cache parameters, determine the address breakdown and trace memory accesses to identify
hits/misses.
Dirty Bit
A dirty bit (or modified bit) is a flag associated with a cache line or a virtual memory page table entry. It indicates
whether the corresponding data block in the cache/page has been modified since it was loaded from the next lower level
of memory (main memory/disk).
Important Formulas & Concepts
Set to '1' when data in the cache line or page is written to.
Set to '0' when the data is clean (matches the lower level memory).
Key Properties & Identities
Crucial for write-back cache policies: if the dirty bit is set, the block must be written back to main memory upon
eviction.
Used in virtual memory page replacement algorithms to avoid unnecessary writes to disk.
Common Pitfalls
Misunderstanding its role in write-through caches (where it's not typically needed) versus write-back caches.

*(PDF Page 20)*

Standard Problem-Solving Techniques
Analyze cache write operations and page replacement scenarios to determine when the dirty bit is set or checked.
Disk
A disk (hard disk drive) is a non-volatile secondary storage device that stores data magnetically on rotating platters. It is
characterized by its large capacity and persistence, but significantly slower access times compared to RAM.
Important Formulas & Concepts
Disk Access Time:
Seek Time: Time taken for the read/write head to move to the correct track. (Often given as average or calculated
based on number of tracks).
Rotational Latency: Time taken for the desired sector to rotate under the read/write head.
(where RPM is revolutions per minute).
Transfer Time: Time taken to transfer the actual data once the head is positioned.
or .
Key Properties & Identities
Non-volatile storage.
Mechanical components make it orders of magnitude slower than electronic memory.
Common Pitfalls
Incorrectly calculating average rotational latency (using Mixing units (e.g., milliseconds and seconds).
of a full rotation).
Standard Problem-Solving Techniques
Break down the access time calculation into its three components and calculate each separately.
Hazards
Hazards are situations in pipelined processors that prevent the next instruction in the instruction stream from executing
in its designated clock cycle. They reduce the ideal speedup of a pipeline.
Important Formulas & Concepts
Structural Hazards: Occur when two instructions require the same hardware resource at the same time (e.g.,
single memory port for both instruction fetch and data access).
Data Hazards: Occur when an instruction depends on the result of a previous instruction that has not yet completed
(RAW, WAR, WAW).
Control Hazards (Branch Hazards): Occur when the pipeline makes a wrong guess about the next instruction to
fetch (e.g., after a conditional branch).
Key Properties & Identities
All hazards increase the effective CPI (Cycles Per Instruction) of the pipeline.

*(PDF Page 21)*

Solutions include stalling, forwarding, and branch prediction.
Common Pitfalls
Confusing the different types of hazards or misidentifying the cause of a stall.
Standard Problem-Solving Techniques
Analyze the instruction sequence and pipeline stage usage to identify potential conflicts.
IO Handling
I/O handling refers to the mechanisms by which a CPU communicates and exchanges data with peripheral input/output
devices. Efficient I/O handling is crucial for system performance.
Important Formulas & Concepts
Programmed I/O (Polling): CPU continuously checks the status of an I/O device.
High CPU overhead, simple to implement.
Interrupt-Driven I/O: I/O device signals the CPU via an interrupt when it needs attention.
Lower CPU overhead than polling, CPU can do other work.
Requires interrupt service routines (ISRs).
Direct Memory Access (DMA): I/O device transfers data directly to/from memory without CPU intervention.
Lowest CPU overhead for large data transfers.
Requires a DMA controller.
Key Properties & Identities
Each method has trade-offs in terms of CPU utilization, response time, and complexity.
Interrupts allow for asynchronous event handling.
Common Pitfalls
Not understanding the CPU's involvement (or lack thereof) in data transfer for each method.
Standard Problem-Solving Techniques
Evaluate scenarios to determine the most suitable I/O handling method based on data volume and CPU availability.
Instruction Execution
Instruction execution is the process by which a CPU carries out a single machine instruction. In a pipelined processor,
this process is broken down into several sequential stages, allowing multiple instructions to be processed concurrently.
Important Formulas & Concepts
Typical 5-stage pipeline:
1. IF (Instruction Fetch): Fetch instruction from memory.
2. ID (Instruction Decode): Decode instruction, read registers.
3. EX (Execute): Perform ALU operation.
4. MEM (Memory Access): Access data memory (load/store).
5. WB (Write Back): Write result back to register file.
Key Properties & Identities
Each stage ideally takes one clock cycle in a pipelined processor.
The slowest stage determines the clock cycle time of the pipeline.
Common Pitfalls

*(PDF Page 22)*

Misunderstanding the specific function of each pipeline stage.
Standard Problem-Solving Techniques
Trace an instruction through each stage of the pipeline to understand its execution flow.
Instruction Format
The instruction format defines the layout of bits within a machine instruction. It specifies how the opcode, operands, and
addressing mode information are encoded, directly impacting the instruction set's flexibility and the CPU's decoding
complexity.
Important Formulas & Concepts
An instruction typically consists of an opcode (operation code) and one or more operand fields.
Operand fields can specify registers, memory addresses, or immediate values.
Fixed-length instruction format: All instructions have the same length. Simplifies fetching and decoding, good for
pipelining (RISC).
Variable-length instruction format: Instructions can have different lengths. Allows for more complex instructions
and addressing modes, but complicates fetching and decoding (CISC).
Key Properties & Identities
The number of bits for the opcode determines the maximum number of unique operations.
The number of bits for operand fields determines the number of registers or the addressable memory range.
Common Pitfalls
Incorrectly calculating the maximum number of opcodes or addressable memory given a fixed instruction length.
Standard Problem-Solving Techniques
Given instruction length and operand requirements, calculate the remaining bits for the opcode or vice-versa.
Instruction Set Architecture (ISA)
The ISA is the abstract model of a computer that is visible to a programmer or compiler writer. It defines the set of
instructions, registers, memory organization, data types, and the I/O model that the hardware supports.
Important Formulas & Concepts
Includes the instruction set, register set, memory addressing modes, and interrupt handling mechanisms.
Forms the interface between software and hardware.
Key Properties & Identities
ISA defines what the processor does, while microarchitecture defines how it does it.
CISC and RISC are two major ISA design philosophies.
Common Pitfalls
Confusing ISA (the specification) with microarchitecture (the implementation).
Standard Problem-Solving Techniques
Understand that ISA is the contract that allows software to run on different hardware implementations of the same
ISA.
Interrupts

*(PDF Page 23)*

An interrupt is a signal to the CPU indicating an event that requires immediate attention, causing the CPU to temporarily
suspend its current task and execute a special routine (Interrupt Service Routine or ISR) to handle the event.
Important Formulas & Concepts
Hardware Interrupts: Generated by I/O devices (e.g., keyboard press, disk completion). Asynchronous.
Software Interrupts (Exceptions/Traps): Generated by program execution (e.g., division by zero, page fault,
system call). Synchronous.
Interrupt Vector Table: A table of addresses for ISRs, indexed by interrupt number.
Key Properties & Identities
Enable efficient I/O handling and error management without constant CPU polling.
Involve saving CPU state, executing ISR, and restoring CPU state.
Common Pitfalls
Misunderstanding the sequence of events during interrupt handling (saving context, jumping to ISR, restoring
context).
Standard Problem-Solving Techniques
Trace the flow of control when an interrupt occurs, considering context saving and ISR execution.
Machine Instruction
A machine instruction is a command or operation that a CPU can directly understand and execute. It is represented in
binary code and forms the lowest-level programming language, specific to a particular processor's Instruction Set
Architecture.
Important Formulas & Concepts
Composed of an opcode and zero or more operands.
Each instruction performs a basic operation (e.g., add, load, store, branch).
Key Properties & Identities
Directly executable by the hardware.
The fundamental unit of computation for the CPU.
Common Pitfalls
Confusing machine instructions (binary) with assembly language instructions (mnemonic representation).
Standard Problem-Solving Techniques
Understand how an assembly instruction translates into its binary machine code equivalent based on the instruction
format.
Memory Interfacing
Memory interfacing is the process of connecting memory devices (RAM, ROM) to the CPU. It involves designing the
necessary address decoding logic, connecting data and address buses, and generating control signals to ensure proper
communication and data transfer.
Important Formulas & Concepts
Address Decoding: Logic gates (decoders, AND gates) used to select the correct memory chip based on the
CPU's address lines.
Chip Select (CS): A control signal that enables a specific memory chip.

*(PDF Page 24)*

Memory Map: The allocation of address ranges to different memory devices.
Key Properties & Identities
Ensures that each memory location has a unique address and that the correct device responds to a CPU request.
Bus width (data and address) must match between CPU and memory.
Common Pitfalls
Incorrectly designing address decoding logic, leading to address conflicts or unused address space.
Standard Problem-Solving Techniques
Given CPU address lines and memory chip sizes, determine the address ranges and design the minimal decoding
logic.
Microprogramming
Microprogramming is a technique for implementing the control unit of a CPU by storing a sequence of microinstructions
in a special control memory. Each machine instruction is executed by a microprogram, which is a sequence of
microinstructions.
Important Formulas & Concepts
Microinstruction: A low-level instruction that controls the individual functional units of the CPU (e.g., enable ALU,
load register).
Control Store (CS): Memory where microprograms are stored.
Key Properties & Identities
Offers flexibility: easier to design complex instruction sets and modify existing ones.
Slower than hardwired control due to the overhead of fetching and decoding microinstructions.
Commonly used in CISC processors.
Common Pitfalls
Confusing microinstructions (internal CPU control) with machine instructions (user-level instructions).
Standard Problem-Solving Techniques
Understand how a machine instruction is broken down into a sequence of micro-operations controlled by
microinstructions.
Pipelining
Pipelining is a technique that allows multiple instructions to be in different stages of execution simultaneously, improving
the throughput of a processor. It does not reduce the execution time of a single instruction but increases the rate at
which instructions complete.
Important Formulas & Concepts
Number of stages:
Number of instructions:
Clock cycle time: (determined by the slowest stage).
Execution time for N instructions (non-pipelined):
Execution time for N instructions (ideal pipelined):
Ideal Speedup ( ) for large N:
Throughput (ideal): instructions per cycle.
CPI (Cycles Per Instruction):

*(PDF Page 25)*

Ideal CPI = 1.
Actual CPI =
.
Key Properties & Identities
Increases instruction throughput, not latency.
Performance is limited by hazards (structural, data, control).
Common Pitfalls
Incorrectly calculating execution time when stalls are present.
Assuming pipelining reduces the execution time of a single instruction.
Standard Problem-Solving Techniques
Draw pipeline diagrams to visualize instruction flow, identify hazards, and calculate stalls.
Runtime Environment
The runtime environment refers to the state of a program during its execution, encompassing all resources and
conditions necessary for the program to run. This includes the CPU's registers, memory (stack, heap, code, data
segments), program counter, and operating system services.
Important Formulas & Concepts
Includes CPU state (registers, PC, flags), memory layout (code, data, heap, stack), and OS resources.
Key Properties & Identities
Managed by the operating system and supported by the hardware architecture.
Defines how programs interact with the underlying system.
Common Pitfalls
Not understanding the distinction between compile-time and run-time aspects of a program.
Standard Problem-Solving Techniques
Understand how memory is organized and utilized by a program during execution (e.g., stack for function calls, heap
for dynamic allocation).
Speedup
Speedup is a measure of how much faster a task executes on an improved system compared to an original system. It
quantifies the performance gain achieved by optimizations like pipelining, parallel processing, or using faster
components.
Important Formulas & Concepts
General Speedup:
Amdahl's Law: Calculates the theoretical maximum speedup for a system when only a portion of the task can be
improved.

*(PDF Page 26)*

where is the proportion of the program that can be enhanced, and Pipelining Speedup (for large N): (number of pipeline stages).
is the speedup of the enhanced part.
Key Properties & Identities
Amdahl's Law highlights that the sequential portion of a program limits overall speedup.
Speedup is a dimensionless quantity.
Common Pitfalls
Incorrectly applying Amdahl's Law, especially regarding the value of .
Forgetting to account for overheads or non-ideal conditions in pipelining.
Standard Problem-Solving Techniques
Identify the parallelizable and sequential components of a task when using Amdahl's Law.
Stall
A stall (also known as a bubble or NOP) is a delay introduced into a pipeline to resolve a hazard. When a hazard is
detected, the pipeline is temporarily halted for one or more clock cycles, preventing the dependent instruction from
proceeding until the hazard is cleared.
Important Formulas & Concepts
Stalls increase the CPI (Cycles Per Instruction) of the pipeline.
Number of stalls depends on the type of hazard and the pipeline's ability to forward data.
Key Properties & Identities
Reduces the effective throughput and speedup of the pipeline.
A common method to ensure correctness in the presence of data and control hazards.
Common Pitfalls
Incorrectly calculating the number of stalls required for a given hazard, especially when forwarding is implemented.
Standard Problem-Solving Techniques
Draw pipeline diagrams and mark the clock cycles where stalls are inserted to resolve dependencies.
Virtual Memory
Virtual memory is a memory management technique that allows a computer to compensate for physical memory
shortages by temporarily transferring data from RAM to disk storage. It provides the illusion of a larger, contiguous
memory space to programs.
Important Formulas & Concepts
Paging: Divides memory into fixed-size blocks (pages and frames).
Page Table: Maps virtual page numbers to physical frame numbers.
TLB (Translation Lookaside Buffer): A small, fast cache for page table entries.
Effective Access Time (EAT) with TLB:
where is TLB access time and Effective Access Time (EAT) with Page Faults:
is main memory access time.

*(PDF Page 27)*

where is the page fault rate, (including disk I/O).
is memory access time, and is the time to handle a page fault
Key Properties & Identities
Provides memory protection, allows multitasking, and enables programs larger than physical memory.
Address translation involves converting virtual addresses to physical addresses.
Common Pitfalls
Incorrectly calculating EAT, especially when considering both TLB misses and page faults.
Confusing page table entries with TLB entries.
Standard Problem-Solving Techniques
Trace the address translation process (TLB lookup, page table lookup, page fault handling).
Quick Formula Reference
Topic Formula/Concept
Average Memory
Access Time (AMAT)
Single-level cache:
Two-level cache:
Cache Memory
(Address Breakdown)
Block Offset bits:
Direct Mapped Index bits:
Set-Associative Index bits:
Tag bits:
Direct Mapped Index:
Disk Access Time
Pipelining Performance
Execution time (N instructions, K stages, ideal):
Ideal Speedup (large N):
Actual CPI:
Speedup (Amdahl's
Law)
Virtual Memory (EAT)
With TLB:
With Page Faults:
Important Tips for GATE
Master Numerical Problems: A significant portion of COA questions are numerical, especially on Cache Memory
(AMAT, address breakdown), Pipelining (execution time, speedup, stalls), Disk Access Time, and Virtual Memory
(EAT). Practice these extensively.
Address Breakdown is Key: For cache and virtual memory, thoroughly understand how a logical/physical address
is divided into Tag, Index/Page Number, and Offset. This is fundamental for many problems.
Pipeline Diagrams: Learn to draw and analyze pipeline diagrams for instruction sequences. This is the best way to
identify data/control hazards and calculate the number of stalls or benefits of forwarding.

*(PDF Page 28)*

Conceptual Clarity: Don't just memorize definitions. Understand the "why" behind concepts. For example, why
RISC is better for pipelining, why cache works (locality), or why DMA is used.
Distinguish Similar Concepts: Be clear on the differences between CISC/RISC, hardwired/microprogrammed
control, various addressing modes, and different types of hazards (structural, data, control).
Read Questions Carefully: Pay close attention to units (ns, ms, cycles), specific assumptions (e.g.,
"no
forwarding,
" "average rotational latency"), and what is being asked (e.g., total time vs. speedup).
Amdahl's Law: This formula frequently appears in questions related to performance improvement. Understand how
to apply it correctly, especially identifying the parallelizable portion .
Time Management: Some numerical problems can be lengthy. If you get stuck or find a calculation too complex,
consider moving on and returning later. Look for shortcuts or approximations if applicable.
Addressing Modes (19)

---

## 4. Complete Question Index & Answer Key Record (250 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `1.1.1` | Addressing Modes: GATE CSE 1987 \| Question: 1-V | **C** |
| `1.1.2` | Addressing Modes: GATE CSE 1988 \| Question: 9iii | **N/A** |
| `1.1.3` | Addressing Modes: GATE CSE 1989 \| Question: 2-ii | **N/A** |
| `1.1.4` | Addressing Modes: GATE CSE 1993 \| Question: 10 | **N/A** |
| `1.1.5` | Addressing Modes: GATE CSE 1996 \| Question: 1.16, ISRO2016-42 | **B** |
| `1.1.6` | Addressing Modes: GATE CSE 1998 \| Question: 1.19 | **D** |
| `1.1.7` | Addressing Modes: GATE CSE 1999 \| Question: 2.23 | **A;B;C;D** |
| `1.1.8` | Addressing Modes: GATE CSE 2000 \| Question: 1.10 | **C** |
| `1.1.9` | Addressing Modes: GATE CSE 2001 \| Question: 2.9 | **A** |
| `1.1.10` | Addressing Modes: GATE CSE 2002 \| Question: 1.24 | **B** |
| `1.1.11` | Addressing Modes: GATE CSE 2004 \| Question: 20 | **C** |
| `1.1.12` | Addressing Modes: GATE CSE 2005 \| Question: 65 | **B** |
| `1.1.13` | Addressing Modes: GATE CSE 2005 \| Question: 66 | **C** |
| `1.1.14` | Addressing Modes: GATE CSE 2008 \| Question: 33, ISRO2009-80 | **C** |
| `1.1.15` | Addressing Modes: GATE CSE 2011 \| Question: 21 | **D** |
| `1.1.16` | Addressing Modes: GATE CSE 2017 \| Set 1 \| Question: 11 | **D** |
| `1.1.17` | Addressing Modes: GATE CSE 2026 \| Set 1 \| Question: 4 | **B** |
| `1.1.18` | Addressing Modes: GATE IT 2006 \| Question: 39, ISRO2009-42 | **D** |
| `1.1.19` | Addressing Modes: GATE IT 2006 \| Question: 40 | **D** |
| `1.2.1` | Average Memory Access Time: GATE CSE 1992 \| Question: 5-a | **180** |
| `1.2.2` | Average Memory Access Time: GATE CSE 2025 \| Set 1 \| Question: 43 | **11.83:11.87** |
| `1.2.3` | Average Memory Access Time: GATE CSE 2025 \| Set 2 \| Question: 45 | **4:4** |
| `1.3.1` | Bit Vector: GATE CSE 2026 \| Set 2 \| Question: 43 | **16417** |
| `1.4.1` | CISC RISC Architecture: GATE CSE 1999 \| Question: 2.22 | **A;B;C;D** |
| `1.4.2` | CISC RISC Architecture: GATE CSE 2018 \| Question: 5 | **D** |
| `1.5.1` | Cache Memory: GATE CSE 1987 \| Question: 4b | **N/A** |
| `1.5.2` | Cache Memory: GATE CSE 1989 \| Question: 6a | **N/A** |
| `1.5.3` | Cache Memory: GATE CSE 1990 \| Question: 7a | **22** |
| `1.5.4` | Cache Memory: GATE CSE 1993 \| Question: 11 | **N/A** |
| `1.5.5` | Cache Memory: GATE CSE 1995 \| Question: 1.6 | **D** |
| `1.5.6` | Cache Memory: GATE CSE 1995 \| Question: 2.25 | **D** |
| `1.5.7` | Cache Memory: GATE CSE 1996 \| Question: 26 | **61.25** |
| `1.5.8` | Cache Memory: GATE CSE 1998 \| Question: 18 | **N/A** |
| `1.5.9` | Cache Memory: GATE CSE 1999 \| Question: 1.22 | **B** |
| `1.5.10` | Cache Memory: GATE CSE 2001 \| Question: 1.7, ISRO2008-18 | **B** |
| `1.5.11` | Cache Memory: GATE CSE 2001 \| Question: 9 | **N/A** |
| `1.5.12` | Cache Memory: GATE CSE 2002 \| Question: 10 | **N/A** |
| `1.5.13` | Cache Memory: GATE CSE 2004 \| Question: 65 | **C** |
| `1.5.14` | Cache Memory: GATE CSE 2005 \| Question: 67 | **A** |
| `1.5.15` | Cache Memory: GATE CSE 2006 \| Question: 74 | **A** |
| `1.5.16` | Cache Memory: GATE CSE 2006 \| Question: 75 | **D** |
| `1.5.17` | Cache Memory: GATE CSE 2006 \| Question: 80 | **C** |
| `1.5.18` | Cache Memory: GATE CSE 2006 \| Question: 81 | **B** |
| `1.5.19` | Cache Memory: GATE CSE 2007 \| Question: 10 | **D** |
| `1.5.20` | Cache Memory: GATE CSE 2007 \| Question: 80 | **C** |
| `1.5.21` | Cache Memory: GATE CSE 2007 \| Question: 81 | **A** |
| `1.5.22` | Cache Memory: GATE CSE 2008 \| Question: 35 | **A** |
| `1.5.23` | Cache Memory: GATE CSE 2008 \| Question: 71 | **D** |
| `1.5.24` | Cache Memory: GATE CSE 2008 \| Question: 72 | **B** |
| `1.5.25` | Cache Memory: GATE CSE 2008 \| Question: 73 | **C** |
| `1.5.26` | Cache Memory: GATE CSE 2009 \| Question: 29 | **D** |
| `1.5.27` | Cache Memory: GATE CSE 2010 \| Question: 48 | **C** |
| `1.5.28` | Cache Memory: GATE CSE 2010 \| Question: 49 | **C** |
| `1.5.29` | Cache Memory: GATE CSE 2011 \| Question: 43 | **D** |
| `1.5.30` | Cache Memory: GATE CSE 2012 \| Question: 54 | **C** |
| `1.5.31` | Cache Memory: GATE CSE 2012 \| Question: 55 | **A** |
| `1.5.32` | Cache Memory: GATE CSE 2013 \| Question: 20 | **A** |
| `1.5.33` | Cache Memory: GATE CSE 2014 \| Set 1 \| Question: 44 | **A** |
| `1.5.34` | Cache Memory: GATE CSE 2014 \| Set 2 \| Question: 43 | **D** |
| `1.5.35` | Cache Memory: GATE CSE 2014 \| Set 2 \| Question: 44 | **D** |
| `1.5.36` | Cache Memory: GATE CSE 2014 \| Set 2 \| Question: 9 | **20** |
| `1.5.37` | Cache Memory: GATE CSE 2014 \| Set 3 \| Question: 44 | **1.68** |
| `1.5.38` | Cache Memory: GATE CSE 2015 \| Set 2 \| Question: 24 | **14** |
| `1.5.39` | Cache Memory: GATE CSE 2015 \| Set 3 \| Question: 14 | **A** |
| `1.5.40` | Cache Memory: GATE CSE 2016 \| Set 2 \| Question: 32 | **24** |
| `1.5.41` | Cache Memory: GATE CSE 2016 \| Set 2 \| Question: 50 | **30** |
| `1.5.42` | Cache Memory: GATE CSE 2017 \| Set 1 \| Question: 25 | **0.05** |
| `1.5.43` | Cache Memory: GATE CSE 2017 \| Set 1 \| Question: 54 | **14** |
| `1.5.44` | Cache Memory: GATE CSE 2017 \| Set 2 \| Question: 29 | **A** |
| `1.5.45` | Cache Memory: GATE CSE 2017 \| Set 2 \| Question: 45 | **4.7** |
| `1.5.46` | Cache Memory: GATE CSE 2017 \| Set 2 \| Question: 53 | **18** |
| `1.5.47` | Cache Memory: GATE CSE 2018 \| Question: 34 | **B** |
| `1.5.48` | Cache Memory: GATE CSE 2019 \| Question: 1 | **D** |
| `1.5.49` | Cache Memory: GATE CSE 2019 \| Question: 45 | **160** |
| `1.5.50` | Cache Memory: GATE CSE 2020 \| Question: 21 | **13.3:13.3;13.5:13.5** |
| `1.5.51` | Cache Memory: GATE CSE 2020 \| Question: 30 | **B** |
| `1.5.52` | Cache Memory: GATE CSE 2021 \| Set 1 \| Question: 22 | **17** |
| `1.5.53` | Cache Memory: GATE CSE 2021 \| Set 2 \| Question: 19 | **2** |
| `1.5.54` | Cache Memory: GATE CSE 2021 \| Set 2 \| Question: 27 | **A** |
| `1.5.55` | Cache Memory: GATE CSE 2022 \| Question: 14 | **A;B;D** |
| `1.5.56` | Cache Memory: GATE CSE 2022 \| Question: 23 | **0.85** |
| `1.5.57` | Cache Memory: GATE CSE 2023 \| Question: 54 | **19** |
| `1.5.58` | Cache Memory: GATE CSE 2024 \| Set 1 \| Question: 43 | **B;C** |
| `1.5.59` | Cache Memory: GATE CSE 2024 \| Set 1 \| Question: 46 | **3** |
| `1.5.60` | Cache Memory: GATE CSE 2026 \| Set 1 \| Question: 28 | **A** |
| `1.5.61` | Cache Memory: GATE CSE 2026 \| Set 1 \| Question: 44 | **B;C** |
| `1.5.62` | Cache Memory: GATE IT 2004 \| Question: 12, ISRO2016-77 | **C** |
| `1.5.63` | Cache Memory: GATE IT 2004 \| Question: 48 | **B** |
| `1.5.64` | Cache Memory: GATE IT 2005 \| Question: 61 | **C** |
| `1.5.65` | Cache Memory: GATE IT 2006 \| Question: 42 | **C** |
| `1.5.66` | Cache Memory: GATE IT 2006 \| Question: 43 | **A** |
| `1.5.67` | Cache Memory: GATE IT 2007 \| Question: 37 | **B** |
| `1.5.68` | Cache Memory: GATE IT 2008 \| Question: 80 | **D** |
| `1.5.69` | Cache Memory: GATE IT 2008 \| Question: 81 | **A** |
| `1.6.1` | Conflict Misses: GATE CSE 2017 \| Set 1 \| Question: 51 | **76** |
| `1.7.1` | Control Unit: GATE CSE 1987 \| Question: 1-vi | **B** |
| `1.8.1` | DMA: GATE CSE 2004 \| Question: 68 | **D** |
| `1.8.2` | DMA: GATE CSE 2005 \| Question: 70 | **B** |
| `1.8.3` | DMA: GATE CSE 2016 \| Set 1 \| Question: 31 | **456** |
| `1.8.4` | DMA: GATE CSE 2021 \| Set 2 \| Question: 20 | **80000** |
| `1.8.5` | DMA: GATE CSE 2022 \| Question: 7 | **A** |
| `1.8.6` | DMA: GATE CSE 2024 \| Set 1 \| Question: 5 | **C** |
| `1.8.7` | DMA: GATE CSE 2024 \| Set 2 \| Question: 1 | **C** |
| `1.8.8` | DMA: GATE IT 2004 \| Question: 51 | **C** |
| `1.9.1` | DRAM: GATE CSE 2019 \| Question: 2 | **A** |
| `1.10.1` | Data Dependency: GATE CSE 2005 \| Question: 68 | **A** |
| `1.10.2` | Data Dependency: GATE CSE 2008 \| Question: 36 | **B** |
| `1.10.3` | Data Dependency: GATE CSE 2015 \| Set 3 \| Question: 47 | **B** |
| `1.10.4` | Data Dependency: GATE IT 2007 \| Question: 39 | **B** |
| `1.11.1` | Data Hazards: GATE CSE 2026 \| Set 1 \| Question: 6 | **B** |
| `1.12.1` | Data Path: GATE CSE 1990 \| Question: 8a | **N/A** |
| `1.12.2` | Data Path: GATE CSE 2001 \| Question: 2.13 | **D** |
| `1.12.3` | Data Path: GATE CSE 2005 \| Question: 79 | **B** |
| `1.12.4` | Data Path: GATE CSE 2005 \| Question: 80 | **B** |
| `1.12.5` | Data Path: GATE CSE 2016 \| Set 2 \| Question: 30 | **28** |
| `1.12.6` | Data Path: GATE CSE 2020 \| Question: 4 | **C** |
| `1.12.7` | Data Path: GATE CSE 2025 \| Set 1 \| Question: 17 | **A;B;C** |
| `1.13.1` | Direct Mapping: GATE CSE 2022 \| Question: 44 | **A;B;D** |
| `1.13.2` | Direct Mapping: GATE CSE 2025 \| Set 1 \| Question: 26 | **A** |
| `1.13.3` | Direct Mapping: GATE CSE 2025 \| Set 2 \| Question: 29 | **A** |
| `1.13.4` | Direct Mapping: GATE CSE 2026 \| Set 2 \| Question: 42 | **A;B** |
| `1.13.5` | Direct Mapping: GATE CSE 2026 \| Set 2 \| Question: 46 | **128** |
| `1.14.1` | Disk: GATE CSE 2026 \| Set 1 \| Question: 49 | **77.3** |
| `1.15.1` | Hazards: GATE CSE 2026 \| Set 1 \| Question: 50 | **95** |
| `1.16.1` | IO Handling: GATE CSE 1987 \| Question: 2a | **True** |
| `1.16.2` | IO Handling: GATE CSE 1987 \| Question: 2b | **True** |
| `1.16.3` | IO Handling: GATE CSE 1990 \| Question: 4-ii | **False** |
| `1.16.4` | IO Handling: GATE CSE 1996 \| Question: 1.24 | **A** |
| `1.16.5` | IO Handling: GATE CSE 1996 \| Question: 25 | **1.4** |
| `1.16.6` | IO Handling: GATE CSE 1997 \| Question: 2.4 | **B** |
| `1.16.7` | IO Handling: GATE CSE 2008 \| Question: 64, ISRO2009-13 | **B** |
| `1.16.8` | IO Handling: GATE CSE 2011 \| Question: 28 | **A** |
| `1.17.1` | Instruction Execution: GATE CSE 1990 \| Question: 4-iii | **False** |
| `1.17.2` | Instruction Execution: GATE CSE 1992 \| Question: 01-iv | **N/A** |
| `1.17.3` | Instruction Execution: GATE CSE 1995 \| Question: 1.2 | **C** |
| `1.17.4` | Instruction Execution: GATE CSE 2002 \| Question: 1.13 | **C** |
| `1.17.5` | Instruction Execution: GATE CSE 2006 \| Question: 43 | **A** |
| `1.17.6` | Instruction Execution: GATE CSE 2017 \| Set 1 \| Question: 49 | **-16.0** |
| `1.17.7` | Instruction Execution: GATE CSE 2025 \| Set 2 \| Question: 51 | **3.0:3.0** |
| `1.18.2` | Instruction Format: GATE CSE 1992 \| Question: 01-vi | **256** |
| `1.18.3` | Instruction Format: GATE CSE 1994 \| Question: 3.2 | **True** |
| `1.18.4` | Instruction Format: GATE CSE 2014 \| Set 1 \| Question: 9 | **16383** |
| `1.18.5` | Instruction Format: GATE CSE 2016 \| Set 2 \| Question: 31 | **500** |
| `1.18.6` | Instruction Format: GATE CSE 2018 \| Question: 51 | **32** |
| `1.18.7` | Instruction Format: GATE CSE 2020 \| Question: 44 | **14** |
| `1.18.8` | Instruction Format: GATE CSE 2024 \| Set 2 \| Question: 47 | **32** |
| `1.18.9` | Instruction Format: GATE CSE 2024 \| Set 2 \| Question: 51 | **34** |
| `1.18.10` | Instruction Format: GATE CSE 2026 \| Set 1 \| Question: 5 | **D** |
| `1.18.11` | Instruction Format: GATE CSE 2026 \| Set 2 \| Question: 34 | **B** |
| `1.19.1` | Instruction Set Architecture: GATE CSE 2025 \| Set 2 \| Question: 18 | **D** |
| `1.20.1` | Interrupts: GATE CSE 1987 \| Question: 1-viii | **D** |
| `1.20.2` | Interrupts: GATE CSE 1995 \| Question: 1.3 | **B** |
| `1.20.3` | Interrupts: GATE CSE 1998 \| Question: 1.20 | **A** |
| `1.20.4` | Interrupts: GATE CSE 2002 \| Question: 1.9 | **A** |
| `1.20.5` | Interrupts: GATE CSE 2005 \| Question: 69 | **B** |
| `1.20.6` | Interrupts: GATE CSE 2009 \| Question: 8, UGCNET-June2012-III: 58 | **C** |
| `1.20.7` | Interrupts: GATE CSE 2020 \| Question: 3 | **C** |
| `1.20.8` | Interrupts: GATE CSE 2023 \| Question: 24 | **10.2** |
| `1.20.9` | Interrupts: GATE CSE 2025 \| Set 1 \| Question: 1 | **A** |
| `1.20.10` | Interrupts: GATE CSE 2026 \| Set 2 \| Question: 8 | **C** |
| `1.21.1` | Machine Instruction: GATE CSE 1988 \| Question: 9i | **N/A** |
| `1.21.2` | Machine Instruction: GATE CSE 1994 \| Question: 12 | **N/A** |
| `1.21.3` | Machine Instruction: GATE CSE 1999 \| Question: 17 | **N/A** |
| `1.21.4` | Machine Instruction: GATE CSE 2003 \| Question: 48 | **B** |
| `1.21.5` | Machine Instruction: GATE CSE 2003 \| Question: 49 | **A** |
| `1.21.6` | Machine Instruction: GATE CSE 2004 \| Question: 63 | **D** |
| `1.21.7` | Machine Instruction: GATE CSE 2004 \| Question: 64 | **B** |
| `1.21.8` | Machine Instruction: GATE CSE 2006 \| Question: 09, ISRO2009-35 | **C** |
| `1.21.9` | Machine Instruction: GATE CSE 2007 \| Question: 54 | **B** |
| `1.21.10` | Machine Instruction: GATE CSE 2007 \| Question: 71 | **D** |
| `1.21.11` | Machine Instruction: GATE CSE 2007 \| Question: 72 | **A** |
| `1.21.12` | Machine Instruction: GATE CSE 2007 \| Question: 73 | **C** |
| `1.21.13` | Machine Instruction: GATE CSE 2008 \| Question: 34 | **D** |
| `1.21.14` | Machine Instruction: GATE CSE 2015 \| Set 2 \| Question: 42 | **D** |
| `1.21.15` | Machine Instruction: GATE CSE 2016 \| Set 2 \| Question: 10 | **16** |
| `1.21.16` | Machine Instruction: GATE CSE 2021 \| Set 1 \| Question: 55 | **50** |
| `1.21.17` | Machine Instruction: GATE CSE 2023 \| Question: 31 | **B** |
| `1.21.18` | Machine Instruction: GATE CSE 2025 \| Set 1 \| Question: 27 | **B** |
| `1.21.19` | Machine Instruction: GATE IT 2004 \| Question: 46 | **D** |
| `1.21.20` | Machine Instruction: GATE IT 2007 \| Question: 41 | **C** |
| `1.21.21` | Machine Instruction: GATE IT 2008 \| Question: 38 | **A** |
| `1.22.1` | Memory Interfacing: GATE CSE 1990 \| Question: 4-iv | **TBA** |
| `1.22.2` | Memory Interfacing: GATE CSE 1991 \| Question: 01,ii | **N/A** |
| `1.22.3` | Memory Interfacing: GATE CSE 2006 \| Question: 41 | **D** |
| `1.22.4` | Memory Interfacing: GATE CSE 2016 \| Set 1 \| Question: 09 | **31** |
| `1.22.5` | Memory Interfacing: GATE CSE 2018 \| Question: 23 | **59** |
| `1.22.6` | Memory Interfacing: GATE CSE 2023 \| Question: 32 | **C** |
| `1.23.1` | Microprogramming: GATE CSE 1987 \| Question: 4a | **N/A** |
| `1.23.2` | Microprogramming: GATE CSE 1996 \| Question: 2.25 | **C** |
| `1.23.3` | Microprogramming: GATE CSE 1997 \| Question: 5.3 | **C** |
| `1.23.4` | Microprogramming: GATE CSE 1999 \| Question: 2.19 | **B** |
| `1.23.5` | Microprogramming: GATE CSE 2002 \| Question: 2.7 | **D** |
| `1.23.6` | Microprogramming: GATE CSE 2004 \| Question: 67 | **A** |
| `1.23.7` | Microprogramming: GATE CSE 2013 \| Question: 28 | **D** |
| `1.23.8` | Microprogramming: GATE IT 2004 \| Question: 49 | **A** |
| `1.23.9` | Microprogramming: GATE IT 2005 \| Question: 45 | **D** |
| `1.23.10` | Microprogramming: GATE IT 2005 \| Question: 49 | **B** |
| `1.23.11` | Microprogramming: GATE IT 2006 \| Question: 41 | **D** |
| `1.23.12` | Microprogramming: GATE IT 2008 \| Question: 39 | **D** |
| `1.24.1` | Pipelining: GATE CSE 1999 \| Question: 13 | **15** |
| `1.24.2` | Pipelining: GATE CSE 2000 \| Question: 1.8 | **B** |
| `1.24.3` | Pipelining: GATE CSE 2000 \| Question: 12 | **N/A** |
| `1.24.4` | Pipelining: GATE CSE 2001 \| Question: 12 | **N/A** |
| `1.24.5` | Pipelining: GATE CSE 2002 \| Question: 2.6, ISRO2008-19 | **D** |
| `1.24.6` | Pipelining: GATE CSE 2003 \| Question: 10, ISRO-DEC2017-41 | **D** |
| `1.24.7` | Pipelining: GATE CSE 2004 \| Question: 69 | **C** |
| `1.24.8` | Pipelining: GATE CSE 2006 \| Question: 42 | **C** |
| `1.24.9` | Pipelining: GATE CSE 2007 \| Question: 37, ISRO2009-37 | **B** |
| `1.24.10` | Pipelining: GATE CSE 2008 \| Question: 76 | **A** |
| `1.24.11` | Pipelining: GATE CSE 2008 \| Question: 77 | **D** |
| `1.24.12` | Pipelining: GATE CSE 2009 \| Question: 28 | **B** |
| `1.24.13` | Pipelining: GATE CSE 2010 \| Question: 33 | **B** |
| `1.24.14` | Pipelining: GATE CSE 2011 \| Question: 41 | **B** |
| `1.24.15` | Pipelining: GATE CSE 2012 \| Question: 20, ISRO2016-23 | **C** |
| `1.24.16` | Pipelining: GATE CSE 2013 \| Question: 45 | **B** |
| `1.24.17` | Pipelining: GATE CSE 2014 \| Set 3 \| Question: 43 | **1.50** |
| `1.24.18` | Pipelining: GATE CSE 2014 \| Set 3 \| Question: 9 | **C** |
| `1.24.19` | Pipelining: GATE CSE 2015 \| Set 1 \| Question: 38 | **3.2** |
| `1.24.20` | Pipelining: GATE CSE 2015 \| Set 2 \| Question: 44 | **13** |
| `1.24.21` | Pipelining: GATE CSE 2015 \| Set 3 \| Question: 51 | **3** |
| `1.24.22` | Pipelining: GATE CSE 2016 \| Set 1 \| Question: 32 | **33.0** |
| `1.24.23` | Pipelining: GATE CSE 2016 \| Set 2 \| Question: 33 | **4** |
| `1.24.24` | Pipelining: GATE CSE 2017 \| Set 1 \| Question: 50 | **1.50** |
| `1.24.25` | Pipelining: GATE CSE 2018 \| Question: 50 | **219** |
| `1.24.26` | Pipelining: GATE CSE 2020 \| Question: 43 | **2.15:2.18** |
| `1.24.27` | Pipelining: GATE CSE 2021 \| Set 1 \| Question: 53 | **17160** |
| `1.24.28` | Pipelining: GATE CSE 2021 \| Set 2 \| Question: 53 | **1.87** |
| `1.24.29` | Pipelining: GATE CSE 2023 \| Question: 23 | **2040** |
| `1.24.30` | Pipelining: GATE CSE 2024 \| Set 1 \| Question: 20 | **A;B;C** |
| `1.24.31` | Pipelining: GATE CSE 2024 \| Set 2 \| Question: 21 | **A** |
| `1.24.32` | Pipelining: GATE CSE 2024 \| Set 2 \| Question: 48 | **3** |
| `1.24.33` | Pipelining: GATE CSE 2025 \| Set 2 \| Question: 46 | **260.20:261.20** |
| `1.24.34` | Pipelining: GATE IT 2004 \| Question: 47 | **C** |
| `1.24.35` | Pipelining: GATE IT 2005 \| Question: 44 | **B** |
| `1.24.36` | Pipelining: GATE IT 2006 \| Question: 78 | **C** |
| `1.24.37` | Pipelining: GATE IT 2006 \| Question: 79 | **B** |
| `1.24.38` | Pipelining: GATE IT 2007 \| Question: 6, ISRO2011-25 | **B** |
| `1.24.39` | Pipelining: GATE IT 2008 \| Question: 40 | **C** |
| `1.25.1` | Runtime Environment: GATE CSE 2001 \| Question: 1.10, UGCNET-Dec2012-III: 36 | **X** |
| `1.25.2` | Runtime Environment: GATE CSE 2008 \| Question: 37, ISRO2009-38 | **A** |
| `1.26.1` | Speedup: GATE CSE 2014 \| Set 1 \| Question: 43 | **4** |
| `1.26.2` | Speedup: GATE CSE 2014 \| Set 1 \| Question: 55 | **1.6** |
| `1.26.3` | Speedup: GATE CSE 2024 \| Set 1 \| Question: 45 | **3** |
| `1.26.4` | Speedup: GATE CSE 2026 \| Set 2 \| Question: 47 | **2.30:2.40** |
| `1.26.5` | Speedup: GATE IT 2004 \| Question: 50 | **A** |
| `1.26.6` | Speedup: GATE IT 2007 \| Question: 36 | **B** |
| `1.27.1` | Stall: GATE CSE 2022 \| Question: 51 | **1.42:1.45** |
| `1.28.1` | Virtual Memory: GATE CSE 1991 \| Question: 03,iii | **A;B** |
| `1.28.2` | Virtual Memory: GATE CSE 2004 \| Question: 47 | **D** |
| `1.28.3` | Virtual Memory: GATE CSE 2008 \| Question: 38 | **C** |

