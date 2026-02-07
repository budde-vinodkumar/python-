# Queue implementation using list

queue = []

# Enqueue operations
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

# Dequeue operation
queue.pop(0)
print("Queue after dequeue:", queue)

# Front element
front = queue[0]
print("Front element:", front)
