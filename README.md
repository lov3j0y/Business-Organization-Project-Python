# **Organization Employee Management System**

This project implements a structured model for an organization, featuring Developers, Designers, and Managers as unique employee types. It includes a **Department** model for calculating salaries, managing teams, and enabling JSON-based data persistence.

---

## **Features**

### **1. Employee Model**

The employee model supports three distinct employee types, each with unique properties:

- **Developer**
- **Designer**
  - **Additional field**: `eff_coeff` — efficiency coefficient (decimal between 0 and 1)
- **Manager**
  - **Optional field**: `team` — a list of Developers and Designers

All employee classes share these core fields:
- **`first_name`**: First name
- **`last_name`**: Last name
- **`base_salary`**: Base salary
- **`experience`**: Years of experience

---

### **2. Salary Calculation**

The `Department` class provides a **`give_salary()`** method, calculating and displaying employee salaries based on role, experience, and additional criteria.

#### **General Rules (all employees)**:
- **Experience > 2 years**: `base_salary + 200`
- **Experience > 5 years**: `base_salary * 1.2 + 500`

#### **Role-Specific Rules**:
- **Designer**: `counted_salary` is multiplied by the efficiency coefficient (`eff_coeff`).
- **Manager**:
  - Teams with **5+ employees**: `counted_salary + 200`
  - Teams with **10+ employees**: `counted_salary + 300`
  - If over half the team consists of Developers: Salary increases by an **additional 10%**.

**Note:** Salaries are rounded to the nearest integer and displayed in this format:
```plaintext
<first_name> <last_name> received <salary> money.
```

---

### **3. Department Management**

The **Department** class maintains a list of `Manager` objects, each with their respective teams of Designers and Developers.

- **Team structure**: Each Manager manages an arbitrary number of Developers and Designers.
- **Salary distribution**: The Department can calculate and print the salary for each employee in the organization.

---

### **4. Data Persistence**

The Department class supports saving and loading employee data through JSON:

- **`save_employees(filename)`**: Serializes and saves the list of managers (and their teams) to a JSON file.
- **`load_employees(filename)`**: Loads and deserializes data from a JSON file, restoring the list of managers and their employees. If the specified file is not found, a friendly error message is displayed.

---

## **Unit Testing**

This project includes **unit tests** for verifying:
- Employee creation
- Salary calculation
- Team management
- JSON serialization/deserialization

**Tests** can be run using either the `unittest` or `pytest` framework.

---

## **Contributing**

Contributions are welcome! Please submit issues or pull requests as needed.

---

This project offers a robust model for organizational structure and employee management, making it a valuable tool for HR systems, payroll processing, and organizational data modeling.
