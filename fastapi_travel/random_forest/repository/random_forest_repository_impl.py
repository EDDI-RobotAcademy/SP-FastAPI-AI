from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from random_forest.repository.random_forest_repository import RandomForestRepository


class RandomForestRepositoryImpl(RandomForestRepository):

    def ordersCategoricalVariableEncoding(self, dataFrame):
        labelEncoders = {}
        categoricalColumns = ['age', 'gender', 'travelConcept', 'travelCompanion', 'snsFrequency', 'photoFrequency', 'travelBudget']

        for column in categoricalColumns:
            labelEncoders[column] = LabelEncoder()
            dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])

        return dataFrame, labelEncoders

    def splitTrainTestSet(self, X, y):
        X_train, X_test, y_train, y_test = (train_test_split(X, y, test_size=0.2, random_state=42))

        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        randomForestModel = RandomForestClassifier(n_estimators=100, random_state=42)
        randomForestModel.fit(X_train, y_train)

        return randomForestModel

    def predict(self, randomForestModel, X_test):
        y_pred = randomForestModel.predict(X_test)

        return y_pred

    def evaluate(self, y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        classificationReport = classification_report(y_test, y_pred)
        confusionMatrix = confusion_matrix(y_test, y_pred)

        return accuracy, classificationReport, confusionMatrix

    def applySmote(self, X_train, y_train):
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

        return X_resampled, y_resampled





