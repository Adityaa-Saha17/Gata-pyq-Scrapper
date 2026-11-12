# Volume 3 — Chapter 2: Computer Networks

- **Source PDF**: [filter1_volume3.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume3.pdf)
- **Total GATE Questions in Chapter**: **226**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **2.2** | Arp | 1 |
| **2.3** | Bit Stuffing | 2 |
| **2.4** | Bridges | 3 |
| **2.5** | CRC Polynomial | 5 |
| **2.6** | CSMA CD | 6 |
| **2.7** | Channel Utilization | 1 |
| **2.8** | Communication | 4 |
| **2.9** | Congestion Control | 9 |
| **2.10** | Data Communication | 1 |
| **2.11** | Distance Vector Routing | 8 |
| **2.12** | Error Detection | 8 |
| **2.13** | Ethernet | 7 |
| **2.14** | Fragmentation | 5 |
| **2.15** | Hamming Code | 2 |
| **2.16** | IP Addressing | 8 |
| **2.17** | IP Packet | 12 |
| **2.18** | Icmp | 1 |
| **2.19** | LAN Technologies | 7 |
| **2.20** | MAC Protocol | 4 |
| **2.21** | Network Flow | 4 |
| **2.22** | Network Layer | 6 |
| **2.23** | Network Protocols | 11 |
| **2.24** | Network Switching | 4 |
| **2.25** | Osi Model | 1 |
| **2.26** | Probability | 1 |
| **2.27** | Pure Aloha | 1 |
| **2.28** | Routing | 14 |
| **2.30** | Sliding Window | 16 |
| **2.31** | Slotted Aloha | 1 |
| **2.32** | Sockets | 4 |
| **2.33** | Stop and Wait | 6 |
| **2.34** | Subnetting | 21 |
| **2.35** | TCP | 20 |
| **2.36** | Token Bucket | 2 |
| **2.37** | UDP | 4 |
| **2.38** | Wrap Around Time | 2 |


---

## 2. Comprehensive GATE CSE Computer Networks Reference (Expanded Research & Formulas)

### 2.1 Delay, Flow Control & Sliding Window Protocols
- **Delays**:
  - **Transmission Delay**: $T_t = \frac{L}{B}$ ($L =$ packet length in bits, $B =$ bandwidth in bps).
  - **Propagation Delay**: $T_p = \frac{d}{v}$ ($d =$ distance, $v =$ propagation speed).
  - **Ratio**: $a = \frac{T_p}{T_t}$.

| Protocol | Sender Window $W_s$ | Receiver Window $W_r$ | Min Sequence Numbers | Min Seq Bits $k$ | Efficiency / Utilization $\eta$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Stop-and-Wait ARQ** | $1$ | $1$ | $2$ | $1$ | $\frac{1}{1 + 2a}$ |
| **Go-Back-N (GBN)** | $W_s \le 2^k - 1$ | $1$ | $W_s + 1$ | $\lceil \log_2(W_s + 1) \rceil$ | $\min\!\left(1, \frac{W_s}{1 + 2a}\right)$ |
| **Selective Repeat (SR)** | $W_s \le 2^{k-1}$ | $W_r = W_s$ | $2 W_s$ | $\lceil \log_2(2 W_s) \rceil$ | $\min\!\left(1, \frac{W_s}{1 + 2a}\right)$ |

- **Optimal Window Size for 100% Link Utilization**: $W_s \ge 1 + 2a = \frac{T_t + 2T_p}{T_t} = \frac{\text{RTT} + T_t}{T_t}$ packets (or Bandwidth-Delay Product $B \times \text{RTT}$ bits).

### 2.2 MAC Protocols (ALOHA, CSMA/CD, Ethernet) & Error Control
- **Pure ALOHA vs Slotted ALOHA**:
  - **Pure ALOHA**: Vulnerable time $= 2 T_{fr}$; Throughput $S = G e^{-2G}$; Max efficiency $= \frac{1}{2e} \approx \mathbf{18.4\%}$ at $G = 0.5$.
  - **Slotted ALOHA**: Vulnerable time $= T_{fr}$; Throughput $S = G e^{-G}$; Max efficiency $= \frac{1}{e} \approx \mathbf{36.8\%}$ at $G = 1$.
- **CSMA/CD Minimum Frame Size (Golden GATE Formula!)**:
  $$T_t \ge 2 T_p \quad \Longrightarrow \quad \frac{L_{\min}}{B} \ge \frac{2d}{v} \quad \Longrightarrow \quad L_{\min} = 2 \cdot B \cdot T_p = \frac{2 \cdot d \cdot B}{v}$$
  - **Binary Exponential Backoff**: After $c$-th collision ($1 \le c \le 10$), random wait $K \in \{0, 1, \dots, 2^c - 1\}$ slot times (where 1 slot $= 2T_p = 51.2\;\mu\text{s}$ for 10 Mbps Ethernet = 512 bits = 64 bytes). Max $c$ is capped at $10$ (up to 16 attempts).
- **Hamming Distance & CRC**:
  - To **detect** up to $s$ bit errors: $d_{\min} \ge s + 1$.
  - To **correct** up to $t$ bit errors: $d_{\min} \ge 2t + 1$.
  - **Single-Bit Hamming Code** ($m$ data bits, $r$ parity bits): $2^r \ge m + r + 1$.

### 2.3 IPv4 Addressing, Subnetting & IP Fragmentation
- **CIDR Block `/n`**: Subnet mask has $n$ leading $1$s and $32 - n$ trailing $0$s.
  - Total IP addresses in block $= 2^{32-n}$; Usable hosts $= 2^{32-n} - 2$ (excluding network ID all-$0$s and directed broadcast all-$1$s).
  - **Longest Prefix Match**: Routers forward packets to the matching route table entry with the **longest subnet mask** (`/26` beats `/24`); default route `/0` (`0.0.0.0/0`) has shortest prefix.
- **IPv4 Header & Fragmentation**:
  - **Header Length (`IHL`)**: 4 bits, scaled by **4 bytes** (min $= 5 \implies 20$ bytes; max $= 15 \implies 60$ bytes).
  - **Total Length**: 16 bits (max IPv4 packet $= 65,535$ bytes).
  - **Fragmentation Rules**:
    - Every fragment except the last must have a **data payload size that is a multiple of 8 bytes**!
    - Max data per fragment $= \left\lfloor \frac{\text{MTU} - \text{Header}}{8} \right\rfloor \times 8$.
    - **Fragment Offset** (13 bits, scaled by **8 bytes**): $\text{Offset} = \frac{\text{Starting byte index of data}}{8}$.
    - **More Fragments (`MF`) Flag**: `MF = 1` for all fragments except the last (`MF = 0` for the last fragment or unfragmented packet).

### 2.4 Transport Layer (TCP / UDP), Congestion Control & Token Bucket
- **TCP Header**: Min 20 bytes, max 60 bytes (`HLEN` scaled by 4 bytes). Sequence numbers count **bytes**, not segments! (`SYN` and `FIN` each consume **1 sequence number** even without data; pure `ACK` consumes $0$).
- **Wrap-Around Time (WAT)**: Time to exhaust $2^{32}$ byte sequence space at bandwidth $B$ (bytes/sec): $\text{WAT} = \frac{2^{32}}{B}$.
- **TCP Congestion Control (`cwnd`, `ssthresh`)**:
  - **Effective Sender Window**: $\text{Window} = \min(\text{cwnd}, \text{rwnd})$.
  - **Slow Start** ($\text{cwnd} < \text{ssthresh}$): $\text{cwnd}$ increases by $+1\text{ MSS}$ per ACK $\implies$ **doubles every RTT** (exponential).
  - **Congestion Avoidance** ($\text{cwnd} \ge \text{ssthresh}$): $\text{cwnd}$ increases by $+1\text{ MSS}$ **per RTT** (linear / additive increase).
  - **Reaction to Congestion**:
    - **Timeout**: $\text{ssthresh} = \lfloor \text{cwnd} / 2 \rfloor$, $\text{cwnd} = 1\text{ MSS}$ (enters Slow Start).
    - **3 Duplicate ACKs (Fast Retransmit / Fast Recovery — TCP Reno)**: $\text{ssthresh} = \lfloor \text{cwnd} / 2 \rfloor$, $\text{cwnd} = \text{ssthresh}$ (continues in Congestion Avoidance).
- **Token Bucket Traffic Shaper**:
  - Bucket capacity $C$ bytes, token arrival rate $r$ bytes/sec, max output link rate $M$ bytes/sec ($M > r$).
  - **Maximum Burst Duration $S$** at peak rate $M$: $C + rS = MS \implies S = \frac{C}{M - r}$ seconds; Max burst size $= M \cdot S$.

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

