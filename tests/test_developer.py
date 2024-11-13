import pytest
import coverage
from models import *

@pytest.mark.developer_initialization_tests
class TestdeveloperInitialization:
    @pytest.mark.parametrize("first_name, last_name, base_salary, experience", [
        ("Ivan", "Ivanov", 2000, 0),
        ("Petko", "Petkov", 5000, 3),
        ("Kiril", "Kirilov", 10000, 7)
    ])
    
    
    
    def test_add_developer_with_valid_data(self, first_name, last_name, base_salary, experience):
        developer = Developer(first_name, last_name, base_salary, experience)
        assert developer is not None
        assert isinstance(developer, Developer)
        
        assert developer.first_name == first_name
        assert developer.last_name == last_name
        assert developer.base_salary == base_salary
        assert developer.experience == experience



    @pytest.mark.parametrize("first_name, last_name, base_salary, experience", [
        ("J0hn", "Doe", 50000, 5),
        ("John", "Doe@#", 50000, 5),
        ("John", "Doe", -256, 5),
        ("John", "Doe", 0, 5),
        ("John", "Doe", 50000, -1),
        ( "", "Doe", 50000, -1)
    ])    
    def test_add_developer_with_invalid_data(self, first_name, last_name, base_salary, experience):
        with pytest.raises(ValueError):
            Developer(first_name, last_name, base_salary, experience)
            
            
@pytest.mark.developer_salary_calculation_tests
class TestSalaryCalculation:
    @pytest.mark.parametrize("base_salary, experience, expected", [
        (1000, 0, 1000),
        (1500, 1, 1500)
    ])
    def test_salary_calculation_experience_less_than_two_years(self, base_salary, experience, expected):
        developer = Developer("John", "Doe", base_salary, experience)
        calculated_salary = developer.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
        
    @pytest.mark.parametrize("base_salary, experience, expected", [
        (1000, 2, 1200),
        (1000, 5, 1200),
        (1500, 2, 1700),
        (1500, 5, 1700),
    ])
    def test_salary_calculation_experience_two_to_five_years(self, base_salary, experience, expected):
        developer = Developer("John", "Doe", base_salary, experience)
        calculated_salary = developer.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
        
    @pytest.mark.parametrize("base_salary, experience, expected", [
        (1000, 6, 1700),
        (1000, 10, 1700),
        (1500, 6, 2300),
        (1500, 10, 2300)
    ])
    def test_salary_calculation_experience_two_to_five_years(self, base_salary, experience, expected):
        developer = Developer("John", "Doe", base_salary, experience)
        calculated_salary = developer.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
        
def test_developer_to_dict():
    developer = Developer("Ivaylo", "Ivanov", 60000, 3)
    dev_dict = developer.to_dict()
    expected_dict = {
            "first_name": "Ivaylo",
            "last_name": "Ivanov",
            "base_salary": 60000,
            "experience": 3,
            "type": "Developer"
    }
    assert dev_dict == expected_dict
    
