class Employee:
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience
        
        
    def salary_calculation(self) -> int:
        calculated_salary = 0   
        if self.experience in range(2, 6):
            self.base_salary += 200
        elif self.experience > 5:
            self.base_salary = self.base_salary * 1.2 + 500
            
        calculated_salary = self.base_salary
        return int(calculated_salary)