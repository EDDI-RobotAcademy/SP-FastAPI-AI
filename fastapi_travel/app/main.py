import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kmeans.controller.kmeans_controller import kmeansRouter
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from random_forest.controller.random_forest_controller import randomForestRouter
from travel_orders_analysis.controller.travel_orders_analysis_controller import travelOrdersAnalysisRouter

app = FastAPI()


# .env 세팅
load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

app.include_router(travelOrdersAnalysisRouter)
app.include_router(logisticRegressionRouter)
app.include_router(randomForestRouter)
app.include_router(kmeansRouter)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=33333) # 127.0.0.1 -> 자기 ipv4 주소로 변경