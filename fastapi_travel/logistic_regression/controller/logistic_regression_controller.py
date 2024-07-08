import os

import numpy as np
import pandas as pd
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

logisticRegressionRouter = APIRouter()

@logisticRegressionRouter.get("/logistic-regression")
async def logistic_regression_test():
    currentDirectory = os.getcwd()
    print(f"currentDirectory: {currentDirectory}")

    filePath = os.path.join(
        currentDirectory, "..", "assets"
    )

    print("logistic_regression_test()")

    df_1 = pd.read_excel(f'{filePath}/survey_data.xlsx')
    df_2 = pd.read_excel(f'{filePath}/travel_orders_data.xlsx')

    merged_df = pd.merge(df_1, df_2, on='accountId')
    merged_df = merged_df.drop_duplicates(subset=['accountId', 'travelId'])

    print(merged_df)

    X = merged_df.drop('travelId', axis=1)
    y =merged_df['travelId']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    coef = model.coef_
    intercept = model.intercept_

    x_values = np.linspace(X.iloc[:, 0].min(), X.iloc[:, 0].max(), 100)
    y_values = -(coef[0][0] * x_values + intercept[0] / coef[0][1])

    return JSONResponse(content={
        "accuracy": accuracy,
        "coefficients": coef.tolist(),
        "intercept": intercept.tolist(),
        "data_point": {
            "X": X.values.tolist(),
            "y": y.values.tolist()
        },
        "decision_boundary": {
            "x_values": x_values.tolist(),
            "y_values": y_values.tolist()
        }
    })