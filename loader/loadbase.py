from abc import ABC, abstractmethod

class LoadBase(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError