from models.models import Salon, Employee

while True:
    print("1. Add new salon\n"
            "2. Get all salons\n"
            "3. Get salon by id\n"
            "4. Add new employee\n"
            "5. Get all employee\n"
            "6. Get employee by id\n"
                )
    flag = int(input("Choose: "))
    if flag == 1:
        name = input("Type name of new salon: ")
        employee = input("Type name of selected employee: ")
        salon = Salon(name, employee)
        salon.save()
    elif flag == 2:
        Salon.get_all()
    elif flag == 3:
        id = int(input("Type id of this salon: "))
        Salon.get_by_id(id)
    elif flag == 4:
        name = input("Type name of employee: ")
        id = int(input("Type id of salon where employee works: "))
        email = input("Type email of employee: ")
        employee = Employee(name, id, email)
        employee.save()
    elif flag == 5:
        Employee.get_all()
    elif flag == 6:
        id = int(input("Type id of this employee: "))
        Employee.get_by_id(id)