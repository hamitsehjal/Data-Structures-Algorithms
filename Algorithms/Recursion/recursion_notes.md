# Recursion

> Leigh Caldwell on StackOverflow:
> "Loops may achieve performance gain for your program. Recursion may achieve a performance gain for your programmer. Choose which is more important in your situation."

- Recursion is used when it makes the solution clearer.
- There's no performance benefit to using recursion; in fact, loops are sometimes better for performance.
- With recursion, you learn how to break a problem down into a base case and a recursive case.
- Every recursive function has two parts:
  - Base case (when the function doesn't call itself).
  - Recursive case (when the function calls itself).

**Most Important:** When you write a recursive function, you NEED TO TELL it when to STOP!!

## Stack
- Data structure.
- The computer uses a stack internally, known as the 'call stack.'

When using recursion, our system basically builds up a `call stack`. Using the stack is convenient because you don't need to keep track of function calls (when using recursion), the stack does it for you. However, this comes with a Cost!!

- Each of the function calls (that the stack is keeping track of) takes up some memory. When your call stack is too tall, your computer is saving information for many function calls.
- At this point, you have two options:
  - You can REWRITE your code to use loops instead.
  - You can use something called `tail recursion`. However, this is not supported in every programming language.

## Important QUESTION
Suppose you accidentally wrote a recursive function that runs forever. As you saw, our computer allocates memory on the stack for each function call. What happens to the stack when your RECURSIVE function runs FOREVER???

- Function Calls: Each time the recursive function is called, the computer allocates a new stack frame to store local variables and the return address of the calling function. This process continues as long as the function keeps making recursive calls.
- Stack Growth: With each recursive call, a new stack frame is added on top of the previous one. As the function doesn't reach a base case to stop the recursion, the stack frames keep growing and consuming more memory.
- Stack Overflow: Eventually, the system's stack space is exhausted, and it can no longer allocate more memory for new stack frames. When this happens, the program encounters a stack overflow error, and the operating system terminates the program to prevent any further damage to the system.
