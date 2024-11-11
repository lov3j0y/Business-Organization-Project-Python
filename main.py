from models import *

employee = Employee("Emil", "Vilhelm", 1500, 5)

designer = Designer("Gabriela", "Georgieva", 1500, 5, 1)
developer = Developer("Ivaylo", "Ivanov", 1500, 1)
developer2 = Developer("Ivaylo", "Ivanov", 1500, 3)
developer3 = Developer("Ivaylo", "Ivanov", 1500, 5)
developer4 = Developer("Ivaylo", "Ivanov", 1500, 7)


manager1 = Manager("Martin", "Petkov", 2000, 10)
manager1.add_team_members(developer)
manager1.add_team_members(developer2)
manager1.add_team_members(developer3)
manager1.add_team_members(developer4)
manager1.add_team_members(designer)


department = Department()
department.add_manager(manager1)


department.print_department_teams()
department.give_salary()

department.save_employees("data/employees.json")

new_department = Department()
new_department.load_employees("data/employees.json")
for manager in new_department.managers:
    print(manager.to_dict())