class Human:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

        def full_name(self):
            return self.name + " " + self.last_name

class Student(Human):
    def __init__(self, name, last_name, score):
        self.name = name
        self.last_name = last_name
        self.score = score

        def full_name(self):
            return "Student: " + self.name + " " + self.last_name

        def say_hello(self):

            print("Hello, " + self.name)

human1 = Human("Dima", "Last Name")
student_dima = Student("Dima", "Student", 34)
print(student_dima.full_name())