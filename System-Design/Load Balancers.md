
## Load Balancing Algorithms

| Algorithm                  | Strategy                      | Pros                                                                 | Cons                                                                | Best Use Cases                                |
|---------------------------|-------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------|
| **Round Robin**           | Rotate requests in sequence   | ✅ Simple, fair if all equal                                         | ❌ Ignores server load                                              | Equal servers, stateless apps                 |
| **Weighted Round Robin**  | Round Robin + weight          | ✅ Supports unequal servers                                          | ❌ Static weights, not dynamic                                       | Mixed-capacity servers                        |
| **Least Connections**     | Fewest active connections     | ✅ Load-aware, good for variable traffic                             | ❌ Slightly complex, load can still vary                             | E-commerce, long-lived connections            |
| **Weighted Least Conn.**  | Least Conn. + weight          | ✅ Adaptive + capacity-aware                                         | ❌ Higher overhead, needs monitoring                                 | Auto-scaling backends, API gateways           |
| **IP Hash**               | Based on client IP            | ✅ Sticky sessions without cookies                                   | ❌ Poor distribution with NAT/VPN                                    | Session-based apps, small clusters            |
| **Random (2 choices)**    | Random + compare 2 servers    | ✅ Almost Least Conn., simpler logic                                | ❌ Still pseudo-random                                               | Large-scale systems, stateless apps           |
| **Consistent Hashing**    | Hash-based (usually keys)     | ✅ Low churn on server change, ideal for sharding                    | ❌ Complex setup, not ideal for generic traffic                      | Caches, databases, microservices routing      |
| **Sticky Sessions**       | Same client ↔ same server     | ✅ Maintains session state                                           | ❌ Poor fault tolerance, uneven load                                 | No session externalization                    |
| **Geo-based (GeoDNS)**    | Route by client location       | ✅ Reduces latency, CDN-friendly                                     | ❌ Ignores load, not always accurate                                 | Global apps, CDNs, regional failover          |

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE4MDI4ODMwNF19
-->