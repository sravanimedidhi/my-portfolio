from collections import deque
bank_queue=deque()
bank_queue.append("Customer 1")
bank_queue.append("Customer 2")
bank_queue.append("Customer 3")
print("Queue afteer customers join:",bank_queue)









cust=bank_queue.popleft()
print(f"{cust} is being sereved")
print("Next in line:",bank_queue[0])
bank_queue.append("Customer 4")
print("Queue after joining the new customers:",bank_queue)






while bank_queue:
    current=bank_queue.popleft()
    print(f"{current} is begin served.")
print("Queue empty?", not bank_queue)



















