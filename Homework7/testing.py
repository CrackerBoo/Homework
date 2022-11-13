class Employee: # in framework file

    def save(self):
        file = open("database/employees.json", "r")
        data_in_json = file.read()
        file.close()
        data = json.loads(data_in_json)
        new_employee = {
            "name": self.name,
            "email": self.email,
            "salon_name": self.salon_name
        }
        if len(data) > 0:
            new_employee["id"] = data[-1]["id"] + 1
        else:
            new_employee["id"] = 1
        data.append(new_employee)
        file = open("database/employees.json", "w")
        file.write(json.dumps(data))
        file.close

    @staticmethod
    def get_all():
        file = open("database/employees.json", "r")
        employees = json.loads(file.read())
        file.close()
        for employee in employees:
            print(employee["name"])
            print(employee["email"])
            print(employee["salon_name"])

    @staticmethod
    def get_by_salon_name(salon_name):
        file = open("database/employees.json", "r")
        employees = json.loads(file.read())
        file.close()
        for employee in employees:
            if employee["salon_name"] == salon_name:
                print(employee["name"])
                print(employee["salon_name"])