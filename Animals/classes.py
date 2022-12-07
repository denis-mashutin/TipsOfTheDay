from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def talk(self):
        pass


class Dog(Animal):

    def talk(self):
        print("I say 'WOOF'.")


class Cat(Animal):
    pass


class Human(Animal):

    pass

