from .manager import Manager, deserialize_employee
from tabulate import tabulate
import json

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
            raise TypeError("Only employees of type Manager can be added to the department.")
        
    # TO DO: remove_manager()
    
    def give_salary(self):
        for manager in self.managers:
            print(manager)
        manager.print_team_members()
            
    def print_department_teams(self):
        """Extra function to print all managers with their teams and information about them in a table."""
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
            
    def save_employees(self, filename):
        """Serializes the list of managers (and their teams) to a JSON file."""
        with open(filename, "w") as file:
            json.dump([manager.to_dict() for manager in self.managers], file, indent = 4)
        print(f"Data saved to {filename}.")
        
    def load_employees(self, filename="data/employees.json"):
        """Deserializes the JSON file to restore the list of managers and their teams."""
        try:
            with open(filename, 'r') as file:
                data_list = json.load(file)
                self.managers = [deserialize_employee(data) for data in data_list]
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {filename}: {e}")
                    
