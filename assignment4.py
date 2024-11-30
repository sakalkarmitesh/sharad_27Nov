"""
Problem Statement
TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback.
An instructor is allocated a course, if he/she satisfies the below two conditions:
eligibility criteria:
* If experience is more than 3 years, average feedback should be 4.5 or more If experience Is 3 years or less, average feedback should be 4 or more
* he/she should posses the technology skill for the course

Identify the class name and attributes from the list of options below to represent instructors.
check eligibility()
avg_feedback experience
allocate_course()
Instructor_name
allocate_course(technolody)
_init()
Instructor
calculate_avg_feedback()
technology_skill

Write a Python program to implement the class chosen with its attributes and methods.

Note:

1. Consider all instance variables to be private and methods to be public 2.
5. Perform case sensitive string comparison
An Instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list 3. check eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false

4. allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false
Represent few objects of the class, Initialize instance variables using setter methods, invoke appropriate methods and test your program.
"""

class Instructor:
    def __init__(self, name):  # Corrected from _init_ to __init__
        self.__name = name
        self.__technology_skills = []
        self.__experience = 0
        self.__avg_feedback = 0

    def set_technology_skills(self, skills):
        self.__technology_skills = skills

    def set_experience(self, experience):
        self.__experience = experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def check_eligibility(self, technology):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        elif technology in self.__technology_skills:
            return True
        else:
            return False

    def allocate_course(self, technology):
        if self.check_eligibility(technology):
            print(f"Course allocated to {self.__name}")
            return True
        else:
            print(f"Course cannot be allocated to {self.__name}")
            return False

# Example usage:
instructor1 = Instructor("John Doe")
instructor1.set_technology_skills(["Python", "Java"])
instructor1.set_experience(5)
instructor1.set_avg_feedback(4.7)

instructor2 = Instructor("Jane Smith")
instructor2.set_technology_skills(["C++", "C#"])
instructor2.set_experience(2)
instructor2.set_avg_feedback(3.8)

instructor1.allocate_course("Python")  # Output: Course allocated to John Doe
instructor2.allocate_course("Java")   # Output: Course cannot be allocated to Jane Smith
