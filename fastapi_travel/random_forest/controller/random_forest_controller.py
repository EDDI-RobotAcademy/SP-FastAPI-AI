from fastapi import APIRouter, Depends

from random_forest.service.random_forest_service_impl import RandomForestServiceImpl

randomForestRouter = APIRouter()

async def injectRandomForestService() -> RandomForestServiceImpl:
    return RandomForestServiceImpl()

@randomForestRouter.get('/random-forest')
async def randomForest(randomForestService: RandomForestServiceImpl =
                       Depends(injectRandomForestService)):
    randomForestService.randomForestAnalysis()