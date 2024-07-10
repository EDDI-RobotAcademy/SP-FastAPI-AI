import os

import numpy as np
import pandas as pd
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

logisticRegressionRouter = APIRouter()

@logisticRegressionRouter.get("/logistic-regression")
async def logistic_regression_test():
    currentDirectory = os.getcwd()
    print(f"currentDirectory: {currentDirectory}")

    filePath = os.path.join(
        currentDirectory, "..", "assets"
    )

    print("logistic_regression_test()")

    data= pd.read_excel(f'{filePath}/orders_data_after_drop_duplication.xlsx')
    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset='accountId')
    df = df[df['accountId'] < 200]
    # df = df.sample(n=00, random_state=1)

    df['y'] = (df['travelBudget'] >= 5).astype(int)
    df['x'] = (df['price'] >= 1000000).astype(int)

    X= df[['accountId','age', 'price', 'x']]
    y = df['y']




    print(df['y'].value_counts())
    X_df = X.copy()

    scaler = StandardScaler()
    X_standardized = scaler.fit_transform(X)


    X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.3, random_state=0)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    coef = model.coef_
    intercept = model.intercept_

    x_values = np.linspace(X_df.iloc[:, 0].min(), X_df.iloc[:, 0].max(), 100)
    y_values = -(coef[0][0] * x_values + intercept[0] / coef[0][1])

    print(y_values)


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