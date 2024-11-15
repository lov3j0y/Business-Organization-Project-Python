from .employee import Employee

# Please refactor the Employee class based on the suggestion: validate all inputs before assigning any values to instance variables
class Designer(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, eff_coeff: float):
        super().__init__(first_name, last_name, base_salary, experience)
        if not isinstance(eff_coeff, (int, float)):
            raise TypeError("Coefficient of efficiency must be a number.")
        if not (0 <= eff_coeff <= 1):
            raise ValueError("Coefficient of efficiency must be between 0 and 1.")
        self.eff_coeff = eff_coeff
        
        
    def salary_calculation(self) -> float:
        calculated_salary = super().salary_calculation()
        # the requirement counted_salary * eff_coeff is incorrect, it should be: counted_salary + counted_salary * eff_coeff
        designer_bonus = calculated_salary * self.eff_coeff
        return round(calculated_salary + designer_bonus, 2)
    
    def to_dict(self):
        data = super().to_dict()
        data["eff_coeff"] = self.eff_coeff
        data["type"] = "Designer"
        return data
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"],
            data["eff_coeff"]
        )