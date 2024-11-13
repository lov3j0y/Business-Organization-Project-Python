import pytest
from models import *

@pytest.mark.manager_initialization_tests
class TestManagerInitialization:    
    def test_manager_valid_initialization(self):
        manager = Manager("Ivan", "Ivanov", 1500, 10)
        
        assert manager.first_name == "Ivan"
        assert manager.last_name == "Ivanov"
        assert manager.base_salary == 1500
        assert manager.experience == 10
        assert manager.team == []

    def test_custom_team_initialization(self):
        team = [
            Developer("Dev", "User", 5000, 5),
            Designer("Des", "User", 4000, 4, 0.8)
        ]
        manager = Manager("Manager", "Managerov", 1500, 10, team)
        
        assert manager.team == team
        assert len(manager.team) == 2
        assert isinstance(manager.team[0], Developer)
        assert isinstance(manager.team[1], Designer)

    @pytest.mark.parametrize("first_name, last_name, base_salary, experience, exception", [
        (123, "Doe", 1500, 10, TypeError),
        ("John", 456, 1500, 10, TypeError),
        ("Ivan", "Iavnov", "1500", 10, TypeError),
        ("Petko", "Petkov", 1500, "10", TypeError),
        ("", "Doe", 1500, 10, ValueError),
        ("John", "", 1500, 10, ValueError),
        ("John", "Johnson", -1500, 10, ValueError),
        ("John", "Johnson", 1500, -1, ValueError)
    ])
    def test_invalid_initialization(self, first_name, last_name, base_salary, experience, exception):
        with pytest.raises(exception):
            Manager(first_name, last_name, base_salary, experience)
            
@pytest.mark.manager_salary_calculation_tests
class TestSalaryCalculation:            
    @pytest.mark.parametrize("base_salary, experience, team_size, developer_count, expected_final_salary", [
        (1000, 5, 0, 0, 1200),
        (1000, 5, 5, 0, 1200),
        (1000, 5, 6, 0, 1400),
        (1000, 5, 11, 0, 1500),
        (1000, 3, 5, 3, 1320),
        (1000, 3, 6, 3, 1400),
        (1000, 7, 6, 4, 2090)
    ])
    def test_salary_calculation(self, base_salary, experience, team_size, developer_count, expected_final_salary):
        manager = Manager('John', 'Doe', base_salary, experience)
        
        for _ in range(developer_count):
            manager.add_team_members(Developer('Dev', 'User', 5000, 3))
        
        for _ in range(team_size - developer_count):
            manager.add_team_members(Designer('Des', 'User', 4000, 3, 0.9))
        
        calculated_salary = manager.salary_calculation()
        
        assert calculated_salary == expected_final_salary

@pytest.mark.manager_team_management_tests
class TestManagerTeamManagement:
    
    def test_add_valid_team_members(self):
        manager = Manager("John", "Doe", 1000, 5)
        developer = Developer("Dev", "User", 5000, 3)
        designer = Designer("Des", "User", 4000, 3, 0.85)
        
        manager.add_team_members(developer)
        manager.add_team_members(designer)
        
        assert developer in manager.team
        assert designer in manager.team

    def test_add_invalid_team_member(self):
        manager = Manager("John", "Doe", 1000, 5)
        
        with pytest.raises(TypeError):
            manager.add_team_members("Invalid Member")

    def test_print_team_members(self, capsys):
        manager = Manager("John", "Doe", 1000, 5)
        developer = Developer("Dev", "User", 5000, 3)
        designer = Designer("Des", "User", 4000, 3, 0.9)
        
        manager.add_team_members(developer)
        manager.add_team_members(designer)
        
        manager.print_team_members()
        
        captured = capsys.readouterr()
        assert "Dev User" in captured.out
        assert "Des User" in captured.out

@pytest.mark.manager_serialization_tests
class TestManagerSerialization:

    def test_manager_to_dict(self):
        manager = Manager("John", "Doe", 1000, 5)
        developer = Developer("Dev", "User", 5000, 3)
        designer = Designer("Des", "User", 4000, 3, 0.85)
        
        manager.add_team_members(developer)
        manager.add_team_members(designer)
        
        manager_dict = manager.to_dict()
        
        assert manager_dict["first_name"] == "John"
        assert len(manager_dict["team"]) == 2
        assert manager_dict["team"][0]["type"] == "Developer"
        assert manager_dict["team"][1]["type"] == "Designer"
        assert manager_dict["team"][1]["eff_coeff"] == 0.85

    def test_manager_from_dict(self):
        manager_data = {
            "first_name": "John",
            "last_name": "Doe",
            "base_salary": 1000,
            "experience": 5,
            "team": [
                {"type": "Developer", "first_name": "Dev", "last_name": "User", "base_salary": 5000, "experience": 3},
                {"type": "Designer", "first_name": "Des", "last_name": "User", "base_salary": 4000, "experience": 3, "eff_coeff": 0.85}
            ]
        }
        
        manager = Manager.from_dict(manager_data)
        
        assert manager.first_name == "John"
        assert len(manager.team) == 2
        assert isinstance(manager.team[0], Developer)
        assert isinstance(manager.team[1], Designer)
        assert manager.team[1].eff_coeff == 0.85
