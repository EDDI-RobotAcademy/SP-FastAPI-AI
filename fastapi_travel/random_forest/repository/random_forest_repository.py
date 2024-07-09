from abc import ABC, abstractmethod

class RandomForestRepository(ABC):
    @abstractmethod
    def ordersCategoricalVariableEncoding(self, dataFrame):
        pass