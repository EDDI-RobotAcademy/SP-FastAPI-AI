from travel_orders_analysis.repository.travel_orders_analysis_repository_impl import TravelOrdersAnalysisRepositoryImpl
from travel_orders_analysis.service.travel_orders_analysis_service import TravelOrdersAnalysisService


class TravelOrdersAnalysisServiceImpl(TravelOrdersAnalysisService):

    def __init__(self):
        self.travelOrdersAnalysisRepositoryImpl = TravelOrdersAnalysisRepositoryImpl()
    def trainModel(self):
        print("service -> trainModel()")
        self.travelOrdersAnalysisRepositoryImpl.trainModel()
