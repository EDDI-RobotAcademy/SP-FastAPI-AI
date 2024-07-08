from abc import ABC, abstractmethod

class TravelOrdersAnalysisRepository(ABC):

    @abstractmethod
    def trainModel(self):
        pass