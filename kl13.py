import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to {self.id}")


if __name__ == '__main__':
    p1 = Person("JAcek", "Kowalski", 1)
    print(p1)  # Person(first_name='JAcek', last_name='Kowalski', id=1)
    p1.greet()

    people = [
        Person("Jacek", "Dobrowolski", 1),
        Person("Mateusz", "Zegar", 2)
    ]
    print(people)
    print(people[0])

    with open('data.pickle', 'wb') as stream:
        pickle.dump(people, stream)
