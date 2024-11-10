from models import *

class Designer(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, eff_coeff: float):
        super().__init__(first_name, last_name, base_salary, experience)
        if not (0 <= eff_coeff <= 1):
            raise ValueError("Coefficient of efficiency must be between 0 and 1.")
        self.eff_coeff = eff_coeff # number betweeen 0 and 1
        
        
    def salary_calculation(self) -> int:
        calculated_salary = super().salary_calculation()
        calculated_salary *= self.eff_coeff
        return int(calculated_salary)