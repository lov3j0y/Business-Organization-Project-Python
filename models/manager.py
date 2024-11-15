from .employee import Employee
from .developer import Developer
from .designer import Designer

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
        return round(calculated_salary)
    
    def add_team_members(self, member):
        #You should check if a Developer or Designer with the given first_name and last_name already exists in the team
        if isinstance(member, (Developer, Designer)):
            self.team.append(member)
        else:
            raise TypeError("Only Developers and Designers can be members of the team.")
        
        
        #TO DO: remove_team_members()
    #  Don't forget to either remove TODOs that are no longer relevant or implement them before pushing to github
        
    def print_team_members(self):
        for member in self.team:
            print(member)
            
    def to_dict(self):
        data = super().to_dict()
        data["team"] = [member.to_dict() for member in self.team]
        return data

    @classmethod
    def from_dict(cls, data):
        manager = cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"]
        )
        manager.team = [deserialize_employee(member_data) for member_data in data["team"]]
        return manager


EMPLOYEE_TYPES = {
    "Developer": Developer,
    "Designer": Designer,
    "Manager": Manager
}

# This code will be more maintainable if we use a dictionary mapping instead of multiple if-elif statements.
# Adding new employee types will only require updating the dictionary, not modifying the function logic.
def deserialize_employee(data: dict) -> Employee:
    """Helper function to create instances based on type."""
    employee_type = data["type"]
    employee_class = EMPLOYEE_TYPES.get(employee_type)

    if employee_class is None:
        raise ValueError(f"Unknown employee type: {employee_type}")

    return employee_class.from_dict(data)