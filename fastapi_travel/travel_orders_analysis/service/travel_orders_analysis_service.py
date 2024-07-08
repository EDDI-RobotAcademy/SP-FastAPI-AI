from abc import ABC, abstractmethod

class TravelOrdersAnalysisService(ABC):

    @abstractmethod
    def trainModel(self):
        pass