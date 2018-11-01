class Students:
    """
    Represents the name, age, and grades of a student.
    attributes: name, age, grades
    """
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades or []

    def __str__(self):
        return "This student is named {}, they are {} years old, and have the following grades: {}.".format(self.name, self.age, self.grades)

    def __eq__(self, other):
        return self.age == other.age

    def __len__(self):
        return len(self.grades)

    def add_a_grade(self, item):
        self.grades.append(item)

christian = Students("Christian", 21)
jack = Students("Jack", 21)

christian.add_a_grade("90")
christian.add_a_grade("85")
christian.add_a_grade("100")

jack.add_a_grade("100")
jack.add_a_grade("98")
jack.add_a_grade("80")

print(christian)
print(jack)
print(christian==jack)
print(len(christian))




