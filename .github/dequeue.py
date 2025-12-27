from collections import deque
import time
import random
import os

class BankQueueSystem:
    def __init__(self):
        self.bank_queue = deque()
        self.token_number = 1
        self.customers = ["Sravani", "Hasini", "Adwitha", "Bhanu", "Varshini"]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def assign_tokens(self):
        print(" Bank Counter System Starting...\n")
        time.sleep(1)

        for customer in self.customers:
            print(f" Token #{self.token_number} assigned to {customer}")
            self.bank_queue.append((self.token_number, customer))
            self.token_number += 1
            time.sleep(1)

        print("\n All customers are now in the waiting queue.")
        time.sleep(2)

    def serve_customers(self):
        self.clear_screen()
        print(" Teller is now serving customers...\n")
        time.sleep(1)

        while self.bank_queue:
            token, name = self.bank_queue.popleft()
            self.clear_screen()
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

# ----------------------------
# Main program execution
# ----------------------------
if __name__ == "__main__":
    bank = BankQueueSystem()
    bank.assign_tokens()
    bank.serve_customers()