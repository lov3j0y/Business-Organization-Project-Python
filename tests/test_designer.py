import pytest
from models import *

@pytest.mark.designer_initialization_tests
class TestDesignerInitialization:
    @pytest.mark.parametrize("eff_coeff", [0, 0.5, 1])
    def test_designer_initialization_with_valid_eff_coeff(self, eff_coeff):
        des = Designer("Emil", "Emilov", 65000, 5, eff_coeff=eff_coeff)
        assert des.eff_coeff == eff_coeff

    @pytest.mark.parametrize("eff_coeff", [-1, 2])
    def test_designer_initialization_with_invalid_eff_coeff(self, eff_coeff):
        with pytest.raises(ValueError):
            Designer("Petko", "Petkov", 65000, 5, eff_coeff=eff_coeff)

@pytest.mark.designer_salary_calculation_tests
class TestSalaryCalculation:
    @pytest.mark.parametrize("base_salary, experience, eff_coeff, expected", [
        (1000, 0, 0, 0),
        (1000, 1, 0.5, 500),
        (1000, 1, 1, 1000)        
    ])
    def test_salary_calculation_experience_less_than_two_years(self, base_salary, experience,eff_coeff, expected):
        designer = Designer("John", "Doe", base_salary, experience, eff_coeff)
        calculated_salary = designer.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
        
    @pytest.mark.parametrize("base_salary, experience,eff_coeff, expected", [
        (1000, 2, 0, 0),
        (1000, 5, 1, 0),
        (1500, 2, 1, 0),
        (1500, 5, 0, 0),
    ])
    def test_salary_calculation_experience_two_to_five_years(self, base_salary, experience,eff_coeff, expected):
        designer = Designer("John", "Doe", base_salary, experience, eff_coeff)
        calculated_salary = designer.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
        
    @pytest.mark.parametrize("base_salary, experience, eff_coeff, expected", [
        (1000, 6, 0, 0),
        (1000, 6, 0.5, 850),
        (1000, 10, 1, 1700),
        (1000, 10, 0.5, 850),
        (1500, 6, 1, 2300),
        (1500, 10, 0, 0)
    ])
    def test_salary_calculation_experience_two_to_five_years(self, base_salary, experience, eff_coeff, expected):
        designer = Designer("John", "Doe", base_salary, experience, eff_coeff)
        calculated_salary = designer.salary_calculation()
        assert calculated_salary == expected, "Calculated salary is not as expected."
        
def test_designer_to_dict():
    des = Designer("Georgi", "Georgiev", 65000, 5, eff_coeff=1)
    des_dict = des.to_dict()
    expected_dict = {
            "first_name": "Georgi",
            "last_name": "Georgiev",
            "base_salary": 65000,
            "experience": 5,
            "eff_coeff": 1,
            "type": "Designer"
    }
    
    assert des_dict == expected_dict
