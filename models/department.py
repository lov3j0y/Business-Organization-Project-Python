from models import *
from tabulate import tabulate

class Department:
    def __init__(self, name = None):
        if name is not None:
            self.name = name
        else:
            self.name = ""
        
        self.managers = []
        
    def add_manager(self, manager):
        if isinstance(manager, Manager):
            self.managers.append(manager)
        else:
            raise TypeError("Only employees of type Managers can be added to the department.")
    
    def give_salary(self):
        for manager in self.managers:
            print(manager)
        manager.print_team_members()
            
    def print_department_teams(self):
        print("\n" + "=" * 50 + "\n")
        
        print(f"Department: {self.name}")
        for manager in self.managers:
            print(f"Manager: {manager.first_name} {manager.last_name}")
            
            team_data = [
                [
                    member.__class__.__name__,
                    member.first_name,
                    member.last_name,
                    member.salary_calculation(),
                    member.experience                    
                ]
                for member in manager.team
            ]
            
            headers = ["Role", "First Name", "Last Name", "Salary", "Experience (Years)"]            
            
            print(tabulate(team_data, headers=headers, tablefmt="pretty"))
            print("\n" + "=" * 50 + "\n")
            
