# Name - Moksh Malik
# Enrollment Number - E22MCAG0020

from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
