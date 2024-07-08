from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

from travel_orders_analysis.service.travel_orders_analysis_service_impl import TravelOrdersAnalysisServiceImpl

travelOrdersAnalysisRouter = APIRouter()

async def injectTravelOrdersAnalysisService() -> TravelOrdersAnalysisServiceImpl:
    return TravelOrdersAnalysisServiceImpl()

@travelOrdersAnalysisRouter.get("/orders-train")
async def travelOrdersTrain(travelOrdersAnalysisService : TravelOrdersAnalysisServiceImpl
                            =Depends(injectTravelOrdersAnalysisService)):

    print("controller -> orders-train")
    travelOrdersAnalysisService.trainModel()