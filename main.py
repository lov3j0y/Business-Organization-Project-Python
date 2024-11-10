from models import *

employee = Employee("Emil", "Vilhelm", 1500, 5)

designer = Designer("Gabriela", "Georgieva", 1500, 5, 1)
developer = Developer("Ivaylo", "Ivanov", 1500, 1)
developer2 = Developer("Ivaylo", "Ivanov", 1500, 3)
developer3 = Developer("Ivaylo", "Ivanov", 1500, 5)
developer4 = Developer("Ivaylo", "Ivanov", 1500, 7)


manager = Manager("Martin", "Petkov", 2000, 10)
manager.add_team_members(developer)
manager.add_team_members(developer2)
manager.add_team_members(developer3)
manager.add_team_members(developer4)
manager.add_team_members(designer)


department = Department()
department.add_manager(manager)

department.print_department_teams()
department.give_salary()