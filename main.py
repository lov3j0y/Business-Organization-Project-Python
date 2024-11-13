from models import *

if __name__ == "__main__":
    # Example setup for production run
    dev = Developer("Ivaylo", "Ivanov", 60000, 3)
    des = Designer("Martin", "Petkov", 65000, 5, eff_coeff=1)
    mgr = Manager("Rumen", "Radev", 90000, 10, team=[dev, des])

    # Add manager to department
    dept = Department()
    dept.add_manager(mgr)

    # Save department to JSON
    dept.save_employees("data/employees.json")