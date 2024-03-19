
class Student:
    def read(self):
        print("They are fighting")

    def write(self):
        print("we are watching.")  # print() is python fucntion

class Teacher(Student):  # Inheritance, teacher is a student too.  Child(Super, A)
    pass

obj = Teacher()
obj.read()  # mehtod call
obj.write()
