from Application.db.db import salary


class Salary():

    def __init__(self):
        print("Зарплатный класс")

    def calculate_salary(self, position):
        for key, value in salary.items():
            if key == position:
                salary_max = int(salary[position][0]["salary"]) + int(salary[position][0]["bonus"])
                print(f'{salary_max} RUR')
