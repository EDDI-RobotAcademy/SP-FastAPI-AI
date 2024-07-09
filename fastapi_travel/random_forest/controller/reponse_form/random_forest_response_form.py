class RandomForestResponseForm:
    @staticmethod
    def createForm(confusionMatrix, smoteConfusionMatrix, y_test, y_pred, y_pred_after_smote, data):
        common_info = {
            "t_age": data[['age', 'travelId']].to_dict(orient='records'),
            't_gender': data[['gender', 'travelId']].to_dict(orient='records'),
            't_travelConcept': data[['travelConcept', 'travelId']].to_dict(orient='records'),
            't_travelCompanion': data[['travelCompanion', 'travelId']].to_dict(orient='records'),
            't_snsFrequency': data[['snsFrequency', 'travelId']].to_dict(orient='records'),
            't_photoFrequency': data[['photoFrequency', 'travelId']].to_dict(orient='records'),
            't_travelBudget': data[['travelBudget', 'travelId']].to_dict(orient='records')
        }

        y_test_list = y_test.tolist()

        confusionMatrixBeforeSmote = {
            'confusion_matrix': confusionMatrix.tolist(),
            'y_test': y_test_list,
            'y_pred': y_pred.tolist()
        }

        confusionMatrixAfterSmote = {
            'confusion_matrix': smoteConfusionMatrix.tolist(),
            'y_test': y_test_list,
            'y_pred': y_pred_after_smote.tolist()
        }

        return {
            'confusion_matrix_info_before_smote': confusionMatrixBeforeSmote,
            'confusion_matrix_info_after_smote': confusionMatrixAfterSmote,
            'common_info': common_info
        }