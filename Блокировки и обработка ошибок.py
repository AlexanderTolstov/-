import threading
import random
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f"Пополнение: {amount}. Баланс: {self.balance + amount}")
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += amount
        time.sleep(0.001)
    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            time.sleep(0.001)
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
                time.sleep(0.001)
            else:
                print("Запрос отклонён, недостаточно средств")
                time.sleep(0.001)
                self.lock.acquire()
            time.sleep(0.001)

bank = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(bank, ))
thread2 = threading.Thread(target=Bank.take, args=(bank,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Итоговый баланс: {bank.balance}")