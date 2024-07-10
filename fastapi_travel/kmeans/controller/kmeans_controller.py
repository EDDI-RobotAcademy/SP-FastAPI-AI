import os

import pandas as pd
from fastapi import APIRouter
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from kmeans.controller.response_form.kmeans_cluster_response_form import KmeansClusterResponseForm

kmeansRouter = APIRouter()

@kmeansRouter.get("/kmeans-test", response_model=KmeansClusterResponseForm)
async def kmeans_cluster_analysis():
    currentDirectory = os.getcwd()
    print(f"currentDirectory: {currentDirectory}")

    filePath = os.path.join(
        currentDirectory, "..", "assets", "preprocessed_orders_data.xlsx"
    )

    df = pd.read_excel(filePath)

    data = df[['travelConcept', 'travelId']]

    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    kmeans = KMeans(n_clusters=4, n_init=10)
    kmeans.fit(data_scaled)

    labels = kmeans.labels_.tolist()
    centers = scaler.inverse_transform(kmeans.cluster_centers_)
    points = data.values.tolist()

    print(f"point: {points}, labels: {labels}, centers: {centers}")

    return {"centers": centers.tolist(), "labels": labels, "points": points}











