# 1.
print('Number 1')
""" Aggregation: # laptop is composite class and battery is its component
12 volt battery with a capacity of 500 Ah battery allows energy storage of
approximately 500 Ah x 12 V = 1,600 Wh."""
class Laptop:
    def __init__(self, voltage):
        self.voltage = voltage

class Battery:
    def __init__(self, voltage, AH_capacity):
        self.voltage = voltage
        self.AH_capacity = AH_capacity
        self.obj_laptop = Laptop(self.voltage)
    def total_capacity(self):
        answer = self.obj_laptop.voltage * self.AH_capacity
        return answer

obj_battery = Battery(12, 500)
print(obj_battery.total_capacity())

# 2.
print('Number 2')
class Guitar:
    def __init__(self, string):
        self.string = string
class GuitarString:
    def __init__(self, material_type):
        self.material_type = material_type

nylon_string = GuitarString('nylon')
Yamaha = Guitar(nylon_string)

# 3.
print('Number 3')
class Sum:
    def __init__(self, syntaxerror, typeerror, nameerror):
        self.syntaxerror = syntaxerror
        self.typeerror = typeerror
        self.nameerror = nameerror
    def add_nums(self):
        return self.syntaxerror + self.typeerror + self.nameerror

sum = Sum(5, 3, 8)
print(sum.add_nums())

# 4.
print('Number 4')
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

pasta_1 = Pasta.bolognaise()
print(pasta_1.ingredients)

pasta_2 = Pasta.carbonara()
print(pasta_2.ingredients)

# 5.
print('Number 5')

class Concert:
    max_visitor_num = 50
    def __init__(self, visitors_count):
        if visitors_count > max_visitor_num:
            self.visitors_count = max_visitor_num
        else:
            self.visitors_count = visitors_count

print(Concert)

Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# 6.
print('Number 6')
import dataclasses
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

schoolAddressBook = AddressBookDataClass(123, 'Mary', '5468931865', '566 Brick Walk', 'slava.ukraini@gmail.com','24.08.1991', 31)
print(schoolAddressBook.email)

