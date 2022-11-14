import sys
from models.models import Salon, Employee

class Controller:
    @staticmethod
    def __init__(self):
        self.salon = Salon()
        self.employee = Employee()
        self.choices = {
            "1": self.add_new_salon,
            "2": self.get_all_salons,
            "3": self.get_salon_by_id,
            "4": self.delete_salon_by_id,
            "5": self.add_new_employees,
            "6": self.get_employee_by_salon_name,
            "7": self.delete_employee_by_salon_name
            }

    def display_menu(self):
        print("""
Salon Employee Controller

1. Add new salon 
2. Get all salons 
3. Get salon by id 
4. Delete salon by id 
5. Add new employee 
6. Get all employees 
7. Get employee by salon_name 
8. Delete employee by salon_name
""")

    @staticmethod
    def get_data(path):
        file = open(path, "r")
        data = json.loads(file.read())
        file.close()
        return data

    def save(self):
        data = self.get_data("database/" + self.file)
        new_instance = self.__dict__
        if len(data) > 0:
            new_instance["id"] = data[-1]["id"] + 1
        else:
            new_instance["id"] = 1
        data.append(new_instance)
        self.save_data_to_file(data, "database/" + self.file)

    @staticmethod
    def save_data_to_file(data, path):
        file = open(path, "w")
        file.write(json.dumps(data))
        file.close()

    @classmethod
    def get_all(cls):
        instances = cls.get_data("database/" + cls.file)
        return instances

    @classmethod
    def get_by_salon_name(cls, salon_name):
        instances = cls.get_data("database/" + cls.file)
        for instance in instances:
            if instance["salon_name"] == salon_name:
                return instance

    @classmethod
    def get_by_id(cls, id):
        file = open("database/" + cls.file, "r")
        instances = json.loads(file.read())
        file.close()
        for instance in instances:
            if instance["id"] == id:
                return instance

    @classmethod
    def delete_id(cls, id):
        instances = cls.get_data("database/" + cls.file)
        for i in range(len(instances)):
            if instances[i]["id"] == id:
                del instances[i]
                break
        cls.save_data_to_file(instances, "database/" + cls.file)



