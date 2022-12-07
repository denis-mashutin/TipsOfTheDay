from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def talk(self):
        pass