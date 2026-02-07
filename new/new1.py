# Stack implementation using list

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop operation
stack.pop()
print("Stack after pop:", stack)

# Peek (top element)
top = stack[-1]
print("Top element:", top)
