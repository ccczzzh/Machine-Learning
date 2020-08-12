class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        #Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


print(Person.number_of_people_())
p1 = Person('Tim')
print(Person.number_of_people_())
p2 = Person('Bill')
print(Person.number_of_people_())