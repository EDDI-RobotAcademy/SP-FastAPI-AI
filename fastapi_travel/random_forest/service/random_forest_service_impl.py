import os

import pandas as pd

from random_forest.controller.reponse_form.random_forest_response_form import RandomForestResponseForm
from random_forest.repository.random_forest_repository_impl import RandomForestRepositoryImpl
from random_forest.service.random_forest_service import RandomForestService


class RandomForestServiceImpl(RandomForestService):
    def __init__(self):
        self.__randomForestRepository = RandomForestRepositoryImpl()

    def readExcel(self):
        currentDirectory = os.getcwd()
        print(f"currentDirectory: {currentDirectory}")

        filePath = os.path.join(
            currentDirectory, "..", "assets", "preprocessed_orders_data.xlsx"
        )

        dataFrame = pd.read_excel(filePath)
        return dataFrame

    def featureTargetVariableDefinition(self, dataEncoded):
        X = dataEncoded.drop('travelId', axis=1)
        y = dataEncoded['travelId']

        return X, y


    def randomForestAnalysis(self):
        dataFrame = self.readExcel()
        # dataEncoded, labelEncoders = (self.__randomForestRepository.ordersCategoricalVariableEncoding(dataFrame))

        X, y = self.featureTargetVariableDefinition(dataFrame)
        X_train, X_test, y_train, y_test = (
            self.__randomForestRepository.splitTrainTestSet(X, y))
        randomForestModel = self.__randomForestRepository.train(X_train, y_train)
        y_pred = self.__randomForestRepository.predict(randomForestModel, X_test)
        accuracy, report, confusionMatrix = (self.__randomForestRepository.evaluate(y_test, y_pred))

        X_resampled, y_resampled = self.__randomForestRepository.applySmote(X_train, y_train)
        randomForestModelAfterSmote = self.__randomForestRepository.train(X_resampled, y_resampled)
        y_pred_after_smote = (
            self.__randomForestRepository.predict(randomForestModelAfterSmote, X_test))

        moteAccuracy, smoteReport, smoteConfusionMatrix = (
            self.__randomForestRepository.evaluate(y_test, y_pred_after_smote))




        return RandomForestResponseForm.createForm(
            confusionMatrix,smoteConfusionMatrix, y_test, y_pred,  y_pred_after_smote, dataFrame,
        )