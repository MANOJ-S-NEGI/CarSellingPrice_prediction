import os
import logging
import pandas as pd
import pymongo
from constants.env_variable import *


class Into_Db:
    def __init__(self):
        try:
            self.connect = os.getenv('MONGO_URL')
            self.client = pymongo.MongoClient(self.connect)
            logging.info(f"Connection Established To Database: {DATABASE_NAME}")
        except Exception as e:
            raise Exception(f"connection error during insertion of record: {e}")

    def ImportData(self):
        try:
            database = self.client[DATABASE_NAME]

            # table name
            collection = database[DATABASE_COLLECTION_NAME]

            # Read CSV into a pandas DataFrame (replace 'csv_path' with actual path)
            df = pd.read_csv(csv_path)

            # Convert DataFrame to dictionary for insertion
            records = df.to_dict(orient='records')

            # Insert records into MongoDB
            collection.insert_many(records)
            logging.info(f"Record inserted into {DATABASE_NAME} collection: {DATABASE_COLLECTION_NAME}")

            # Close MongoDB connection
            self.client.close()

        except Exception as e:
            raise e


Into_Db().ImportData()
