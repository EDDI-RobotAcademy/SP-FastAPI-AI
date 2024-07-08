from abc import ABC, abstractmethod

class RandomForestService(ABC):
    @abstractmethod
    def readExcel(self):
        pass

    @abstractmethod
    def randomForestAnalysis(self):
        pass