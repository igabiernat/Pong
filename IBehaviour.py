from abc import ABCMeta, abstractmethod

AllBehaviours = []  #przechowywanie wszystkich obiektów, na których ma się wykonać funkcja action


class IBehaviour:
    __metaclass__ = ABCMeta

    @abstractmethod     #deklaracja abstrakcyjnej funkcji
    def action(self): raise NotImplementedError
