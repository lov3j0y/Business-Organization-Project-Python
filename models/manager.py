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
        if isinstance(member, (Developer, Designer)):
            self.team.append(member)
        else:
            raise TypeError("Only Developers and Designers can be members of the team.")
        
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


def deserialize_employee(data):
    """Helper function to create instances based on type."""
    if data["type"] == "Developer":
        return Developer.from_dict(data)
    elif data["type"] == "Designer":
        return Designer.from_dict(data)
    elif data["type"] == "Manager":
        return Manager.from_dict(data)
    else:
        raise ValueError(f"Unknown employee type: {data['type']}")