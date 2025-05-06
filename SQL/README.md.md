### ✅ **One-to-One Relationship: Key Notes**

1.  **UNIQUE Constraint is Essential**
    
    -   To enforce **true one-to-one**, the foreign key in the **dependent table** must have a `UNIQUE` constraint.
        
    -   Without it, the relationship becomes **one-to-many**.
        
2.  **NOT NULL is Optional — Depends on Use Case**
    
    -   If the foreign key **is NOT NULL**, the relationship is **strict one-to-one** (i.e., every dependent must have a corresponding parent).
        
    -   If the foreign key **is nullable**, the relationship becomes **zero-or-one-to-one**, meaning the dependent can exist without a parent — depending on your business rules.
        

----------

### 🎯 Quick Example:

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE user_profiles (
    profile_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNIQUE NOT NULL,  -- Enforces strict 1:1
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

```

Or:

```sql
user_id INT UNIQUE  -- allows a profile to exist without linking to a user (0 or 1:1)

```

----------



## JOINS

1. Inner Join (Join)
2. Left Join
3. Right Join
4. Full Outer Join
5. Cross Join
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjIzNTA1MTExLDUxMzkwMDIwN119
-->