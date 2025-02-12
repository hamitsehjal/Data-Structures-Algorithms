Monotonic stacks can be four types:

1. Strictly Decreasing Stack: every element is smaller than its previous element
2. Non-Increasing Stack: every element is either smaller or equals to its previous element
3. Strictly Increasing Stack
4. Non-Decreasing Stack


Template to build a stack that keep the monotonous property alive through the execution of the program.
```
function buildMonoStack(array){
// initialize a stack
stack = []

for (i=0;i<len(array;i++){
		while stack is not empty and element represented by stack top is `operator` array[i] {
			let stackTop = stack.pop()
			
			// Do something with the stackTop
			// For example,
			// nextGreater[stackTop] = stack.at(-1)
		}
		
		if (stack.length) {
			// if stack has still some elements left
			// do something with stack top here e.g.,
			previousGreater[i] = stack.at(-1)
		}

		stack.push(i)
	}

}

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ1MTI3ODAzNCwtMTc5NzExNjY4MSw0ND
A5MjA1ODVdfQ==
-->