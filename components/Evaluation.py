from components.Training import *
from components.Ingestion import *
from components.Transformation import *
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import r2_score


class Evaluation:
    def __init__(self):
        self.feature_selection = Training().Feature_selection()

    # Initialize the XGBoost regressor
    def Metric(self):
        try:
            _, _, x_test, _, y_test = self.feature_selection

            # called best feature selection model and transform test data
            Feature_selection = load_feature_selection_model()
            x_test_selected = Feature_selection.transform(x_test)

            # scaling test data
            STDS = StandardScaler()
            test_feature = STDS.fit_transform(x_test_selected)

            # print(test_feature.shape)

            # Apply Unsupervised Learning (K-means Clustering) on the test data by calling knn model as
            cluster_data = load_cluster_model()
            cluster_assignments_test = cluster_data.fit_predict(test_feature)
        
            # Step 4: Combine Cluster Assignments with Original Features for testing sets
            X_test_combined = np.column_stack((x_test_selected, cluster_assignments_test))

            # Predict the target variable on the test set by calling xgboost model
            xgboost_model = load_xgboost_model()
            y_preds = xgboost_model.predict(X_test_combined)

            # performance metric mean square error:
            mean_sq_error = mse(y_test, y_preds)
            logging.info(f"mean_square_error : {np.round(mean_sq_error, 1)}")

            # Root mean squared error:
            rmse = np.sqrt(mean_sq_error)
            logging.info(f"Root_mean_squared_error:{np.round(rmse, 1)}")

            # performance metric mean absolute error:
            mean_abs_error = mae(y_test, y_preds)
            rounded_mae = round(mean_abs_error, 1)
            logging.info(f"mean_absolute_error : {rounded_mae}")

            # Calculate R-squared
            r_squared = r2_score(y_test, y_preds)
            rounded_r_squared = round(r_squared, 1)
            logging.info(f"R-squared: {rounded_r_squared}")

            # Calculate Adjusted R-squared
            p = 4
            n = len(y_test)
            adjusted_r_squared = 1 - ((1 - r_squared) * (n - 1) / (n - p - 1))

            logging.info(f"Adjusted R-squared: {np.round(adjusted_r_squared, 2)}")

        except Exception as e:
            raise Exception(f"evaluation Prediction", e)




