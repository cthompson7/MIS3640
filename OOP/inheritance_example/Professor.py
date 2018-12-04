from BabsonPerson import BabsonPerson
from Person import Person

class Professor(BabsonPerson):

    def __init__(self, name, division):
        BabsonPerson.__init__(self, name)
        self.division = division

    def getDivision(self):
        return self.division

    def ProfessorSpeak(self, utterance):
        return Professor.speak(self, "Bro, " + utterance)


s1 = Professor('Zhi Li', "QTM Divison")
print(s1.ProfessorSpeak('Hello class.'))
