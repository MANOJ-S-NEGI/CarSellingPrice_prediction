from db_config.database_connection_fetch import *
from log_dir.log import *
from artifects_dir.path_artifect import *


class Ingestion:
    def __init__(self):
        try:
            self.data_call_from_database = MongoDBClient().fetching_collection_data()
            self.csv = CSV_PATH
        except Exception as e:
            raise Exception(f"Claas Ingestion Init error", e)

    def export_data_feature_store(self):
        try:
            # calling dataframe form db module
            dataframe = self.data_call_from_database
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            # make directory
            os.makedirs(CSV_DIR, exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {self.csv}")
            dataframe.to_csv(self.csv, index=False, header=True)
            return dataframe

        except Exception as e:
            raise Exception(f"Error in Ingestion Dataframe export Failed", e)

#Ingestion().export_data_feature_store()
