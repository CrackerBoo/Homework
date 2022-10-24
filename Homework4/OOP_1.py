# 1.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print(f'speed increase is {self.max_speed} mi/h')

    def break_speed(self):
        print(f'break speed is {self.max_speed} mi/h')

    def mileage_info(self):
        print(f'the number of miles on this vehicle odometer is {self.mileage}')

# 2.
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def seating_capacity(self):
        print(f'This bus can carry approximately {self.seating_capacity} passengers')

# 3.
print(issubclass(Bus, Vehicle))

# 4.
school_bus = Bus(45, 150000, 60)

print(isinstance(school_bus, Vehicle))
print(isinstance(school_bus, Bus))

# 5.
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self):
        print(f'school id {self.get_school_id} points out to its location, which is at OX1 4AU, Oxford, United Kingdom')

    def main_subject(self):
        print(f'since this school specializes in Sciences, the main subject for all {self.number_of_students} students is Information Technology')

# 6.
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        super(School).__init__(get_school_id, number_of_students)
        super(Bus).__init__(max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def bus_school_color(self):
        print(f'Boris Johnson ordered all school buses to be painted in {self.bus_school_color}')

# 7.
class Bear:
    def __init__(self, color, preference):
        self.preference = preference
        self.color = color

    def eat(self):
        print(f'Hello world! I am a {self.color} bear and I love to eat {self.preference}.')

class Wolf:
    def __init__(self, color, preference):
        self.preference = preference
        self.color = color

    def eat(self):
        print(f'Hello world! I am a {self.color} wolf and I like to eat {self.preference}.')

Vedmedyk_Lasunchyk = Bear('brown', 'berries')
Siryi_Vovk = Wolf('grey', 'kolobok')

for animal in (Vedmedyk_Lasunchyk, Siryi_Vovk):
    animal.eat()

# 8.
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        if population < 1500:
            print('Your city is too small')
        else:
            print('This is a city of moderate size')

Lutsk = City('Lutsk', 1000)
print(Lutsk.name)
