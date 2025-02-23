Monotonic stacks can be four types:

1. Strictly Decreasing Stack: every element is smaller than its previous elemententer code here
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

```
def nextGreaterElement(arr):
    stack = [] # non-increasing stack
    nextGreaterElement = [-1]*len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            stack_top = stack.pop()
            nextGreaterElement[stack_top] = arr[i]
        
        stack.append(i)
    
    return nextGreaterElement


def nextGreaterOrEqualElement(arr):
    stack = [] # strictly decreasing stack
    nextGreaterOrEqual = [-1]*len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack_top = stack.pop()
            nextGreaterOrEqual[stack_top] = arr[i]
        
        stack.append(i)
    
    return nextGreaterOrEqual
            
def previousGreaterElement(arr):
    stack = [] # strictly decreasing stack
    previousGreater = [-1]*len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        
        if stack:
            previousGreater[i] = arr[stack[-1]]
            
        stack.append(i)
        
    
    return previousGreater
        
    
def previousGreaterAndNextGreaterOrEqualElement(arr):
    stack = [] # strictly decreasing stack
    previousGreater = [-1]*len(arr)
    nextGreaterOrEqual = [-1]*len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack_top = stack.pop()
            nextGreaterOrEqual[stack_top] = arr[i]
        
        if stack:
            previousGreater[i] = arr[stack[-1]]
            
        stack.append(i)
        
    
    return previousGreater,nextGreaterOrEqual
        
arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
print(arr)
print(nextGreaterElement(arr))
print(nextGreaterOrEqualElement(arr))
print(previousGreaterElement(arr))
print(previousGreaterAndNextGreaterOrEqualElement(arr))
            
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMzMwMDQ2NTYsNTY5MDMxMjMzLC00NT
EyNzgwMzQsLTE3OTcxMTY2ODEsNDQwOTIwNTg1XX0=
-->