from abc import ABC, abstractmethod


class TankInterface(ABC):

    @abstractmethod
    def redraw(self, screen):
        pass

    def hit(self):
        print('hit')
