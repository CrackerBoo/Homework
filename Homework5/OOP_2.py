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

#2.
print('Number2')
class Guitar:
    def __init__(self,string):
        self.string=string
class GuitarString:
    def __init__(self,material_type):
        self.material_type=material_type

nylon_string = GuitarString('nylon')
Yamaha = Guitar(nylon_string)

#3.
print('Number3')
class Sum:
    def __init__(self,syntaxerror,typeerror,nameerror):
        self.syntaxerror=syntaxerror
        self.typeerror=typeerror
        self.nameerror=nameerror
    def add_nums(self):
        return self.syntaxerror + self.typeerror + self.nameerror

sum = Sum(5,3,8)
print(sum.add_nums())

#4.
print('Number4')
class Pasta:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat','tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon','parmesan','eggs'])

pasta_1 = Pasta.bolognaise()
print(pasta_1.ingredients)

pasta_2 = Pasta.carbonara()
print(pasta_2.ingredients)

#5.
print('Number5')
class Concert:
    max_visitor_num = 50
    def __init__(self, visitors_count):
        if visitors_count > max_visitor_num:
            self.visitors_count = max_visitor_num
        else:
            self.visitors_count = visitors_count

#6.
print('Number6')
import dataclasses
@dataclasses.dataclass

class AddressBookDataClass:
    key:int
    name:str
    phone_number:str
    address:str
    email:str
    birthday:str
    age:int

schoolAddressBook = AddressBookDataClass(123,'Mary','5468931865','566 Brick Walk','slava.ukraini@gmail.com','24.08.1991',31)
print(schoolAddressBook.email)
print(schoolAddressBook.birthday)

#7.
print('Number7')
import collections
AddressBookDataClass = collections.namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
schoolAddressBook2 = AddressBookDataClass(678,'Gary','847262729','755 Brick Walk','heroiam.slava@gmail.com','24.08.1991',31)
print(schoolAddressBook2[4])

#8.
print('Number8')
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def AddressBook(self):
        print(f"key: {self.key}, name: {self.name}, phone_number: {self.phone_number}, address: {self.address}, email: {self.email}, birthday: {self.birthday}, age: {self.age}")

VIP = AddressBook(7, 'Volodymyr_Velykyi', '3367462098', 'Volodymyrskiy descent 6 Kyiv', 'kyiv@gmail.com', '15.07.963', 50)
VIP.AddressBook()

#9.
print('Number9')
class Person:
    def __init__(self, age = 36, name = "John", country = "USA"):
        self.name = name
        self.age = age
        self.county = country

    def get_age(self):
        return self._age

    def set_age(self, x):
        self._age = x

Human = Person()
Human.set_age(80)

print(Human._age)

#10.
print('Number10')
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(787, 'Mary')
setattr(student,'email','luck@gmail.com')
print('name: ', student.name)
print('id: ', student.id)

student_email = print(student.email)
#Assign the new attribute to 'student_email' variable and print it by using getattr - not sure how to solve this part yet
#what is meant by 'assign a new attribute to 'student_email' variable? This new variable was created, but what comes next?
#Does it work the same way as class attributes?






