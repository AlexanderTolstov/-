import random
import time
import threading
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_eat = random.randint(3, 10)
        time.sleep(time_to_eat)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break

            if free_table is not None:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():  # Проверка, жив ли поток
                        print(f"{table.guest.name} покушал(а) и ушёл(ла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f"{next_guest.name} вышел(ла) из очереди и сел(а) за стол номер {table.number}")

            time.sleep(1)


if __name__ == "__main__":
    guests_names = ['Alexander', 'Svaelana', 'Sophia', 'Oleg', 'Maxim', 'Elena', 'Natasha', 'Stephan', 'Olga', 'Egor',
                    'Xenia', 'Vadim', 'Dmitry', 'Oksana', 'Paavel', 'Konstantin']
    cafe = Cafe(Table(1), Table(2), Table(3), Table(4), Table(5), Table(6))

    guests = [Guest(f"Гость {name}") for name in guests_names]
    cafe.guest_arrival(*guests)

    cafe.discuss_guests()
print('В кафе не осталось посетителей, можно закрываться!')