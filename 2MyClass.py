class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, " + self.name)

student_dima = Student("Dima", 34)
student_dima.say_hello()
print("Age: " + str(student_dima.age))