2 Computer Networks (226)
Concept of layering.OSI and TCP/IP Protocol Stacks; Basics of packet, circuit and virtual circuit-
switching; Data link layer: framing, error detection, Medium Access Control, Ethernet bridging; Routing
protocols: shortest path, flooding, distance vector and link state routing; Fragmentation and IP addressing, IPv4, CIDR
notation, Basics of IP support protocols (ARP, DHCP, ICMP), Network Address Translation (NAT); Transport
layer: flow control and congestion control, UDP, TCP, sockets; Application layer protocols: DNS, SMTP, HTTP,
FTP, Email.
.
The Computer Networks chapter in GATE Computer Science is a fundamental and high-scoring area, essential for
understanding how modern computing systems communicate and interact. It covers everything from the physical
transmission of data to high-level application protocols, network architecture, and security principles. Mastery of this
subject is crucial not only for the GATE exam but also for a career in software development, system administration, and
network engineering. Typically, Computer Networks carries a weightage of 8-12 marks in the GATE CS exam, with
questions ranging from conceptual understanding of protocols and layers to numerical problems involving network
performance, addressing, and error control. Question patterns often include multiple-choice questions (MCQs), multiple-
select questions (MSQs), and numerical answer type (NAT) questions, testing both theoretical knowledge and problem-
solving skills.
Topic-wise Key Concepts
Application Layer Protocols
These protocols are at the highest layer of the TCP/IP model, providing services directly to user applications. They
define how applications on different hosts communicate and exchange data.
Key Concepts:
HTTP (Hypertext Transfer Protocol): Used for web browsing, client-server model, stateless. Default port 80.
FTP (File Transfer Protocol): Used for file transfer, uses two connections (control and data). Default ports 20
(data) and 21 (control).
DNS (Domain Name System): Translates domain names to IP addresses. UDP port 53 for queries, TCP port 53 for
zone transfers.
SMTP (Simple Mail Transfer Protocol): Used for sending emails. Default port 25.
POP3 (Post Office Protocol v3): Used for retrieving emails. Default port 110.
IMAP (Internet Message Access Protocol): More advanced email retrieval, allows managing mail on server.
Default port 143.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing the functions and default port numbers of different protocols.
Technique: Create a table mapping protocol to function and port number for quick recall.
ARP (Address Resolution Protocol)
ARP is a protocol used to map an IP address (Network Layer) to a physical MAC address (Data Link Layer) on a local
network. It is essential for IP packets to be encapsulated into Ethernet frames for local delivery.
Key Concepts:
ARP Request: Broadcasts a query to all hosts on the local network asking for the MAC address corresponding to a
specific IP.
ARP Reply: The host with the matching IP address sends a unicast reply containing its MAC address.
ARP Cache: Hosts maintain a cache of IP-to-MAC mappings to reduce ARP traffic.

*(PDF Page 96)*

Common Pitfalls and Problem-Solving Techniques:
Pitfall: Assuming ARP works across routers; it's a local network protocol.
Technique: Understand the ARP process step-by-step for tracing packet flows.
Bit Stuffing
Bit stuffing is a technique used in the Data Link Layer to prevent the flag sequence from appearing in the data portion of
a frame. It ensures that the receiver correctly identifies the start and end of a frame.
Key Concepts:
Flag Sequence: A unique bit pattern (e.g., 01111110) used to mark frame boundaries.
Stuffing Rule: Whenever five consecutive 1s appear in the data, an extra 0 bit is inserted (stuffed) by the sender.
Destuffing Rule: The receiver removes a 0 bit after five consecutive 1s.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly stuffing/destuffing bits, especially at the end of the data or near the flag sequence.
Technique: Practice with examples, carefully counting consecutive 1s.
Bridges
Bridges are Data Link Layer devices that connect two or more LAN segments. They filter frames based on MAC
addresses, forwarding only those frames destined for another segment, thus reducing collision domains and improving
network performance.
Key Concepts:
MAC Address Filtering: Bridges maintain a forwarding table (MAC address table) to decide whether to forward or
filter frames.
Learning: Bridges learn MAC addresses by inspecting the source MAC address of incoming frames.
Spanning Tree Protocol (STP): Used to prevent loops in bridged networks by disabling redundant paths.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing bridges with routers (Layer 3) or hubs (Layer 1). Bridges operate at Layer 2.
Technique: Trace frame paths in a bridged network, applying learning and forwarding rules.
CRC Polynomial (Cyclic Redundancy Check)
CRC is a powerful error detection technique used in the Data Link Layer. It appends a checksum (FCS - Frame Check
Sequence) to the data, calculated using polynomial division.
Important Formulas and Results:
Let be the data polynomial and be the generator polynomial of degree . To find the CRC remainder
:
where is the remainder polynomial of degree less than .
The transmitted codeword is:
This means the codeword is exactly divisible by .
Key Properties and Identities:

*(PDF Page 97)*

CRC can detect all single-bit errors, all double-bit errors, any odd number of errors, and all burst errors of length less
than or equal to .
It can detect a high percentage of burst errors longer than .
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Performing binary division incorrectly (modulo-2 arithmetic, no borrows).
Technique: Practice modulo-2 polynomial division. Remember to pad the data with zeros before division.
CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
CSMA/CD is a MAC protocol used in shared-medium networks like Ethernet. Stations listen before transmitting (carrier
sense) and stop transmitting if a collision is detected (collision detection).
Important Formulas and Results:
Slot Time: The maximum time it takes for a collision to be detected by all stations.
Minimum Frame Size: To ensure a collision is detected before the sender finishes transmitting the frame.
Key Properties and Identities:
Uses binary exponential backoff algorithm to resolve collisions.
Collision domain is the segment where collisions can occur.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing propagation delay with transmission delay. Propagation delay is time for a bit to travel,
transmission delay is time to put all bits on wire.
Technique: Ensure units are consistent (e.g., convert Mbps to bits/second, km to meters, ms to seconds).
Channel Utilization
Channel utilization (or efficiency) measures the fraction of time the channel is actively transmitting data, rather than
being idle or transmitting overhead. It's a key performance metric for network protocols.
Important Formulas and Results:
General formula:
For Stop-and-Wait ARQ:
where . This assumes no errors and negligible ACK transmission time.
For Sliding Window (Go-Back-N or Selective Repeat) with window size :
This assumes no errors. If For Pure Aloha:
, utilization can be 100%.

*(PDF Page 98)*

where is throughput, is offered load. Max at .
For Slotted Aloha:
Max at .
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly calculating or not considering the full round-trip time.
Technique: Clearly identify and from the problem statement. Remember is one-way.
Communication
Communication in networks refers to the process of exchanging information between two or more entities. It involves
various modes and fundamental concepts that define how data travels.
Key Concepts:
Simplex: Data flows in one direction only (e.g., radio broadcast).
Half-Duplex: Data flows in both directions, but not simultaneously (e.g., walkie-talkie).
Full-Duplex: Data flows in both directions simultaneously (e.g., telephone call).
Bandwidth: The maximum data transfer rate of a network path, typically measured in bits per second (bps).
Latency (Delay): The time it takes for a data packet to travel from one point to another. Comprises transmission,
propagation, processing, and queuing delays.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing bandwidth with throughput. Bandwidth is capacity, throughput is actual rate.
Technique: Understand the implications of each communication mode on protocol design (e.g., collision detection
in half-duplex).
Congestion Control
Congestion control mechanisms aim to prevent network collapse by regulating the rate at which senders transmit data
when the network is overloaded. TCP implements several strategies for this.
Key Concepts (TCP):
Slow Start: Exponentially increases congestion window (cwnd) at the beginning of a connection or after a timeout.
cwnd starts at 1 MSS (Maximum Segment Size) and doubles every RTT.
Congestion Avoidance: After cwnd reaches ssthresh (slow start threshold), cwnd increases linearly (by 1 MSS per
RTT).
Fast Retransmit: If the sender receives three duplicate ACKs, it retransmits the lost segment without waiting for a
timeout.
Fast Recovery: After Fast Retransmit, ssthresh is set to half of the current cwnd, and cwnd is set to ssthresh + 3
MSS. It then enters congestion avoidance.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly applying the rules for cwnd and ssthresh changes during slow start, congestion avoidance, and
recovery phases.
Technique: Draw a graph of cwnd vs. RTT to visualize the changes. Remember the ssthresh value is halved upon
a loss.
Data Communication
Data communication encompasses the processes, technologies, and methods involved in the electronic transmission of
information. It covers the physical and logical aspects of moving data between devices.

