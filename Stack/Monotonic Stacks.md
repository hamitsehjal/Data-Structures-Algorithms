Monotonic stacks can be four types:

1. Strictly Decreasing Stack
2. Non-Increasing Stack: every element is either smaller or equals to its previous element
3. Strictly Increasing Stack
4. Non-Decreasing Stack


```
function buildMonoStack(array){
// initialize a stack
stack = []

for (i=0;i<len(array;i++){
		while stack is not empty and element represented by stack top is `operator` array[i] {
			let stackTop = stack.pop()
			
			// Do something with the stackTop
			// For example,
			// nextGreater[stackTop] = array[i]
		}
		
		if (stack.length) {
			// if stack has still some element
		}
	}

}

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2ODcxMDAxNTIsNDQwOTIwNTg1XX0=
-->