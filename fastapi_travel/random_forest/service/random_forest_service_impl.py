import os

import pandas as pd

from random_forest.service.random_forest_service import RandomForestService


class RandomForestServiceImpl(RandomForestService):


    def readExcel(self):
        currentDirectory = os.getcwd()
        print(f"currentDirectory: {currentDirectory}")

        filePath = os.path.join(
            currentDirectory, "..", "assets"
        )

        df_1 = pd.read_excel(f'{filePath}/survey_data.xlsx')
        df_2 = pd.read_excel(f'{filePath}/travel_orders_data.xlsx')
        df_3 = pd.read_excel(f'{filePath}/preprocessed_orders_data.xlsx')

    def randomForestAnalysis(self):
        pass