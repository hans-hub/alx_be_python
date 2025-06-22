class Person:
    count = 0  # Class variable to count instances

    def __init__(self, name):
        self.name = name
        Person.count += 1  # Increment count on instance creation

    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")

# Usage
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Hans")
Person.display_count()  # Output: Total persons created: 2