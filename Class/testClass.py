class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def display_info(self):
        student_info =  f"{self.name} {self.age}"
        return student_info
    



newStudent= Student("kofi",45)
print(newStudent.name)
print(newStudent.age)