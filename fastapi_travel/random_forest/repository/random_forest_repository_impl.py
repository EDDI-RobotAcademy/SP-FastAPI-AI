from sklearn.preprocessing import LabelEncoder

from random_forest.repository.random_forest_repository import RandomForestRepository


class RandomForestRepositoryImpl(RandomForestRepository):

    def ordersCategoricalVariableEncoding(self, dataFrame):
        labelEncoders = {}
        categoricalColumns = ['aga', 'gender', 'travelConcept', 'travelCompanion', 'snsFrequency', 'photoFrequency', 'travelBudget']

        for column in categoricalColumns:
            labelEncoders[column] = LabelEncoder()
            dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])

        return dataFrame, labelEncoders