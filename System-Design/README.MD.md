## Data Storage Units and Scales

```
This spreadsheet defines computer storage units and their sizes. It contains the following fields:

| Unit        | Abbreviation | Approximate Size (Bytes)      | Exact Size (Bytes) | Example                                              |
| :---------- | :----------- | :---------------------------- | :----------------- | :--------------------------------------------------- |
| Bit         | b            | 1 or 0 (binary digit)         | 1 bit              | Smallest unit of data                                |
| Byte        | B            | 8 bits                        | 8 bits             | A single character (e.g., 'a', '1', '$')            |
| Kilobyte    | KB           | 103 bytes (1,000)             | 210 (1,024)        | A few paragraphs of text                             |
| Megabyte    | MB           | 106 bytes (1,000,000)         | 220 (1,048,576)    | A high-quality photo, a few minutes of MP3 audio      |
| Gigabyte    | GB           | 109 bytes                     | 230                | A typical movie, thousands of photos                  |
| Terabyte    | TB           | 1012 bytes                    | 240                | Thousands of movies, many personal hard drives        |
| Petabyte    | PB           | 1015 bytes                    | 250                | Large data centers, all user photos on Facebook       |
| Exabyte     | EB           | 1018 bytes                    | 260                | Estimated global internet traffic per month           |
| Zettabyte   | ZB           | 1021 bytes                    | 270                | All digital data in existence (as of 2010 est.)      |
| Yottabyte   | YB           | 1024 bytes                    | 280                | Beyond current practical storage scales               |

-   **Unit:** The name of the storage unit.
-   **Abbreviation:** The abbreviation used for each unit.
-   **Approximate Size (Bytes):** The approximate size of the unit in bytes.
-   **Exact Size (Bytes):** The exact size of the unit in bytes.
-   **Example:** An example to help understand the scale of each unit.
```

## Latency Numbers
```
| Operation                                 | Approximate Latency |
| :---------------------------------------: | :-----------------: |
| L1 cache reference                        | 0.5 ns              |
| L2 cache reference                        | 7 ns                |
| Mutex lock/unlock                         | 25 ns               |
| Main memory reference                     | 100 ns              |
| Compress 1KB with Zippy                   | 3 µs (3,000 ns)     |
| Send 1KB over 1 Gbps network              | 10 µs (10,000 ns)   |
| SSD random read                           | 150 µs (150,000 ns) |
| Read 1 MB sequentially from memory        | 250 µs (250,000 ns) |
| Round trip within same datacenter         | 0.5 ms (500,000 ns) |
| Read 1 MB sequentially from SSD           | 1 ms (1,000,000 ns) |
| Disk seek (spinning disk)                 | 10 ms               |
| Read 1 MB sequentially from spinning disk | 20 ms               |
| Send packet from CA to Netherlands (RTT)  | 150 ms              |
| Human blink                               | 100 ms              |
```

## Data Transfer Rates (Bandwidth Examples)
```
| Medium/Interface         | Typical Speed (Approximate) |
| :----------------------: | :-------------------------: |
| Gigabit Ethernet         | 1 Gbps (125 MB/s)           |
| 10 Gigabit Ethernet      | 10 Gbps (1.25 GB/s)         |
| SATA III SSD             | \~500-600 MB/s              |
| NVMe SSD (PCIe Gen3 x4)  | \~3.5 GB/s                  |
| NVMe SSD (PCIe Gen4 x4)  | \~7 GB/s                    |
| USB 3.0                  | 5 Gbps (640 MB/s)           |
| USB 3.1                  | 10 Gbps (1.2 GB/s)          |
| Wi-Fi (802.11ac/Wi-Fi 5) | Up to \~1.3 Gbps            |
| Wi-Fi (802.11ax/Wi-Fi 6) | Up to \~9.6 Gbps            |
| Typical Home Broadband   | 100 Mbps - 1 Gbps           |
| Mobile 5G                | 100 Mbps - 10 Gbps          |
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExMzA1NjY2MiwxODI4MTgxMTIsLTEwOT
Y5NTk0NV19
-->