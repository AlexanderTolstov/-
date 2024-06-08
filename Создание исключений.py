class GamesException(Exception):
    def __init__(self, name, number, points, status):
        self.name = name
        self.number = number
        self.points = points
        self.status = status

    def __str__(self):
        return f'{self.name} is not correct number: {self.number}'

class PointException(Exception):
    def __init__(self, name, number, points, status):
        self.name = name
        self.number = number
        self.points = points
        self.status = status

    def __str__(self):
        return f'{self.name} is not correct points: {self.points}'

class FootballClub:
    def __init__(self, name, number, points, status):
        self.name = name
        if number > 38 or number < 38:
            raise GamesException(name, number, points, status)
        else:
            self.number = number
        if points > 100:
            raise PointException(name, number, points, status)
        else:
            self.points = points
        self.status = status
        print(f'Команда: {self.name}, Игры в сезоне: {self.number}, Очки: {self.points}, Место в таблице: {self.status}')
try:
    Arsenal = FootballClub('Arsenal', 38, 89, '2nd place')
    Chelsea = FootballClub('Chelsea', 34, 63, '6th place')
    ManchesterCity = FootballClub('Manchester City', 38, 91, 'Champion')
except GamesException as e:
    print(f'У команды некорректоное колличество игр,', e)
try:
    Arsenal = FootballClub('Arsenal', 38, 256, '2nd place')
    Chelsea = FootballClub('Chelsea', 38, 63, '6th place')
    ManchesterCity = FootballClub('Manchester City', 38, 91, 'Champion')
except PointException as a:
    print(f'У команды некорректное колличство очков,', a)
finally:
    print(f'Хоть Сити и чемпион, Арсенал все равно крутая команда!!!')

