# Queue implementation using list

queue = []

queue.append(10)
queue.append(20)

print("Queue after enqueue:", queue)

queue.pop(0)
print("Queue after dequeue:", queue)

front = queue[0]
print("Front element:", front)
