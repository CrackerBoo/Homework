from models.models import Salon, Employee

while True:
    print("1. Add new salon \n "
          "2. Get all salons \n "
          "3. Get salon by id \n "
          "4. Delete salon by id \n "
          "5. Add new employee \n "
          "6. Get all employees \n "
          "7. Get employee by salon_name \n "
          "8. Delete employee by salon_name \n "
          )
    flag = int(input("Choose: "))
    if flag == 1:
        name = input("Type name of new salon: ")
        location = input("Type location of salon: ")
        salon = Salon(name, location)
        salon.save()
    elif flag == 2:
        salons = Salon.get_all()
        for salon in salons:
            print(salon["id"])
            print(salon["name"])
            print(salon["location"])
    elif flag == 3:
        id = int(input("Type id of salon: "))
        salon = Salon.get_by_id(id)
        print(salon["id"])
        print(salon["name"])
        print(salon["location"])
    elif flag == 4:
        id = int(input("Type id of salon you want to delete: "))
        Salon.delete_id(id)
    elif flag == 5:
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        salon_name = input("Type name of salon: ")
        employee = Employee(name, email, salon_name)
        employee.save()
    elif flag == 6:
        employees = Employee.get_all()
        for employee in employees:
            print(employee["salon_name"])
            print(employee["email"])
            print(employee["name"])
    elif flag == 7:
        salon_name = input("Type salon_name of employee: ")
        employee = Employee.get_by_salon_name(salon_name)
        print(employee["salon_name"])
        print(employee["email"])
        print(employee["name"])
    elif flag == 8:
        salon_name = input("Type salon_name of employee: ")
        Employee.delete(salon_name)