class Kangaroo:
    """
    Represents the name and pouch contents of a kangaroo.
    attributes: name, gender, pouch_contents
    """

    def __init__(self, name, gender, pouch_contents=None):
        self.name = name
        self.gender = gender
        self.pouch_contents = pouch_contents or []

    def __str__(self):
        return "This kangaroo is named {}, {}, and his pouch contents are: {}.".format(self.name, self.gender, self.pouch_contents)

    def __eq__(self, other):
        return self.gender == other.gender

    def put_in_pouch(self, item):
        """
        Adds a new item to the pouch of the kangaroo.
        """
        self.pouch_contents.append(item)

jack = Kangaroo("Jack", "male")
kyle = Kangaroo("Kyle", "male")

jack.put_in_pouch("OneCard")
jack.put_in_pouch("License")
jack.put_in_pouch("Coat")
kyle.put_in_pouch("License")
kyle.put_in_pouch("Water")
kyle.put_in_pouch("Food")

print(jack)
print(kyle)
print(jack == kyle)



