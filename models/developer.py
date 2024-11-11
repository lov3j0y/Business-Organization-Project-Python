from .employee import Employee

class Developer(Employee):
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Developer"  # Adding type to help with deserialization
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"]
        )