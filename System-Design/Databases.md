### When to Denormalize?

It makes sense in cases like:

-   **OLAP (analytics/reporting)** where performance > consistency.
    
-   Data is **mostly read-only**, or changes **rarely**.
    
-   You're building a **data warehouse**, not a transactional system.
    

But for **OLTP (transactional systems)**, normalization is the safer route.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMjI4MDY0MjJdfQ==
-->