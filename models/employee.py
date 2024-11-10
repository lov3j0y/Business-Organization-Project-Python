class Employee:
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience
              
    
    def salary_calculation(self) -> int:
        calculated_salary = self.base_salary        
        
        if self.experience in range(2, 6):
            calculated_salary += 200
        elif self.experience > 5:
            calculated_salary = calculated_salary * 1.2 + 500          
        
        return int(calculated_salary)
    
    
    def __str__(self):
        """ ToString  method overloaded to let you print information about salary of particular employee."""
        return f"{self.first_name} {self.last_name} received {self.salary_calculation()} money."