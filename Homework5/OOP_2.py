# 1.
class Laptop:
    def __init__(self):
       button_1 = Button('This is page 1')
       button_2 = Button('This is page 2')
       button_3 = Button('This is page 3')
       self.laptop = [button_1.voltage, button_2.voltage, button_3.voltage]

class Battery:
    def __init__(self, voltage):
        self.voltage = voltage

# 2.
class Guitar:
    def __init__(self):
        self.string = string

class GuitarString:
    def __init__(self, material_type):
        self.material_type = material_type

nylon = GuitarString('nylon')
Yamaha = Guitar(nylon_string)

# 3.
class Calc:
    """
    Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
    """

3
class Calc:
    """
    Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
    """

4*.
class Pasta:
    """
    Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """

6.
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """

7. Create the same class (6) but using NamedTuple

8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """
9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"

10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name