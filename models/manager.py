from models import *

class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, team = None):
        super().__init__(first_name, last_name, base_salary, experience)
        if team is not None:
            self.team = team
        else:
            self.team = []
        
        
    def salary_calculation(self) -> int:
        calculated_salary = super().salary_calculation()
        team_size = len(self.team)
        
        if team_size > 10:
            calculated_salary += 300
        elif team_size > 5:
            calculated_salary += 200
            
        
        
        developer_count = sum(1 for member in self.team if isinstance(member, Developer))
        
        if developer_count > team_size / 2:
            calculated_salary *= 1.1
        return int(calculated_salary)
    
    def add_team_members(self, member):
        if isinstance(member, (Developer, Designer)):
            self.team.append(member)
        else:
            raise TypeError("Only Developers and Designers can be members of the team.")