*(PDF Page 99)*

Key Concepts:
Signals: Electrical or electromagnetic waves used to transmit data. Can be analog or digital.
Modulation: Converting digital data into analog signals for transmission over analog media.
Demodulation: Converting analog signals back into digital data.
Multiplexing: Combining multiple data streams into a single stream for transmission (e.g., TDM, FDM, WDM).
Switching: Techniques for connecting communication paths (e.g., circuit, packet, message switching).
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing modulation with encoding, or different multiplexing techniques.
Technique: Understand the purpose and basic mechanism of each concept.
Distance Vector Routing
Distance Vector Routing is a dynamic routing algorithm where each router maintains a routing table (distance vector)
containing the best known distance to each destination and the next hop. Routers exchange their entire routing tables
with directly connected neighbors.
Key Concepts:
Bellman-Ford Algorithm: The underlying algorithm for distance vector routing.
where is the cost from to , is cost from to neighbor , and is 's reported cost to .
Count-to-Infinity Problem: A major drawback where routing loops can cause costs to increase indefinitely.
Poisoned Reverse: A mechanism to mitigate count-to-infinity by advertising infinite cost for routes learned from a
neighbor back to that neighbor.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly updating routing tables or failing to identify routing loops.
Technique: Simulate the routing table updates step-by-step for a given network topology and link cost changes.
Error Detection
Error detection techniques are used to determine if errors have occurred during data transmission. They add redundant
bits to the data, allowing the receiver to check for integrity.
Key Concepts:
Parity Check: Adds a single parity bit to make the total number of 1s even (even parity) or odd (odd parity). Detects
single-bit errors.
Checksum: Divides data into segments, sums them (using one's complement arithmetic), and takes the one's
complement of the sum as the checksum. Detects most errors, but not as robust as CRC.
CRC (Cyclic Redundancy Check): Most powerful error detection technique, uses polynomial division. (See CRC
Polynomial topic).
Important Formulas and Results:
Internet Checksum: Sum all 16-bit words (or specified size) of the data. If sum exceeds 16 bits, wrap around the
carry. Take one's complement of the final sum.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Forgetting one's complement arithmetic for checksum calculations.
Technique: Practice checksum calculations, especially with carry bits.
Ethernet

*(PDF Page 100)*

Ethernet is the most widely used LAN technology, standardized by IEEE 802.3. It defines the physical and Data Link
Layer specifications for wired networks, primarily using CSMA/CD.
Key Concepts:
MAC Address: A 48-bit (6-byte) unique hardware identifier assigned to each network interface card (NIC).
Ethernet Frame Format: Includes Preamble, SFD (Start Frame Delimiter), Destination MAC, Source MAC,
Type/Length, Data, and FCS (Frame Check Sequence/CRC).
Minimum/Maximum Frame Size: Standard Ethernet has a minimum frame size of 64 bytes (including header and
FCS) and a maximum of 1518 bytes.
CSMA/CD: The access method used for shared Ethernet segments.
Important Formulas and Results:
Minimum Data Size: 46 bytes (to ensure minimum frame size of 64 bytes, considering 18 bytes of header/trailer).
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing the total frame size with the data payload size.
Technique: Memorize the Ethernet frame structure and minimum/maximum sizes.
Fragmentation
Fragmentation is the process at the Network Layer (IP) where a large IP packet is divided into smaller fragments to
traverse a network link with a smaller Maximum Transmission Unit (MTU).
Important Formulas and Results:
Offset Field: In the IP header, indicates the position of the fragment's data relative to the original datagram's data,
in units of 8 bytes.
Total Length Field: In the IP header, indicates the total length of the current fragment (header + data).
More Fragments (MF) Flag: Set to 1 for all fragments except the last one.
Key Properties and Identities:
Fragmentation can occur at any router along the path.
Reassembly typically occurs only at the destination host.
The data payload of each fragment (except possibly the last) must be a multiple of 8 bytes.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly calculating the offset field or the data length of fragments, especially when the original packet's
data length is not a multiple of 8.
Technique: Work through fragmentation problems step-by-step, ensuring each fragment's data length is a multiple
of 8 (except the last) and updating the offset correctly.
Hamming Code
Hamming code is an error-correcting code capable of detecting and correcting single-bit errors. It adds redundant parity
bits at specific positions within the data.
Important Formulas and Results:
Number of Parity Bits ( satisfy:
): To correct single-bit errors in a message of data bits, the number of parity bits must

*(PDF Page 101)*

Parity Bit Positions: Parity bits are placed at positions that are powers of 2 (1, 2, 4, 8, ...).
Parity Check: Each parity bit checks specific data bit positions. For example, parity bit at position positions whose binary representation has the -th bit set.
checks all
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly assigning parity bit positions or calculating parity values.
Technique: Systematically determine parity bit positions, then calculate parity values based on the data bits they
cover. For error detection/correction, calculate syndrome bits.
IP Addressing
IP addressing (IPv4 and IPv6) is a fundamental concept in the Network Layer, providing unique logical addresses for
devices on a network. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses.
Important Formulas and Results (IPv4):
Number of Hosts: For a given subnet mask, if bits are available for host IDs, then the number of usable hosts is
(subtracting network and broadcast addresses).
Number of Subnets: If bits are borrowed from the host portion for subnetting, the number of subnets created is
.
CIDR (Classless Inter-Domain Routing): Uses a prefix length (e.g., /24) to specify the network portion of an IP
address, replacing class-based addressing.
Key Properties and Identities:
Network ID: All host bits are 0.
Broadcast ID: All host bits are 1.
Private IP Ranges: Reserved for private networks (e.g., 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly calculating subnet masks, network IDs, or broadcast IDs, especially with CIDR notation.
Technique: Convert IP addresses and subnet masks to binary for clear visualization. Practice subnetting problems
extensively.
IP Packet
An IP packet (or datagram) is the fundamental unit of data transfer in the Internet Protocol. It consists of an IP header
and a data payload.
Key Concepts (IPv4 Header Fields):
Version (4 bits): Indicates IPv4 or IPv6.
Header Length (IHL, 4 bits): Length of the IP header in 32-bit words. Minimum 5 (20 bytes), maximum 15 (60
bytes).
Total Length (16 bits): Total length of the IP datagram (header + data) in bytes. Max 65535 bytes.
Identification (16 bits): Used for reassembling fragmented datagrams.
Flags (3 bits): Includes DF (Don't Fragment) and MF (More Fragments).
Fragment Offset (13 bits): Position of the fragment in the original datagram (in 8-byte units).
Time To Live (TTL, 8 bits): Decremented by each router; packet is discarded if TTL reaches 0. Prevents infinite
loops.
Protocol (8 bits): Indicates the next-level protocol (e.g., 6 for TCP, 17 for UDP, 1 for ICMP).
Header Checksum (16 bits): Used for error detection only on the header. Recalculated at each hop.
Source IP Address (32 bits): Sender's IP address.
Destination IP Address (32 bits): Receiver's IP address.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing header length (in 32-bit words) with total length (in bytes).

*(PDF Page 102)*

Technique: Memorize the key fields and their sizes. Practice calculating header checksums.
ICMP (Internet Control Message Protocol)
ICMP is a Network Layer protocol used by network devices, like routers, to send error messages and operational
information indicating, for example, that a requested service is not available or that a host or router could not be
reached.
Key Concepts:
Error Reporting: Reports errors such as "Destination Unreachable,
" "Time Exceeded,
" "Parameter Problem.
"
Query Messages: Used for diagnostic purposes (e.g., Echo Request/Reply for ping, Timestamp Request/Reply).
Traceroute: Uses ICMP Time Exceeded messages to map the path to a destination.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing ICMP's role with routing protocols or transport layer protocols. ICMP is for network diagnostics
and error reporting.
type 11).
Technique: Understand the common ICMP message types and their uses (e.g., ping uses type 8/0, traceroute uses
LAN Technologies
LAN (Local Area Network) technologies define the standards and methods for connecting devices within a limited
geographical area. Ethernet is the dominant LAN technology.
Key Concepts:
Ethernet (IEEE 802.3): Dominant wired LAN technology, uses CSMA/CD (for shared media) or full-duplex
switching. Various speeds (10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps, etc.).
Token Ring (IEEE 802.5): Older LAN technology, uses a token-passing mechanism for media access. Devices
form a logical ring.
FDDI (Fiber Distributed Data Interface): High-speed token-passing LAN over fiber optics, uses dual rings for
redundancy.
Wi-Fi (IEEE 802.11): Wireless LAN technology, uses CSMA/CA (Collision Avoidance).
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing the MAC access methods (CSMA/CD vs. Token Passing vs. CSMA/CA).
Technique: Compare and contrast the characteristics, advantages, and disadvantages of different LAN
technologies.
MAC Protocol (Medium Access Control)
MAC protocols define how multiple stations share a common transmission medium to avoid collisions and ensure fair
access. They are part of the Data Link Layer.
Key Concepts:
Channel Partitioning Protocols: Divide the channel into smaller, independent channels (e.g., TDMA, FDMA,
CDMA).
Random Access Protocols: Allow stations to transmit whenever they have data, resolving collisions if they occur
(e.g., Aloha, CSMA, CSMA/CD, CSMA/CA).
Taking-Turns Protocols: Stations take turns accessing the channel (e.g., Token Ring, Polling).
Important Formulas and Results:
(See Pure Aloha, Slotted Aloha, CSMA/CD for specific formulas).
Common Pitfalls and Problem-Solving Techniques:

*(PDF Page 103)*

Pitfall: Misidentifying the type of MAC protocol or its collision resolution mechanism.
Technique: Understand the trade-offs between different MAC protocols (efficiency, fairness, complexity).
Network Flow
Network flow is a concept in graph theory used to model the movement of resources through a network. In computer
networks, it can represent data traffic.
Key Concepts:
Flow Network: A directed graph where each edge has a capacity and a flow.
Source and Sink: Special nodes representing the origin and destination of the flow.
Max-Flow Min-Cut Theorem: States that the maximum amount of flow passing from a source to a sink in a flow
network is equal to the total capacity of the minimum cut.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: While Max-Flow Min-Cut is a core concept, GATE CS typically tests its conceptual understanding rather than
complex numerical algorithms like Edmonds-Karp or Dinic.
Technique: Focus on understanding the theorem and identifying cuts in simple networks.
Network Layer
The Network Layer (Layer 3 of the OSI model) is responsible for logical addressing, routing, and forwarding packets
across different networks. IP is the primary protocol at this layer.
Key Concepts:
Logical Addressing: IP addresses provide unique identification for devices across the internet.
Routing: Determining the best path for packets to travel from source to destination.
Forwarding: Moving a packet from an incoming interface to an outgoing interface on a router.
Protocols: IP, ICMP, IGMP, Routing Protocols (RIP, OSPF, BGP).
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing Network Layer functions with Data Link Layer (MAC addressing, framing) or Transport Layer (port
numbers, reliability).
Technique: Clearly distinguish the responsibilities of each layer in the OSI/TCP-IP model.
Network Protocols
Network protocols are formal rules and standards that govern how devices communicate and exchange data over a
network. They define the format, timing, sequencing, and error control of data transmission.
Key Concepts:
TCP/IP Suite: The most widely used set of protocols, forming the basis of the internet. Includes TCP, UDP, IP,
HTTP, FTP, etc.
Layered Architecture: Protocols are organized into layers (e.g., OSI model, TCP/IP model), with each layer
providing services to the layer above it.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Not knowing which protocols operate at which layer or their specific functions.
Technique: Create a mental map or table of protocols and their corresponding layers/functions.
Network Switching
Network switching refers to the mechanisms used to establish connections between communicating devices in a
network. Different switching techniques have varying characteristics regarding resource allocation and delay.

*(PDF Page 104)*

Key Concepts:
Circuit Switching: A dedicated end-to-end communication path (circuit) is established before data transfer and
maintained for the duration of the communication (e.g., traditional telephone networks). Guarantees bandwidth.
Packet Switching: Data is broken into small, independent packets, each routed individually through the network. No
dedicated path. More efficient use of bandwidth, but variable delay (e.g., Internet).
Message Switching: Entire messages are stored and forwarded at each intermediate node. No dedicated path.
High delay.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing the characteristics of circuit vs. packet switching, especially regarding setup time, resource
reservation, and delay.
Technique: Understand the trade-offs: Circuit switching for guaranteed QoS, Packet switching for efficiency and
flexibility.
OSI Model
The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a
telecommunication or computing system into seven distinct layers. It helps in understanding network architecture and
troubleshooting.
Key Concepts:
1. Physical Layer (Layer 1): Deals with the physical transmission of raw bits over a medium (cables, connectors,
voltage levels). PDU: Bit.
2. Data Link Layer (Layer 2): Provides reliable data transfer between adjacent nodes, framing, MAC addressing, error
detection/correction. PDU: Frame.
3. Network Layer (Layer 3): Handles logical addressing (IP), routing, and forwarding packets across networks. PDU:
Packet/Datagram.
4. Transport Layer (Layer 4): Provides end-to-end communication, reliability (TCP), flow control, congestion control,
port addressing. PDU: Segment (TCP), Datagram (UDP).
5. Session Layer (Layer 5): Manages communication sessions, synchronization, dialog control.
6. Presentation Layer (Layer 6): Handles data representation, encryption, decryption, compression.
7. Application Layer (Layer 7): Provides network services directly to user applications (HTTP, FTP, DNS). PDU:
Data/Message.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Forgetting the order of layers or the primary function/PDU of each layer.
Technique: Use mnemonics (e.g.,
"Please Do Not Throw Sausage Pizza Away") to remember the order. Focus on
the first four layers, as they are most frequently tested.
Probability
Probability theory is used in computer networks to model and analyze the performance of random access protocols (like
Aloha) and to evaluate network reliability and queueing behavior.
Key Concepts:
Poisson Distribution: Often used to model arrival rates of packets or frames in random access protocols.
Throughput: The rate at which successful transmissions occur.
Offered Load (G): The total number of frames generated per unit of time, including retransmissions.
Important Formulas and Results:
(See Pure Aloha, Slotted Aloha for specific probability-based throughput formulas).
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Misinterpreting the meaning of offered load (G) vs. throughput (S).

*(PDF Page 105)*

Technique: Understand the assumptions behind probabilistic models (e.g., Poisson arrivals, infinite number of
users).
Pure Aloha
Pure Aloha is a simple random access MAC protocol where stations transmit frames whenever they have data. If a
collision occurs, the stations wait a random amount of time and retransmit.
Important Formulas and Results:
Throughput (S): The rate of successful transmissions.
where is the offered load (total number of frames generated per frame transmission time, including
retransmissions).
Maximum Throughput ( ): Occurs when .
Key Properties and Identities:
Collision window is .
Highly inefficient due to frequent collisions.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Forgetting the factor of 2G in the exponent for pure Aloha.
Technique: Understand the concept of the vulnerability period for collisions.
Routing
Routing is the process of selecting paths in a network along which to send network traffic. It involves determining the
best route for packets from a source to a destination.
Key Concepts:
Static Routing: Routes are manually configured by an administrator. Simple for small networks.
Dynamic Routing: Routers exchange routing information and update their tables automatically using routing
protocols. Adaptable to network changes.
Routing Table: A table stored in a router that maps destination network addresses to the next hop router and
outgoing interface.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing routing (path selection) with forwarding (packet movement).
Technique: Understand how a router uses its routing table to make forwarding decisions.
Routing Protocols
Routing protocols are the algorithms and rules that routers use to exchange routing information and build their routing
tables. They are classified by their operating scope and algorithm type.
Key Concepts:
Interior Gateway Protocols (IGPs): Used within an Autonomous System (AS).
RIP (Routing Information Protocol): Distance Vector, uses hop count as metric, max 15 hops.
OSPF (Open Shortest Path First): Link State, uses Dijkstra's algorithm, builds a complete topology map.
Exterior Gateway Protocols (EGPs): Used between Autonomous Systems.
BGP (Border Gateway Protocol): Path Vector, used for inter-domain routing on the Internet.

*(PDF Page 106)*

Link State vs. Distance Vector:
Distance Vector: Routers share their entire routing tables with neighbors. (e.g., RIP)
Link State: Routers share information about their directly connected links with all other routers in the AS. (e.g.,
OSPF)
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing RIP with OSPF, or IGPs with EGPs.
Technique: Know the key characteristics of each protocol (metric, algorithm type, scope). Practice Dijkstra's
algorithm for OSPF-like problems.
Sliding Window
Sliding Window protocols are flow control mechanisms that allow a sender to transmit multiple frames before receiving
an acknowledgment, improving channel utilization. They use a window of sequence numbers.
Important Formulas and Results:
Window Size (W): The maximum number of unacknowledged frames a sender can transmit.
Sequence Number Bits (n): For a window size , the minimum number of bits required for sequence numbers
depends on the protocol.
Go-Back-N: Sender window , Receiver window . Sequence numbers range from 0 to .
.
Selective Repeat: Sender window , Receiver window . .
Channel Utilization (U) for Sliding Window:
where .
Key Properties and Identities:
Go-Back-N (GBN): If a frame is lost, the sender retransmits that frame and all subsequent frames already sent.
Receiver discards out-of-order frames.
Selective Repeat (SR): If a frame is lost, only that specific frame is retransmitted. Receiver buffers out-of-order
frames. More efficient but complex.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly determining the maximum window size for Go-Back-N vs. Selective Repeat for a given number of
sequence bits.
Technique: Memorize the window size rules for GBN and SR. Practice calculating utilization with different window
sizes and values.
Slotted Aloha
Slotted Aloha is an improvement over Pure Aloha where time is divided into discrete slots. Stations are only allowed to
transmit at the beginning of a slot, reducing the collision window.
Important Formulas and Results:
Throughput (S):
where is the offered load.
Maximum Throughput ( ): Occurs when .

*(PDF Page 107)*

Key Properties and Identities:
Collision window is .
Requires global time synchronization.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing the throughput formula with Pure Aloha (exponent is -G, not -2G).
Technique: Understand how slotting reduces the vulnerability period for collisions.
Sockets
Sockets provide an Application Programming Interface (API) for network communication, allowing applications to send
and receive data over a network. They are the endpoints of communication.
Key Concepts:
Socket Types:
Stream Sockets (TCP): Connection-oriented, reliable, ordered data delivery.
Datagram Sockets (UDP): Connectionless, unreliable, unordered data delivery.
Common Socket Functions (for TCP server): socket(), bind(), listen(), accept(), send(), recv(), close().
Common Socket Functions (for TCP client): socket(), connect(), send(), recv(), close().
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing the sequence of system calls for client vs. server, or for TCP vs. UDP.
Technique: Memorize the typical sequence of socket calls for both client and server applications.
Stop and Wait
Stop and Wait is the simplest ARQ (Automatic Repeat Request) protocol for reliable data transfer. The sender transmits
one frame and waits for an acknowledgment (ACK) before sending the next.
Important Formulas and Results:
Transmission Time ( ): Time to put the entire frame on the link.
Propagation Delay ( ): Time for the first bit to travel from sender to receiver.
Dimensionless Parameter ( ): Ratio of propagation delay to transmission time.
Channel Utilization (Efficiency) ( ):
This assumes no errors and negligible ACK transmission time.
Key Properties and Identities:

*(PDF Page 108)*

Sender window size = 1, Receiver window size = 1.
Uses 1-bit sequence numbers (0 and 1).
Low utilization for high bandwidth-delay product links.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Forgetting to multiply formula.
by 2 for the round-trip propagation delay in the denominator of the utilization
Technique: Always calculate and first, then , then . Pay attention to units.
Subnetting
Subnetting is the process of dividing a larger IP network into smaller, more manageable subnetworks (subnets). It
improves network efficiency, security, and reduces broadcast traffic.
Important Formulas and Results:
Number of Subnets: If bits are borrowed from the host portion of the IP address to create subnets, the number of
subnets created is .
Number of Usable Hosts per Subnet: If bits remain for host IDs in a subnet, the number of usable hosts is
(excluding the network and broadcast addresses for that subnet).
Subnet Mask: A 32-bit number that distinguishes the network portion from the host portion of an IP address. All
network/subnet bits are 1, all host bits are 0.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Incorrectly identifying the network ID, broadcast ID, or valid host range for a given IP address and subnet
mask.
Technique: Convert IP addresses and subnet masks to binary. Draw out the network, subnet, and host portions.
Practice finding the first/last usable IP.
TCP (Transmission Control Protocol)
TCP is a reliable, connection-oriented, byte-stream Transport Layer protocol. It provides error control, flow control, and
congestion control, making it suitable for applications requiring high data integrity.
Key Concepts:
Connection-Oriented: Establishes a connection using a 3-way handshake before data transfer.
Reliable: Uses sequence numbers, acknowledgments (ACKs), and retransmissions to ensure all data arrives
correctly.
Flow Control: Prevents a fast sender from overwhelming a slow receiver using a receive window (rwnd).
Congestion Control: Prevents network congestion (see Congestion Control topic).
Full-Duplex: Data can flow in both directions simultaneously.
Header Fields: Source/Destination Port, Sequence Number, Acknowledgment Number, Window Size, Checksum,
Flags (SYN, ACK, FIN, RST, PSH, URG).
Important Formulas and Results:
3-Way Handshake: SYN -> SYN+ACK -> ACK.
4-Way Handshake (Connection Termination): FIN -> ACK -> FIN -> ACK.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing sequence numbers with acknowledgment numbers, or the purpose of different TCP flags.
Technique: Trace the sequence and acknowledgment numbers during a TCP connection setup, data transfer, and
termination. Understand the role of the advertised window.
Token Bucket

*(PDF Page 109)*

The Token Bucket algorithm is a traffic shaping technique used to control the rate at which data is sent over a network.
It smooths out bursty traffic and enforces a maximum average rate.
Key Concepts:
Bucket Capacity (C): The maximum number of tokens the bucket can hold. Represents the maximum burst size
allowed.
Token Arrival Rate (r): The rate at which tokens are added to the bucket (e.g., tokens/second). Represents the
average allowed transmission rate.
Traffic Shaping: Packets can only be sent if there are enough tokens in the bucket. If not, packets are buffered or
dropped.
Important Formulas and Results:
Maximum Output Rate: Can be up to the link speed for a burst, but limited by the token rate Maximum Burst Size: Equal to the bucket capacity .
over time.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Confusing token bucket with leaky bucket. Token bucket allows bursts up to capacity, leaky bucket smooths
all traffic to a constant rate.
Technique: Calculate the maximum burst duration or the time it takes for the bucket to fill given a token rate and
capacity.
UDP (User Datagram Protocol)
UDP is a simple, connectionless, unreliable Transport Layer protocol. It provides minimal services, primarily
multiplexing/demultiplexing and basic error checking (optional checksum).
Key Concepts:
Connectionless: No connection setup or teardown.
Unreliable: No guarantees of delivery, order, or duplicate protection.
No Flow Control, No Congestion Control: Applications must handle these if needed.
Header Fields: Source Port, Destination Port, Length, Checksum (optional).
Key Properties and Identities:
Lower overhead and faster than TCP.
Suitable for applications where speed is more critical than reliability (e.g., streaming media, DNS, VoIP).
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Attributing TCP features (reliability, flow control) to UDP.
Technique: Understand the trade-offs between UDP and TCP and identify appropriate applications for each.
Wrap Around Time
Wrap Around Time (WAT) refers to the time it takes for the sequence numbers used in a protocol (like TCP) to cycle
through all possible values and return to the starting point. It's crucial for preventing ambiguity when old segments with
duplicate sequence numbers arrive late.
Important Formulas and Results:
If sequence numbers are in bytes and is the number of bits for the sequence number field:

*(PDF Page 110)*

(This formula might vary based on how sequence numbers are defined, e.g., per byte or per segment).
A simpler form often seen:
Key Properties and Identities:
WAT should ideally be greater than the maximum segment lifetime (MSL) to prevent old segments from being
misinterpreted.
For TCP, the sequence number field is 32 bits.
Common Pitfalls and Problem-Solving Techniques:
Pitfall: Forgetting to account for the units of sequence numbers (bytes vs. segments) and bandwidth.
Technique: Ensure consistent units. Understand the relationship between WAT and MSL.
Quick Formula Reference
Channel Utilization & Throughput:
Stop-and-Wait ARQ: where
Sliding Window ARQ (Go-Back-N/Selective Repeat):
Pure Aloha Throughput: (Max at )
Slotted Aloha Throughput: (Max at )
Transmission Time:
Propagation Delay:
Error Detection & Correction:
Hamming Code Parity Bits:
CRC Codeword:
MAC Protocols:
CSMA/CD Slot Time:
CSMA/CD Minimum Frame Size:
IP Fragmentation:
Fragment Offset: (in 8-byte units)
IP Addressing & Subnetting:
Usable Hosts: (where is host bits)
Number of Subnets: (where is subnet bits)
Sliding Window Sequence Numbers:
Go-Back-N Sender Window : (where is sequence number bits)
Selective Repeat Sender/Receiver Window :
Wrap Around Time:
WAT (bytes): (where is sequence number bits)
Important Tips for GATE

*(PDF Page 111)*

1. Master OSI/TCP-IP Layers: Understand the function of each layer, the protocols operating at each layer, and the
PDU (Protocol Data Unit) names. This is foundational and frequently tested.
2. Practice Numerical Problems Extensively: Focus on channel utilization, throughput, propagation/transmission
delay calculations, IP addressing, subnetting, and fragmentation. Pay close attention to units (bits vs. bytes, Mbps
vs. Kbps, ms vs. seconds).
3. Differentiate Flow Control vs. Congestion Control: Understand their distinct goals, mechanisms, and the
protocols that implement them (e.g., TCP's window mechanisms for both).
4. Know Protocol Headers: Be familiar with the key fields in Ethernet, IP, TCP, and UDP headers. Questions often
test the purpose or size of specific fields.
5. Understand ARQ Protocols: Clearly distinguish Stop-and-Wait, Go-Back-N, and Selective Repeat in terms of
window sizes, retransmission strategies, and efficiency.
6. Be Precise with IP Addressing and Subnetting: Convert to binary if needed. Don't confuse network ID, broadcast
ID, and usable host addresses. Practice CIDR notation.
7. Read Questions Carefully: Look for keywords like "negligible ACK time,
" "error-free channel,
" "half-duplex,
" or "full-
duplex" as they significantly impact formula application.
8. Time Management: Some numerical problems can be lengthy. If stuck, make an educated guess (if no negative
marking) or move on and return if time permits.
Application Layer Protocols (13)

---

## 4. Complete Question Index & Answer Key Record (226 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `2.1.1` | Application Layer Protocols: GATE CSE 2008 \| Question: 14, ISRO2016-74 | **A** |
| `2.1.2` | Application Layer Protocols: GATE CSE 2011 \| Question: 4 | **C** |
| `2.1.3` | Application Layer Protocols: GATE CSE 2012 \| Question: 10 | **C** |
| `2.1.4` | Application Layer Protocols: GATE CSE 2016 \| Set 1 \| Question: 25 | **C** |
| `2.1.5` | Application Layer Protocols: GATE CSE 2019 \| Question: 16 | **B** |
| `2.1.6` | Application Layer Protocols: GATE CSE 2020 \| Question: 25 | **6** |
| `2.1.7` | Application Layer Protocols: GATE CSE 2022 \| Question: 25 | **4** |
| `2.1.8` | Application Layer Protocols: GATE CSE 2026 \| Set 1 \| Question: 9 | **A;C;D** |
| `2.1.9` | Application Layer Protocols: GATE CSE 2026 \| Set 2 \| Question: 12 | **C** |
| `2.1.10` | Application Layer Protocols: GATE IT 2005 \| Question: 25 | **B** |
| `2.1.11` | Application Layer Protocols: GATE IT 2005 \| Question: 77 | **C** |
| `2.1.12` | Application Layer Protocols: GATE IT 2006 \| Question: 18 | **D** |
| `2.1.13` | Application Layer Protocols: GATE IT 2008 \| Question: 20 | **C** |
| `2.2.1` | Arp: GATE CSE 2025 \| Set 2 \| Question: 6 | **B** |
| `2.3.1` | Bit Stuffing: GATE CSE 2014 \| Set 3 \| Question: 24 | **B** |
| `2.3.2` | Bit Stuffing: GATE IT 2004 \| Question: 80 | **D** |
| `2.4.1` | Bridges: GATE CSE 2004 \| Question: 16 | **B** |
| `2.4.2` | Bridges: GATE CSE 2006 \| Question: 82 | **A** |
| `2.4.3` | Bridges: GATE CSE 2006 \| Question: 83 | **A** |
| `2.5.1` | CRC Polynomial: GATE CSE 2007 \| Question: 68, ISRO2016-73 | **B** |
| `2.5.2` | CRC Polynomial: GATE CSE 2017 \| Set 1 \| Question: 32 | **C** |
| `2.5.3` | CRC Polynomial: GATE CSE 2021 \| Set 2 \| Question: 34 | **C** |
| `2.5.4` | CRC Polynomial: GATE CSE 2026 \| Set 2 \| Question: 33 | **D** |
| `2.5.5` | CRC Polynomial: GATE IT 2005 \| Question: 78 | **A** |
| `2.6.1` | CSMA CD: GATE CSE 2015 \| Set 3 \| Question: 6 | **D** |
| `2.6.2` | CSMA CD: GATE CSE 2016 \| Set 2 \| Question: 53 | **200** |
| `2.6.3` | CSMA CD: GATE CSE 2018 \| Question: 55 | **50** |
| `2.6.4` | CSMA CD: GATE IT 2005 \| Question: 27 | **C** |
| `2.6.5` | CSMA CD: GATE IT 2005 \| Question: 71 | **A** |
| `2.6.6` | CSMA CD: GATE IT 2008 \| Question: 65 | **B** |
| `2.7.1` | Channel Utilization: GATE CSE 2025 \| Set 2 \| Question: 26 | **A** |
| `2.8.1` | Communication: GATE CSE 2012 \| Question: 44 | **A** |
| `2.8.2` | Communication: GATE CSE 2022 \| Question: 49 | **7.07:7.09** |
| `2.8.3` | Communication: GATE IT 2007 \| Question: 62 | **B** |
| `2.8.4` | Communication: GATE IT 2007 \| Question: 64 | **B** |
| `2.9.1` | Congestion Control: GATE CSE 2008 \| Question: 56 | **D** |
| `2.9.2` | Congestion Control: GATE CSE 2012 \| Question: 45 | **C** |
| `2.9.3` | Congestion Control: GATE CSE 2014 \| Set 1 \| Question: 27 | **1100** |
| `2.9.4` | Congestion Control: GATE CSE 2018 \| Question: 14 | **C** |
| `2.9.5` | Congestion Control: GATE CSE 2020 \| Question: 55 | **44** |
| `2.9.6` | Congestion Control: GATE CSE 2024 \| Set 2 \| Question: 44 | **4** |
| `2.9.7` | Congestion Control: GATE CSE 2026 \| Set 1 \| Question: 34 | **B** |
| `2.9.8` | Congestion Control: GATE CSE 2026 \| Set 2 \| Question: 48 | **4:4** |
| `2.9.9` | Congestion Control: GATE IT 2005 \| Question: 73 | **B** |
| `2.10.1` | Data Communication: GATE CSE 2026 \| Set 2 \| Question: 55 | **30:30** |
| `2.11.1` | Distance Vector Routing: GATE CSE 2010 \| Question: 54 | **C** |
| `2.11.2` | Distance Vector Routing: GATE CSE 2010 \| Question: 55 | **B** |
| `2.11.3` | Distance Vector Routing: GATE CSE 2011 \| Question: 52 | **A** |
| `2.11.4` | Distance Vector Routing: GATE CSE 2011 \| Question: 53 | **C** |
| `2.11.5` | Distance Vector Routing: GATE CSE 2021 \| Set 2 \| Question: 45 | **B;C** |
| `2.11.6` | Distance Vector Routing: GATE CSE 2022 \| Question: 47 | **0.5** |
| `2.11.7` | Distance Vector Routing: GATE IT 2005 \| Question: 29 | **B** |
| `2.11.8` | Distance Vector Routing: GATE IT 2007 \| Question: 60 | **A** |
| `2.12.1` | Error Detection: GATE CSE 1992 \| Question: 01,ii | **3** |
| `2.12.2` | Error Detection: GATE CSE 1995 \| Question: 1.12 | **A** |
| `2.12.3` | Error Detection: GATE CSE 2009 \| Question: 48 | **C** |
| `2.12.4` | Error Detection: GATE CSE 2017 \| Set 2 \| Question: 34 | **A** |
| `2.12.5` | Error Detection: GATE IT 2005 \| Question: 74 | **A** |
| `2.12.6` | Error Detection: GATE IT 2007 \| Question: 43 | **B** |
| `2.12.7` | Error Detection: GATE IT 2008 \| Question: 66 | **C** |
| `2.12.8` | Error Detection: GATE1987-2-i | **N/A** |
| `2.13.1` | Ethernet: GATE CSE 2004 \| Question: 54 | **B** |
| `2.13.2` | Ethernet: GATE CSE 2013 \| Question: 36 | **B** |
| `2.13.3` | Ethernet: GATE CSE 2016 \| Set 2 \| Question: 24 | **D** |
| `2.13.4` | Ethernet: GATE CSE 2022 \| Question: 12 | **C** |
| `2.13.5` | Ethernet: GATE CSE 2024 \| Set 2 \| Question: 13 | **B** |
| `2.13.6` | Ethernet: GATE CSE 2024 \| Set 2 \| Question: 45 | **500** |
| `2.13.7` | Ethernet: GATE IT 2006 \| Question: 19 | **C** |
| `2.14.1` | Fragmentation: GATE CSE 2004 \| Question: 56 | **D** |
| `2.14.2` | Fragmentation: GATE CSE 2004 \| Question: 57 | **B** |
| `2.14.3` | Fragmentation: GATE CSE 2013 \| Question: 37 | **C** |
| `2.14.4` | Fragmentation: GATE CSE 2025 \| Set 1 \| Question: 47 | **7:7** |
| `2.14.5` | Fragmentation: GATE CSE 2025 \| Set 2 \| Question: 13 | **D** |
| `2.15.1` | Hamming Code: GATE CSE 1994 \| Question: 9 | **N/A** |
| `2.15.2` | Hamming Code: GATE CSE 2021 \| Set 1 \| Question: 29 | **A** |
| `2.16.1` | IP Addressing: GATE CSE 2003 \| Question: 27 | **D** |
| `2.16.2` | IP Addressing: GATE CSE 2012 \| Question: 23 | **C** |
| `2.16.3` | IP Addressing: GATE CSE 2017 \| Set 2 \| Question: 20 | **9** |
| `2.16.4` | IP Addressing: GATE CSE 2018 \| Question: 54 | **144** |
| `2.16.5` | IP Addressing: GATE CSE 2023 \| Question: 42 | **C;D** |
| `2.16.6` | IP Addressing: GATE CSE 2024 \| Set 2 \| Question: 28 | **A** |
| `2.16.7` | IP Addressing: GATE CSE 2025 \| Set 2 \| Question: 8 | **D** |
| `2.16.8` | IP Addressing: GATE CSE 2026 \| Set 2 \| Question: 23 | **4094** |
| `2.17.1` | IP Packet: GATE CSE 2006 \| Question: 5 | **C** |
| `2.17.2` | IP Packet: GATE CSE 2010 \| Question: 15. PGEE 2018 | **D** |
| `2.17.3` | IP Packet: GATE CSE 2014 \| Set 3 \| Question: 25 | **D** |
| `2.17.4` | IP Packet: GATE CSE 2014 \| Set 3 \| Question: 28 | **A** |
| `2.17.5` | IP Packet: GATE CSE 2015 \| Set 1 \| Question: 22 | **B** |
| `2.17.6` | IP Packet: GATE CSE 2015 \| Set 2 \| Question: 52 | **C** |
| `2.17.7` | IP Packet: GATE CSE 2016 \| Set 1 \| Question: 53 | **13** |
| `2.17.8` | IP Packet: GATE CSE 2024 \| Set 1 \| Question: 21 | **A;C** |
| `2.17.9` | IP Packet: GATE CSE 2024 \| Set 1 \| Question: 55 | **6** |
| `2.17.10` | IP Packet: GATE CSE 2024 \| Set 2 \| Question: 18 | **B;C** |
| `2.17.11` | IP Packet: GATE CSE 2024 \| Set 2 \| Question: 22 | **C;D** |
| `2.17.12` | IP Packet: GATE IT 2004 \| Question: 86 | **D** |
| `2.18.1` | Icmp: GATE IT 2005 \| Question: 26 | **A** |
| `2.19.1` | LAN Technologies: GATE CSE 2003 \| Question: 83 | **D** |
| `2.19.2` | LAN Technologies: GATE CSE 2007 \| Question: 65 | **A** |
| `2.19.3` | LAN Technologies: GATE CSE 2014 \| Set 2 \| Question: 25 | **26** |
| `2.19.4` | LAN Technologies: GATE CSE 2019 \| Question: 49 | **3** |
| `2.19.5` | LAN Technologies: GATE IT 2004 \| Question: 27 | **D** |
| `2.19.6` | LAN Technologies: GATE IT 2005 \| Question: 28 | **D** |
| `2.19.7` | LAN Technologies: GATE IT 2006 \| Question: 66 | **B** |
| `2.20.1` | MAC Protocol: GATE CSE 2005 \| Question: 74 | **D** |
| `2.20.2` | MAC Protocol: GATE CSE 2015 \| Set 2 \| Question: 8 | **12** |
| `2.20.3` | MAC Protocol: GATE IT 2004 \| Question: 85 | **B** |
| `2.20.4` | MAC Protocol: GATE IT 2005 \| Question: 75 | **C** |
| `2.21.1` | Network Flow: GATE CSE 1992 \| Question: 01,v | **N/A** |
| `2.21.2` | Network Flow: GATE CSE 2017 \| Set 2 \| Question: 35 | **D** |
| `2.21.3` | Network Flow: GATE IT 2004 \| Question: 87 | **C** |
| `2.21.4` | Network Flow: GATE IT 2006 \| Question: 67 | **A** |
| `2.22.1` | Network Layer: GATE CSE 2003 \| Question: 28 | **D** |
| `2.22.2` | Network Layer: GATE CSE 2004 \| Question: 15 | **A** |
| `2.22.3` | Network Layer: GATE CSE 2013 \| Question: 14 | **C** |
| `2.22.4` | Network Layer: GATE CSE 2014 \| Set 3 \| Question: 23 | **B** |
| `2.22.5` | Network Layer: GATE CSE 2018 \| Question: 13 | **C** |
| `2.22.6` | Network Layer: GATE CSE 2026 \| Set 1 \| Question: 46 | **A;B;C** |
| `2.23.1` | Network Protocols: GATE CSE 2005 \| Question: 24 | **D** |
| `2.23.2` | Network Protocols: GATE CSE 2007 \| Question: 20 | **C** |
| `2.23.3` | Match the following: | **B** |
| `2.23.4` | Network Protocols: GATE CSE 2015 \| Set 1 \| Question: 17 | **A** |
| `2.23.5` | Network Protocols: GATE CSE 2016 \| Set 1 \| Question: 24 | **C** |
| `2.23.6` | Network Protocols: GATE CSE 2019 \| Question: 29 | **C** |
| `2.23.7` | Network Protocols: GATE CSE 2021 \| Set 1 \| Question: 49 | **50** |
| `2.23.8` | Network Protocols: GATE CSE 2021 \| Set 1 \| Question: 8 | **C** |
| `2.23.9` | Network Protocols: GATE CSE 2024 \| Set 1 \| Question: 6 | **C** |
| `2.23.10` | Network Protocols: GATE IT 2007 \| Question: 69 | **D** |
| `2.23.11` | Network Protocols: GATE IT 2008 \| Question: 68 | **B** |
| `2.24.1` | Network Switching: GATE CSE 2005 \| Question: 73 | **D** |
| `2.24.2` | Network Switching: GATE CSE 2014 \| Set 2 \| Question: 26 | **D** |
| `2.24.3` | Network Switching: GATE CSE 2015 \| Set 3 \| Question: 36 | **1575** |
| `2.24.4` | Network Switching: GATE IT 2004 \| Question: 22 | **B** |
| `2.25.1` | Osi Model: GATE CSE 2025 \| Set 1 \| Question: 6 | **B** |
| `2.26.1` | Probability: GATE CSE 2025 \| Set 1 \| Question: 46 | **0.949:0.952** |
| `2.27.1` | Pure Aloha: GATE CSE 2021 \| Set 2 \| Question: 54 | **130** |
| `2.28.1` | Routing: GATE CSE 2005 \| Question: 26 | **B** |
| `2.28.2` | Routing: GATE CSE 2014 \| Set 1 \| Question: 23 | **D** |
| `2.28.3` | Routing: GATE CSE 2014 \| Set 2 \| Question: 23 | **A** |
| `2.28.4` | Routing: GATE CSE 2014 \| Set 3 \| Question: 26 | **1** |
| `2.28.5` | Routing: GATE CSE 2017 \| Set 2 \| Question: 09 | **C** |
| `2.28.6` | Routing: GATE CSE 2020 \| Question: 15 | **D** |
| `2.28.7` | Routing: GATE CSE 2023 \| Question: 15 | **A;C** |
| `2.28.8` | Routing: GATE CSE 2024 \| Set 1 \| Question: 26 | **B** |
| `2.28.9` | Routing: GATE CSE 2024 \| Set 1 \| Question: 48 | **40** |
| `2.28.10` | Routing: GATE CSE 2026 \| Set 2 \| Question: 11 | **B** |
| `2.28.11` | Routing: GATE IT 2005 \| Question: 85a | **C** |
| `2.28.12` | Routing: GATE IT 2005 \| Question: 85b | **A** |
| `2.28.13` | Routing: GATE IT 2007 \| Question: 63 | **C** |
| `2.28.14` | Routing: GATE IT 2008 \| Question: 67 | **D** |
| `2.29.1` | B. S1, S3 and S4 only C. S2 and S3 only D. S1 and S4 only | **A** |
| `2.30.1` | Sliding Window: GATE CSE 2003 \| Question: 84 | **B** |
| `2.30.2` | Sliding Window: GATE CSE 2005 \| Question: 25 | **B** |
| `2.30.3` | Sliding Window: GATE CSE 2006 \| Question: 44 | **B** |
| `2.30.4` | Sliding Window: GATE CSE 2006 \| Question: 46 | **C** |
| `2.30.5` | Sliding Window: GATE CSE 2007 \| Question: 69 | **C** |
| `2.30.6` | Sliding Window: GATE CSE 2009 \| Question: 57, ISRO2016-75 | **D** |
| `2.30.7` | Sliding Window: GATE CSE 2009 \| Question: 58 | **C** |
| `2.30.8` | Sliding Window: GATE CSE 2014 \| Set 1 \| Question: 28 | **5** |
| `2.30.9` | Sliding Window: GATE CSE 2015 \| Set 3 \| Question: 28 | **8** |
| `2.30.10` | Sliding Window: GATE CSE 2016 \| Set 2 \| Question: 55 | **4** |
| `2.30.11` | Sliding Window: GATE CSE 2026 \| Set 1 \| Question: 35 | **B** |
| `2.30.12` | Sliding Window: GATE IT 2004 \| Question: 81 | **C** |
| `2.30.13` | Sliding Window: GATE IT 2004 \| Question: 83 | **B** |
| `2.30.14` | Sliding Window: GATE IT 2004 \| Question: 88 | **B** |
| `2.30.15` | Sliding Window: GATE IT 2006 \| Question: 64 | **A** |
| `2.30.16` | Sliding Window: GATE IT 2008 \| Question: 64 | **A** |
| `2.31.1` | Slotted Aloha: GATE CSE 2015 \| Set 1 \| Question: 29 | **0.4404** |
| `2.32.1` | Sockets: GATE CSE 2008 \| Question: 17 | **D** |
| `2.32.2` | Sockets: GATE CSE 2008 \| Question: 59 | **C** |
| `2.32.3` | Sockets: GATE CSE 2014 \| Set 2 \| Question: 24 | **C** |
| `2.32.4` | Sockets: GATE CSE 2015 \| Set 2 \| Question: 20 | **B** |
| `2.33.1` | Stop and Wait: GATE CSE 2015 \| Set 1 \| Question: 53 | **320** |
| `2.33.2` | Stop and Wait: GATE CSE 2016 \| Set 1 \| Question: 55 | **2500** |
| `2.33.3` | Stop and Wait: GATE CSE 2017 \| Set 1 \| Question: 45 | **86.5** |
| `2.33.4` | Stop and Wait: GATE CSE 2023 \| Question: 7 | **B** |
| `2.33.5` | Stop and Wait: GATE IT 2005 \| Question: 72 | **D** |
| `2.33.6` | Stop and Wait: GATE IT 2006 \| Question: 68 | **B** |
| `2.34.1` | Subnetting: GATE CSE 2003 \| Question: 82, ISRO2009-1 | **D** |
| `2.34.2` | Subnetting: GATE CSE 2004 \| Question: 55 | **A** |
| `2.34.3` | Subnetting: GATE CSE 2005 \| Question: 27 | **D** |
| `2.34.4` | Subnetting: GATE CSE 2006 \| Question: 45 | **C** |
| `2.34.5` | Subnetting: GATE CSE 2007 \| Question: 67, ISRO2016-72 | **C** |
| `2.34.6` | Subnetting: GATE CSE 2008 \| Question: 57 | **C** |
| `2.34.7` | Subnetting: GATE CSE 2010 \| Question: 47 | **D** |
| `2.34.8` | Subnetting: GATE CSE 2012 \| Question: 34, ISRO-DEC2017-32 | **A** |
| `2.34.9` | Subnetting: GATE CSE 2015 \| Set 2 \| Question: 41 | **A** |
| `2.34.10` | Subnetting: GATE CSE 2015 \| Set 3 \| Question: 38 | **158** |
| `2.34.11` | Subnetting: GATE CSE 2019 \| Question: 28 | **C** |
| `2.34.12` | Subnetting: GATE CSE 2020 \| Question: 38 | **B** |
| `2.34.13` | Subnetting: GATE CSE 2022 \| Question: 45 | **B;D** |
| `2.34.14` | Subnetting: GATE CSE 2023 \| Question: 55 | **3** |
| `2.34.15` | Subnetting: GATE CSE 2025 \| Set 1 \| Question: 30 | **A** |
| `2.34.16` | Subnetting: GATE IT 2004 \| Question: 26 | **C** |
| `2.34.17` | Subnetting: GATE IT 2005 \| Question: 76 | **D** |
| `2.34.18` | Subnetting: GATE IT 2006 \| Question: 63, ISRO2015-57 | **C** |
| `2.34.19` | Subnetting: GATE IT 2006 \| Question: 70 | **D** |
| `2.34.20` | Subnetting: GATE IT 2008 \| Question: 84 | **C** |
| `2.34.21` | Subnetting: GATE IT 2008 \| Question: 85 | **B** |
| `2.35.1` | TCP: GATE CSE 2009 \| Question: 47 | **A** |
| `2.35.2` | TCP: GATE CSE 2012 \| Question: 22 | **C** |
| `2.35.3` | TCP: GATE CSE 2015 \| Set 1 \| Question: 19 | **B** |
| `2.35.4` | TCP: GATE CSE 2015 \| Set 2 \| Question: 34 | **C** |
| `2.35.5` | TCP: GATE CSE 2015 \| Set 3 \| Question: 22 | **A** |
| `2.35.6` | TCP: GATE CSE 2016 \| Set 2 \| Question: 25 | **C** |
| `2.35.7` | TCP: GATE CSE 2017 \| Set 1 \| Question: 14 | **D** |
| `2.35.8` | TCP: GATE CSE 2021 \| Set 1 \| Question: 44 | **A;B;C** |
| `2.35.9` | TCP: GATE CSE 2021 \| Set 1 \| Question: 45 | **A;C** |
| `2.35.10` | TCP: GATE CSE 2021 \| Set 2 \| Question: 7 | **C** |
| `2.35.11` | TCP: GATE CSE 2022 \| Question: 50 | **33** |
| `2.35.12` | TCP: GATE CSE 2023 \| Question: 40 | **B;C;D** |
| `2.35.13` | TCP: GATE CSE 2024 \| Set 1 \| Question: 19 | **A;D** |
| `2.35.14` | TCP: GATE CSE 2025 \| Set 1 \| Question: 12 | **B;D** |
| `2.35.15` | TCP: GATE CSE 2026 \| Set 1 \| Question: 8 | **D** |
| `2.35.16` | TCP: GATE IT 2004 \| Question: 23 | **A** |
| `2.35.17` | TCP: GATE IT 2004 \| Question: 28 | **A** |
| `2.35.18` | TCP: GATE IT 2007 \| Question: 13 | **B** |
| `2.35.19` | TCP: GATE IT 2007 \| Question: 14 | **D** |
| `2.35.20` | TCP: GATE IT 2008 \| Question: 69 | **B** |
| `2.36.1` | Token Bucket: GATE CSE 2008 \| Question: 58 | **B** |
| `2.36.2` | Token Bucket: GATE CSE 2016 \| Set 1 \| Question: 54 | **1.10:1.19** |
| `2.37.1` | UDP: GATE CSE 2005 \| Question: 23 | **B** |
| `2.37.2` | UDP: GATE CSE 2013 \| Question: 12 | **C** |
| `2.37.3` | UDP: GATE CSE 2017 \| Set 2 \| Question: 18 | **B** |
| `2.37.4` | UDP: GATE IT 2006 \| Question: 69 | **D** |
| `2.38.1` | Wrap Around Time: GATE CSE 2014 \| Set 3 \| Question: 27 | **256** |
| `2.38.2` | Wrap Around Time: GATE CSE 2018 \| Question: 25 | **34** |

