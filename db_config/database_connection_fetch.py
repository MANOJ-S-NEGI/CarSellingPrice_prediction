import pymongo
import pandas as pd
import numpy as np
from artifects_dir.path_artifect import *
import logging
from log_dir.log import *


# Connection to MongoDB and data fetching from DATABASE
class MongoDBClient:
    def __init__(self):
        try:
            Mongo_db_url = os.getenv('MONGO_URL')
            if Mongo_db_url is None:
                raise Exception(f"Environment key: is not set.")
            self.connection = pymongo.MongoClient(Mongo_db_url)
        except Exception as e:
            raise EnvironmentError(e)

    def fetching_collection_data(self):
        try:
            collection = self.connection[DATABASE_NAME][DATABASE_COLLECTION_NAME]

            records = []
            for i in collection.find():
                records.append(i)
            df = pd.DataFrame(records)
            if "_id" in df.columns:
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            logging.info(f"sample data from are {df.head(2)}")
            return df

        except Exception as e:
            raise Exception(f"Error in record Fetching: {e}")

#print(MongoDBClient().fetching_collection_data())
