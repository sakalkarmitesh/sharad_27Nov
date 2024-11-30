"""
A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
* Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if
Age and marks are valid and Marks is 65 or more
Write a python program to represent the students seeking admission in the university.
The details of student class are given below.
"""

class Student:
    def _init_(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_age(self, age):
        self.__age = age

    def set_marks(self, marks):
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id

    def get_age(self):
        return self.__age

    def get_marks(self):
        return self.__marks

    def validate_age(self):
        if self._age is not None and self._age > 20:
            return True
        else:
            return False

    def validate_marks(self):
        if self._marks is not None and 0 <= self._marks <= 100:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks() and self.__marks >= 65:
            return True
        else:
            return False

# Example usage:
student1 = Student()
student1.set_student_id(12345)
student1.set_age(25)
student1.set_marks(75)

print(student1.get_student_id()) 
print(student1.get_age())       
print(student1.get_marks())     
if student1.check_qualification():
    print("Student is qualified for admission")
else:
    print("Student is not qualified for admission")