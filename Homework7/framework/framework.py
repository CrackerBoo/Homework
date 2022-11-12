import json
from abc import ABC

class Model(ABC):
    file = "default.json"

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