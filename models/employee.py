class Employee:
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        if not first_name.isalpha():
            raise ValueError("First name must contains alphabetic characters only.")
        self.first_name = first_name
        if not last_name.isalpha():
            raise ValueError("Last name must contains alphabetic characters only.")
        self.last_name = last_name
        if not isinstance(base_salary, (int, float)):
            raise TypeError("Base salary must be a number.")
        if base_salary <= 0:
            raise ValueError("Base salary must be bigger than zero.")
        self.base_salary = base_salary
        if not isinstance(experience, int):
            raise TypeError("Experience must be an integer.")
        if experience < 0:
            raise ValueError("Experience must be a positive number.")
        self.experience = experience
              
    
    def salary_calculation(self) -> int:
        calculated_salary = self.base_salary        
        
        if self.experience in range(2, 6):
            calculated_salary += 200
        elif self.experience > 5:
            calculated_salary = calculated_salary * 1.2 + 500          
        
        return round(calculated_salary)
    
    
    def __str__(self):
        """ ToString  method overloaded to let you print information about salary of particular employee."""
        return f"{self.first_name} {self.last_name} received {self.salary_calculation()} money."
    
    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "base_salary": self.base_salary,
            "experience": self.experience
        }
        
    @classmethod    
    def from_dict(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"]
        )