
## 📊 Layer 4 vs Layer 7 Load Balancer Comparison
| Feature                         | Layer 4 Load Balancer                             | Layer 7 Load Balancer                                |
|----------------------------------|----------------------------------------------------|--------------------------------------------------------|
| **OSI Layer**                   | Layer 4 (Transport Layer)                         | Layer 7 (Application Layer)                            |
| **Protocols Handled**          | TCP, UDP                                          | HTTP, HTTPS, WebSockets, gRPC                          |
| **Routing Criteria**           | IP address, TCP/UDP port                          | URL path, HTTP headers, cookies, query params          |
| **Content Awareness**          | ❌ No (Blind to application data)                 | ✅ Yes (Understands application-level data)            |
| **Speed / Performance**        | ✅ Faster (lower overhead)                        | ❌ Slightly slower (due to inspection/parsing)         |
| **SSL Termination**            | ❌ Rarely supported                               | ✅ Commonly supported                                  |
| **Advanced Features**          | ❌ Basic traffic distribution                     | ✅ Auth, rate limiting, A/B testing, redirects         |
| **Sticky Sessions**            | ⚠️ Requires IP hash or source port                | ✅ Can use cookies/session data                        |
| **Use Case Example**           | Load balancing TCP services (DB, SMTP, etc.)      | HTTP APIs, Web apps, microservices routing             |
| **Popular Tools**              | HAProxy (L4), AWS NLB, Envoy (L4 mode)            | NGINX, AWS ALB, Traefik, Istio, Envoy (L7 mode)        |

## 🔍 Quick Summary

-   Use **Layer 4** when you want **fast, protocol-level routing** without inspecting traffic content (e.g., DB connections, low-latency services).
    
-   Use **Layer 7** when you need **smart, content-aware routing** (e.g., API gateway, microservices, user-based routing).

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
eyJoaXN0b3J5IjpbLTg3Njg1NTA3MCwxMTgwMjg4MzA0XX0=
-->