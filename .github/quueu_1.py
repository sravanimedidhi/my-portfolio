from collections import deque
import time
import random
import os

# Function to clear screen for live effect
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Step 1: Create queue (customer name + token number)
bank_queue = deque()
token_number = 1

# Step 2: Simulate customers arriving
customers = ["Anushka", "Siri", "Akshitha", "Srivalli", "Varshini"]

print(" Bank Counter System Starting...\n")
time.sleep(1)

for customer in customers:
    print(f" Token #{token_number} assigned to {customer}")
    bank_queue.append((token_number, customer))
    token_number += 1
    time.sleep(1)

print("\n All customers are now in the waiting queue.")
time.sleep(2)

# Step 3: Start serving customers
clear_screen()
print(" Teller is now serving customers...\n")
time.sleep(1)

while bank_queue:
    token, name = bank_queue.popleft()
    clear_screen()
    print("====================================")
    print(f" BANK SERVICE COUNTER DISPLAY")
    print("====================================")
    print(f" Now Serving: Token #{token} — {name}")
    print("====================================")
    
    service_time = random.randint(2, 5)
    for remaining in range(service_time, 0, -1):
        print(f" Serving {name}... {remaining} sec remaining", end='\r')
        time.sleep(1)
    print(f"\n {name}'s service completed! Thank you, {name}.\n")
    time.sleep(2)

print("\n All customers have been served. Queue is now empty!\n")