import pytest
from models import *

@pytest.mark.employee_initialization_tests
class TestEmployeeInitialization:
    @pytest.mark.parametrize("first_name, last_name, base_salary, experience", [
        ("Ivan", "Ivanov", 2000, 0),
        ("Petko", "Petkov", 5000, 3),
        ("Kiril", "Kirilov", 10000, 7)
    ])
    
    
    
    def test_add_employee_with_valid_data(self, first_name, last_name, base_salary, experience):
        employee = Employee(first_name, last_name, base_salary, experience)
        assert employee is not None
        assert isinstance(employee, Employee)
        
        assert employee.first_name == first_name
        assert employee.last_name == last_name
        assert employee.base_salary == base_salary
        assert employee.experience == experience



    @pytest.mark.parametrize("first_name, last_name, base_salary, experience", [
        ("J0hn", "Doe", 50000, 5),
        ("John", "Doe@#", 50000, 5),
        ("John", "Doe", -256, 5),
        ("John", "Doe", 0, 5),
        ("John", "Doe", 50000, -1),
        ( "", "Doe", 50000, -1)
    ])    
    def test_add_employee_with_invalid_data(self, first_name, last_name, base_salary, experience):
        with pytest.raises(ValueError):
            Employee(first_name, last_name, base_salary, experience)
            
            
@pytest.mark.employee_salary_calculation_tests
class TestSalaryCalculation:
    @pytest.mark.parametrize("base_salary, experience, expected", [
        (1000, 0, 1000),
        (1500, 1, 1500)
    ])
    def test_salary_calculation_experience_less_than_two_years(self, base_salary, experience, expected):
        employee = Employee("John", "Doe", base_salary, experience)
        calculated_salary = employee.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
        
    @pytest.mark.parametrize("base_salary, experience, expected", [
        (1000, 2, 1200),
        (1000, 5, 1200),
        (1500, 2, 1700),
        (1500, 5, 1700),
    ])
    def test_salary_calculation_experience_two_to_five_years(self, base_salary, experience, expected):
        employee = Employee("John", "Doe", base_salary, experience)
        calculated_salary = employee.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
        
    @pytest.mark.parametrize("base_salary, experience, expected", [
        (1000, 6, 1700),
        (1000, 10, 1700),
        (1500, 6, 2300),
        (1500, 10, 2300)
    ])
    def test_salary_calculation_experience_two_to_five_years(self, base_salary, experience, expected):
        employee = Employee("John", "Doe", base_salary, experience)
        calculated_salary = employee.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."

def test_employee_to_dict():
    employee = Employee("Ivaylo", "Ivanov", 60000, 3)
    emp_dict = employee.to_dict()
    expected_dict = {
            "first_name": "Ivaylo",
            "last_name": "Ivanov",
            "base_salary": 60000,
            "experience": 3,
            "type": "Employee"
    }
    
    assert emp_dict == expected_dict 
    
def test_employee_from_dict():    
    data = {
            "first_name": "Ivaylo",
            "last_name": "Ivanov",
            "base_salary": 60000,
            "experience": 3,
            "type": "Employee"
    }
    
    employee = Employee.from_dict(data)
    
    assert employee.first_name == data["first_name"]
    assert employee.last_name == data["last_name"]
    assert employee.base_salary == data["base_salary"]
    assert employee.experience == data["experience"]