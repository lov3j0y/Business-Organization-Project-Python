import pytest
import json
import os
from models import *

@pytest.mark.department_initialization_tests
class TestDepartmentInitialization:
    def test_default_initialization(self):
        department = Department()
        assert department.name == ""
        assert department.managers == []

    def test_named_initialization(self):
        department = Department(name="IT")
        assert department.name == "IT"
        assert department.managers == []

@pytest.mark.department_add_manager_tests
class TestDepartmentAddManager:    
    def test_add_valid_manager(self):
        department = Department(name="IT")
        manager = Manager("Alice", "Smith", 1500, 10)
        
        department.add_manager(manager)
        
        assert len(department.managers) == 1
        assert department.managers[0] == manager

    def test_add_invalid_manager(self):
        department = Department(name="IT")        
        with pytest.raises(TypeError, match="Only employees of type Manager can be added to the department."):
            department.add_manager("Not a Manager")

@pytest.mark.department_give_salary_tests
class TestDepartmentGiveSalary:    
    def test_give_salary_prints_correctly(self, capsys):
        department = Department(name="IT")
        manager = Manager("Alice", "Smith", 1500, 10)
        dev = Developer("Dev", "Jones", 1000, 3)
        designer = Designer("Des", "Taylor", 1200, 4, 0.9)
        
        
        department.add_manager(manager)
        manager.add_team_members(dev)
        manager.add_team_members(designer)        
       
        department.give_salary()
        
        captured = capsys.readouterr()
        
        assert "Alice Smith" in captured.out
        assert "Dev Jones" in captured.out
        assert "Des Taylor" in captured.out


class TestDepartmentPrintDepartmentTeams:    
    def test_print_department_teams(self, capsys):
        department = Department(name="IT")
        manager = Manager("Alice", "Smith", 1500, 10)
        dev = Developer("Dev", "Jones", 1000, 3)
        designer = Designer("Des", "Taylor", 1200, 4, 0.9)
        
        department.add_manager(manager)
        manager.add_team_members(dev)
        manager.add_team_members(designer)
        
        department.print_department_teams()
        
        captured = capsys.readouterr()
       
        assert "Department: IT" in captured.out
        assert "Manager: Alice Smith" in captured.out
        assert "Developer" in captured.out
        assert "Designer" in captured.out

@pytest.mark.department_serialization_tests
class TestDepartmentSerialization:    
    def test_save_employees(self, tmpdir):
        department = Department(name="IT")
        manager = Manager("Alice", "Smith", 1500, 10)
        dev = Developer("Dev", "Jones", 1000, 3)
        designer = Designer("Des", "Taylor", 1200, 4, 0.9)
        
        department.add_manager(manager)
        manager.add_team_members(dev)
        manager.add_team_members(designer)
        
        filepath = tmpdir.join("employees.json")
        
        department.save_employees(filepath)
        
        assert os.path.exists(filepath)
        
        with open(filepath, 'r') as file:
            data = json.load(file)
            assert len(data) == 1
            assert data[0]["first_name"] == "Alice"
            assert data[0]["team"][0]["first_name"] == "Dev"
            assert data[0]["team"][1]["first_name"] == "Des"
    
    def test_load_employees(self, tmpdir):
        data = [
            {
                "type": "Manager",
                "first_name": "Alice",
                "last_name": "Smith",
                "base_salary": 1500,
                "experience": 10,
                "team": [
                    {
                        "type": "Developer",
                        "first_name": "Dev",
                        "last_name": "Jones",
                        "base_salary": 1000,
                        "experience": 3
                    },
                    {
                        "type": "Designer",
                        "first_name": "Des",
                        "last_name": "Taylor",
                        "base_salary": 1200,
                        "experience": 4,
                        "eff_coeff": 0.9
                    }
                ]
            }
        ]
        
        filepath = tmpdir.join("employees.json")
        with open(filepath, 'w') as file:
            json.dump(data, file)
        
        department = Department(name="IT")
        department.load_employees(filepath)
        
        assert len(department.managers) == 1
        manager = department.managers[0]
        assert manager.first_name == "Alice"
        assert len(manager.team) == 2
        assert isinstance(manager.team[0], Developer)
        assert manager.team[0].first_name == "Dev"
        assert isinstance(manager.team[1], Designer)
        assert manager.team[1].first_name == "Des"

    def test_load_employees_file_not_found(self, capsys):
        department = Department(name="IT")
        
        department.load_employees("non_existent_file.json")
        
        captured = capsys.readouterr()
        
        assert "Error: File non_existent_file.json not found." in captured.out

    def test_load_employees_json_decode_error(self, tmpdir, capsys):       
        filepath = tmpdir.join("employees.json")
        with open(filepath, 'w') as file:
            file.write("corrupt data")
        
        department = Department(name="IT")
        department.load_employees(filepath)
        
        captured = capsys.readouterr()
        
        assert "Error decoding JSON from file" in captured.out
