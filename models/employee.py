class Employee:

    # It would be better validate all inputs before assigning any values to instance variables
    @staticmethod
    def _validate_string_field(value: str, field_name: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string.")
        if not value:
            raise ValueError(f"{field_name} must not be empty.")
        if not value.isalpha():
            raise ValueError(f"{field_name} must contain only alphabetic characters.")

    @staticmethod
    def _validate_numeric_field(value: float | int, field_name: str, min_value: float = 0,
                                integer_only: bool = False) -> None:
        if integer_only and not isinstance(value, int):
            raise TypeError(f"{field_name} must be an integer.")
        elif not integer_only and not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number.")
        if value < min_value:
            raise ValueError(f"{field_name} must be greater than or equal to {min_value}.")

    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        """
        Initialize an Employee instance.

        Args:
            first_name (str): Employee's first name
            last_name (str): Employee's last name
            base_salary (float): Base salary amount
            experience (int): Years of experience

        Raises:
            TypeError: If any argument is of incorrect type
            ValueError: If any argument contains invalid data
        """
        self._validate_string_field(first_name, "First name")
        self._validate_string_field(last_name, "Last name")
        self._validate_numeric_field(base_salary, "Base salary", min_value=0.1)
        self._validate_numeric_field(experience, "Experience", integer_only=True)

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