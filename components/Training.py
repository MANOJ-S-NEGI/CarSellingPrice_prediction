from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
from artifects_dir.path_artifect import *
from components.Transformation import *
from components.Ingestion import *
from log_dir.log import *
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.cluster import DBSCAN
import numpy as np
import joblib


class Training:
    def __init__(self):
        self.transformation = Transformation().Train_Test_Split()

    def Feature_selection(self):
        try:
            x_train, x_test, y_train, y_test = self.transformation
            Best_Parameters = {'max_depth': None,
                               'min_samples_split': 2,
                               'n_estimators': 50
                               }

            RFR_MODEL = RandomForestRegressor(**Best_Parameters)
            RFR_MODEL_FIT = RFR_MODEL.fit(x_train, y_train)

            # Perform feature selection
            SFM = SelectFromModel(RFR_MODEL_FIT, threshold=0.05)  # Adjust the threshold as needed
            SFM.fit(x_train, y_train)

            # make directory
            os.makedirs(MODEL_DIR, exist_ok=True)
            joblib.dump(SFM, FEATURE_SELECTION_MODEL_PATH)

            return SFM, x_train, x_test, y_train, y_test

        except Exception as e:
            raise Exception(f"Transformation feature selection : ", e)

    def Assignment_Trainer(self):
        try:
            SFM, x_train, _, y_train, _ = self.Feature_selection()

            # Transform the training
            x_train_selected = SFM.transform(x_train)
            logging.info(f"Best feature Extracted with threshold = 0.05")

            # Apply K-means Clustering
            STDS = StandardScaler()
            train_feature = STDS.fit_transform(x_train_selected)
            logging.info(f"Scaling x_train features")

            # Apply Unsupervised Learning (K-means Clustering) on the training
            dbscan = DBSCAN(eps=0.3, min_samples=2)
            # kmeans = KMeans(n_clusters=5, n_init='auto')
            logging.info(f"Scaling x_train features: done")
            cluster_assignments_train = dbscan.fit_predict(train_feature)
            
            # make directory
            os.makedirs(MODEL_DIR, exist_ok=True)
            # Save the kmeans model
            joblib.dump(dbscan, DBSCAN_MODEL_PATH)
            
            # Step 4: Combine Cluster Assignments with Original Features for both training and testing sets
            X_train_combined = np.column_stack((x_train_selected, cluster_assignments_train))
            logging.info(f"class assignment attached to the array  ")

            logging.info(f"model training initialized: model XGBOOST_REGRESSOR")
            xgb_regressor = XGBRegressor()
            XGB_model = xgb_regressor.fit(X_train_combined, y_train)

            logging.info(f"model XGBOOST called")

            # make directory
            os.makedirs(MODEL_DIR, exist_ok=True)
            # Save the model
            joblib.dump(XGB_model, FINAL_MODEL_PATH)
            logging.info(f"model XGBOOST saved")
            return XGB_model

        except Exception as e:
            raise Exception(f"Transformation Class Assignment", e)

