# Task 1

class Data:

    @classmethod
    def get_num_from_dt(cls, dt):
        return tuple(int(num) for num in dt.split('-'))

    @staticmethod
    def validate(num: tuple):
        if 0 < num[0] >= 31 and num[0]:
            raise Exception(f"Bad day {num[0]}")
        if 0 < num[1] >= 12 and num[1]:
            raise Exception(f"Bad month {num[1]}")
        if 0 < num[2] >= 99999 and [2]:
            raise Exception(f"Bad year {num[3]}")
        print("Validate success")


a = Data()
num_dt = a.get_num_from_dt("12-03-2022")

print("Task 1\n")
print(num_dt)
a.validate(num_dt)

# Task 2
print("\nTask 2\n")


class ZeroDivineException(Exception):

    def __str__(self):
        return "Делить на 0 нельзя"


num_input = int(input("Введите число\n"))
divider_input = int(input("Введите делитель:\n"))

try:
    if divider_input == 0:
        raise ZeroDivineException
    print(num_input / divider_input)
except ZeroDivineException as err:
    print(err)

# Task 3
print("\nTask 3\n")


class OnlyNumberException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"В список можно добавить только числа, текущий тип: {type(self.data)}"


def check(num):
    try:
        float(num)
    except:
        raise OnlyNumberException(num)


result = []
while True:
    b = input('Введите число\n')
    if b == "stop":
        break
    try:
        check(b)
    except OnlyNumberException as err:
        print(err)
        continue
    result.append(float(b))
print(result)

# Task 4, Task 5, Task 6
print("\nTask 4,5,6\n")


class Warehouse:
    _warehouse_property: dict = {}
    _available_cnt_warehouse_position: int = 1000
    product: str
    cnt_entrance_position: int

    def __repr__(self):
        return f"{self._warehouse_property}"

    @property
    def available_cnt_warehouse_position(self):
        return self._available_cnt_warehouse_position

    @staticmethod
    def __validate_input(num):
        if isinstance(num, int):
            return True
        print("Количество товаров можно указывать только числами")

    @classmethod
    def receipt_of_goods(cls, product: str, cnt_entrance_position: int):
        if cls.__validate_input(cnt_entrance_position) is None:
            return
        cls._warehouse_property.update({product: cnt_entrance_position})
        cls._available_cnt_warehouse_position -= cnt_entrance_position

    @classmethod
    def move_to_subdivision(cls, product: str, cnt_entrance_position: int):
        if cls.__validate_input(cnt_entrance_position) is None:
            return
        product_to_move = cls._warehouse_property.get(product)
        if product_to_move is None:
            print("Такого товара не существует")
            return
        if product_to_move - cnt_entrance_position > 0:
            cls._warehouse_property.update({product: product_to_move - cnt_entrance_position})
            cls._available_cnt_warehouse_position += cnt_entrance_position
            return
        if product_to_move - cnt_entrance_position == 0:
            cls._warehouse_property.pop(product)
            cls._available_cnt_warehouse_position += cnt_entrance_position
            return
        print(f"Не хватает товара на складе, текущее количестов {product_to_move}")


class OfficeEquipment:
    price: int
    model: str
    manufacturer: str

    def __init__(self, price, model, manufacturer):
        self.price = price
        self.model = model
        self.manufacturer = manufacturer


class Printer(OfficeEquipment):
    volume_ink: int
    cnt_cartridge: int

    def __init__(self, volume_ink, cnt_cartridge, price, model, manufacturer):
        super().__init__(price, model, manufacturer)
        self.volume_ink = volume_ink
        self.cnt_cartridge = cnt_cartridge


class Scanner(OfficeEquipment):
    sensor: int
    type_scanner: int

    def __init__(self, sensor, type_scanner, price, model, manufacturer):
        super().__init__(price, model, manufacturer)
        self.sensor = sensor
        self.type_scanner = type_scanner


class Copier(OfficeEquipment):
    max_dpi: int
    min_dpi: int
    cnt_blanks: int

    def __init__(self, max_dpi, min_dpi, cnt_blanks, price, model, manufacturer):
        super().__init__(price, model, manufacturer)
        self.max_dpi = max_dpi
        self.min_dpi = min_dpi
        self.cnt_blanks = cnt_blanks


wh = Warehouse()
wh.receipt_of_goods("printer", 15)
print(wh, f"Остаток места на складе {wh.available_cnt_warehouse_position}")
wh.move_to_subdivision("printer", 10)
print(wh, f"Остаток места на складе {wh.available_cnt_warehouse_position}")
wh.move_to_subdivision("printer", "пять")
wh.move_to_subdivision("printer", 5)
print(wh, f"Остаток места на складе {wh.available_cnt_warehouse_position}")
wh.move_to_subdivision("scanner", 5)

# Task 7
print("\nTask 7\n")


class ComplexNumber:
    first_num: int
    complex_num: int

    def __init__(self, first_num, complex_num):
        self.first_num = first_num
        self.complex_num = complex_num

    def __mul__(self, other):
        return complex(self.first_num, self.complex_num) + complex(other.first_num, other.complex_num)

    def __truediv__(self, other):
        return complex(self.first_num, self.complex_num) / complex(other.first_num, other.complex_num)


a = ComplexNumber(3, 1)
b = ComplexNumber(5, -2)
print(a * b)
print(a / b)
