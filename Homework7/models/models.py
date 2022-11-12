import json

class Salon:
    def __init__(self, name, employee):
        self.employee = employee
        self.name = name

    def save(self):
        file = open("database/salons.json", "r")
        data_in_json = file.read()
        file.close()
        data = json.loads(data_in_json)
        new_salon = {
            "name": self.name, "employee": self.employee
        }
        if len(data) > 0:
            new_salon["id"] = data[-1]["id"] + 1
        else:
            new_salon["id"] = 1
        data.append(new_salon)
        file = open("database/salons.json", "w")
        file.write(json.dumps(data))
        file.close()

    @staticmethod
    def get_all():
        file = open("database/salons.json", "r")
        salons = json.loads(file.read())
        file.close()
        for salon in salons:
            print(salon["name"])
            print(salon["employee"])

    @staticmethod
    def get_by_id(id):
        file = open("database/salons.json", "r")
        salons = json.loads(file.read())
        file.close()
        for salon in salons:
            if salon["id"] == id:
                print(salon["name"])
                print(salon["employee"])
                print(salon["id"])

class Employee:
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id

    def save(self):
        file = open("database/employee.json", "r")
        data_in_json = file.read()
        file.close()
        data = json.loads(data_in_json)
        new_employee = {
            "name": self.name,
            "email": self.email,
            "id": self.id
        }
        if len(data) > 0:
            new_employee["id"] = data[-1]["id"] + 1
        else:
            new_employee["id"] = 1
        data.append(new_employee)
        file = open("database/employee.json", "w")
        file.write(json.dumps(data))
        file.close()

    @staticmethod
    def get_all():
        file = open("database/employee.json", "r")
        employee = json.loads(file.read())
        file.close()
        for employee in employee:
            print(employee["name"])
            print(employee["email"])
            print(employee["id"])

    @staticmethod
    def get_by_id(id):
        file = open("database/employee.json", "r")
        employee = json.loads(file.read())
        file.close()
        for employee in employee:
            if employee["id"] == id:
                print(employee["name"])
                print(employee["email"])
                print(employee["id"])
