from threading import Thread
import time

class Knight(Thread):
    def __init__(self,name, power, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.power = power
        self.enemy = 100
        self.time_day = 5
        self.day = 0

    def run(self):
        print(f"{self.name}, На нас напали!")
        while self.enemy > 0:
            self.day += 1
            print(f"{self.name} сражается {self.day} дней(дня)...,"
                f"осталось {self.enemy - self.power} воинов.")
            self.enemy = self.enemy - self.power
            time.sleep(self.time_day)
        print(f"{self.name} одержал победу за {self.day} дней(дня)")

knight1 = Knight('sir Lancelot', 10)
knight2 = Knight('sir Galahad', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("Все враги убиты, все бои закончены!!! Ура, ПОБЕДА!!!!")