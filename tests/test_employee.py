import pytest
import coverage
from models import *

@pytest.mark.employee_initialization_tests
class TestEmployeeInitialization:
    def test_add_employee_with_valid_data(self):
        employee = Employee("John", "Doe", 50000, 5)
        assert employee is not None
        assert isinstance(employee, Employee)
        
        assert employee.first_name == "John"
        assert employee.last_name == "Doe"
        assert employee.base_salary == 50000
        assert employee.experience == 5



    @pytest.mark.parametrize("first_name, last_name, base_salary, experience", [
        ("J0hn", "Doe", 50000, 5),
        ("John", "Doe@#", 50000, 5),
        ("John", "Doe", -256, 5),
        ("John", "Doe", 0, 5),
        ("John", "Doe", 50000, -1),
        ( "", "Doe", 50000, -1),
    ])    
    def test_add_employee_with_invalid_data(self, first_name, last_name, base_salary, experience):
        with pytest.raises(ValueError):
            Employee(first_name, last_name, base_salary, experience)
            
            
@pytest.mark.salary_calculation_tests
class TestSalaryCalculation:
    @pytest.mark.parametrize("base_salary, experience, expected", [
        (1000, 0, 1000),
        (1500, 1, 1500),
        (2000, 2, 2200)
    ])
    def test_salary_calculation_experience_two_or_less(self, base_salary, experience, expected):
        employee = Employee("John", "Doe", base_salary, experience)

        assert employee.salary_calculation() == expected, "Calculated salary is not as expected."
    