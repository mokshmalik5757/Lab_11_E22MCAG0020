# Name - Moksh Malik
# Enrollment Number - E22MCAG0020

from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass
