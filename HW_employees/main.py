from Application.db.people import Employees
from Application.salary import Salary
from datetime import datetime


if __name__ == '__main__':
    date = datetime.now()
    print(date)
    ivan = Employees()
    ivan.get_employees()
    manager2 = Salary()
    manager2.calculate_salary('manager')
