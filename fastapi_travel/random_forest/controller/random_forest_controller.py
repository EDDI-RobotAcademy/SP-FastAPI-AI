from fastapi import APIRouter, Depends

randomForestRouter = APIRouter()

async def injectRandomForestService() -> RandomForestServiceImpl:
    return RandomForestServiceImpl()

@randomForestRouter.get('/random-forest')
async def randomForest(randomForestService: RandomForestServiceImpl =
                       Depends(injectRandomForestService)):
    randomForestService.randomForestAnalysis()