from decimal import Decimal
from datetime import date
from classes import Employee
from decorator import timer

# Initialize employees object
employees = [
    Employee(name="John", start=date(2022, 5, 20), rate=Decimal("11"), taxes=10),
    Employee(name="Alex", start=date(2022, 5, 1), rate=Decimal("50"), taxes=20),
    Employee(name="Kseniya", start=date(2022, 5, 10), rate=Decimal("50"), taxes=40),
    Employee(name="Valeriy", start=date(2022, 4, 20), rate=Decimal("60"), taxes=50),
    Employee(name="Vera", start=date(2019, 5, 20), rate=Decimal("99"), taxes=60),
    Employee(name="Suzanna", start=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
    Employee(name="Gleb", start=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
]


@timer("Show table ")
def show_table():
    Employee.show_header()
    for employee in employees:
        Employee.show_line()
        Employee.show_row(employee)


def update_table():
    for employee in employees:
        input_rate = int(
            input(
                "What is employee rate for {employee_name}".format(
                    employee_name=employee.name
                )
            )
        )
        employee.update_rate(input_rate)
        employee.validation(
            employee.name,
            employee._start,
            employee._end,
            employee.rate,
            employee._taxes,
        )


if __name__ == "__main__":
    show_table()
    update_table()
    show_table()
