import os

import pandas as pd

from random_forest.repository.random_forest_repository_impl import RandomForestRepositoryImpl
from random_forest.service.random_forest_service import RandomForestService


class RandomForestServiceImpl(RandomForestService):
    def __init__(self):
        self.__randomForestRepository = RandomForestRepositoryImpl()

    def readcsv(self):
        currentDirectory = os.getcwd()
        print(f"currentDirectory: {currentDirectory}")

        filePath = os.path.join(
            currentDirectory, "..", "assets", "preprocessed_orders_data.xlsx"
        )

        dataFrame = pd.read_csv(filePath)
        return dataFrame


    def randomForestAnalysis(self):
        dataFrame = self.readCsv()
        dataEncoded, labelEncoders = (self.__randomForestRepository.ordersCategoricalVariableEncoding(dataFrame))

