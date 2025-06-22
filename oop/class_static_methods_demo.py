class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Static method: doesn't need access to class or instance"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: uses 'cls' to access class-level attributes"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
