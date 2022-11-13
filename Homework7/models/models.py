from framework.models import Model

class Salon(Model):
    file = "salons.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location

class Employee(Model):
    file = "employees.json"

    def __init__(self, name, email, salon_name):
        self.name = name
        self.email = email
        self.salon_name = salon_name