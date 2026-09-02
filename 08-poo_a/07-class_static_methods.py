class Person:
    species = 'Humano'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_specie(cls, new_specie):
        cls.species = new_specie


person1 = Person('Ricardo', 29)
print(person1.species)
Person.change_specie('Reptilianos')
print(person1.species)

person2 = Person('Fernando', 20)
print(person2.species)
