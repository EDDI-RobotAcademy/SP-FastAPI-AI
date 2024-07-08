from travel_orders_analysis.repository.travel_orders_analysis_repository import TravelOrdersAnalysisRepository


class TravelOrdersAnalysisRepositoryImpl(TravelOrdersAnalysisRepository):

    def trainModel(self):
        print("repository -> trainModel()")