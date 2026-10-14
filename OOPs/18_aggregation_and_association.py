"""Definition: Aggregation is a weak whole-part relationship, while association is a general relationship between two objects.

Explanation:
Association describes a relationship between objects, such as a Course being taught by a Teacher.
Aggregation is a special kind of association where one object contains or collects other objects, but the contained objects can still exist independently.
In this example, a Department aggregates Course objects.
"""


class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        return f"{self.name} is teaching"


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher  # Association


class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []  # Aggregation

    def add_course(self, course):
        self.courses.append(course)


teacher = Teacher("Mr. Kumar")
course = Course("Python OOP", teacher)
department = Department("Computer Science")
department.add_course(course)

print("Aggregation and Association")
print(course.teacher.teach())
print(department.courses[0].title)
