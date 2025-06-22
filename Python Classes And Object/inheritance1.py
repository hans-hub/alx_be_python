class Shape:
    def calculate_area(self):
        print("This method should be overridden by subclasses.")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        print(f"The area of the rectangle is: {area}")


# Example usage
shape = Shape()
shape.calculate_area()  # Base class method

rectangle = Rectangle(5, 10)
rectangle.calculate_area()  # Overridden method in Rectangle
