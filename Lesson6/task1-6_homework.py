import time

# task1
print("Task 1\n")


class TrafficLight:
    __color: str = "red"
    _traff_work: tuple = (('red', 7),
                          ('yellow', 2),
                          ('green', 5),)

    def switch_light(self):
        for color, tm in self._traff_work:
            print(color)
            time.sleep(tm)


first = TrafficLight()

first.switch_light()

# task2
print("\nTask 2\n")


class Road:
    _length: float
    _width: float

    def __init__(self, length: float, width: float, mas: float, sm: float) -> None:
        self._length = length
        self._width = width
        self._mas = mas
        self._sm = sm

        self.__get_mass()

    def __get_mass(self):
        print(f"{int((self._length * self._width * self._mas * self._sm) / 1000)} т")


Road(20, 5000, 25, 5)

# task3
print("\nTask 3\n")


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"{self._income['wage'] + self._income['bonus']}")


officer = Position("Иван", "Иванов", "Офицер", 13400, 500)

officer.get_full_name()
officer.get_total_income()

# task4
print("\nTask 4\n")


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed: int, color: str, name: str, is_police: bool) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print("Машина поехала")

    @staticmethod
    def stop():
        print("Машина остановилась")

    @staticmethod
    def turn(direction):
        print(f"Машина поехала {direction}")

    def show_speed(self):
        print(f"Speed: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Over Speed: {self.speed}")
        else:
            print(f"Speed: {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Over Speed: {self.speed}")
        else:
            print(f"Speed: {self.speed}")


class PoliceCar(Car):
    pass


town_car = TownCar(70, "yellow", "mazda", False)
sport_car = SportCar(40, "red", "toyota", False)
work_car = WorkCar(50, "green", "bmw", False)
police_car = PoliceCar(60, "blue", "audi", False)

print(town_car.speed, town_car.color, town_car.name, town_car.is_police)
print(sport_car.speed, sport_car.color, sport_car.name, sport_car.is_police)
print(work_car.speed, work_car.color, work_car.name, work_car.is_police)
print(police_car.speed, police_car.color, police_car.name, police_car.is_police)

town_car.go()
sport_car.stop()
work_car.turn("вправо")
police_car.turn("влево")

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()

# task5
print("\nTask 5\n")


class Stationery:
    title: str

    def __init__(self):
        pass

    def draw(self):
        print(f"Запуск отрисовки", end=': ')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print("Рисуем маркером")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
