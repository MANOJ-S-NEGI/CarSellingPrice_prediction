from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from db_config.database_connection_fetch import *
from log_dir.log import *
from artifects_dir.path_artifect import *
from components.Ingestion import *
logging.info(f"initiating Transformation module")


class Transformation:
    def __init__(self):
        self.frame = Ingestion().export_data_feature_store()

    def Read_Csv(self):
        try:
            numerical_col = []
            categorical_col = []

            dframe = self.frame
            logging.info(f"dataframe called have columns: \n {dframe.dtypes}")

            # Iterate through columns and check if they are numeric
            for i in dframe.columns:
                if pd.api.types.is_numeric_dtype(dframe[i]):
                    numerical_col.append(i)
                else:
                    categorical_col.append(i)

            logging.info(f"numerical and categorical column list created successfully")
            logging.info(f"categorical_col :{categorical_col}")
            logging.info(f"numerical_col :{numerical_col}")
            return dframe, categorical_col, numerical_col

        except Exception as e:
            raise Exception(f"Transformation Error_read_csv", e)

    def One_Hot_Encoder(self):
        try:
            dframe, categorical_col, numerical_col = self.Read_Csv()
            OHE = OneHotEncoder()
            encode = OHE.fit_transform(dframe[categorical_col])
            logging.info(f"categorical_col transformed")

            # fitting encode into frame with columns:
            encode_frame = pd.DataFrame(encode.toarray(), columns=OHE.get_feature_names_out(categorical_col))
            logging.info(f"fitting encode into frame with columns")

            # Reset the index of encode_categories and data_num_frame
            encode_frame = encode_frame.reset_index(drop=True)
            data_numerical_frame = dframe[numerical_col].reset_index(drop=True)
            logging.info(f" index of encode_categories and data_num_frame reset")

            # Concatenate the one-hot encoded categorical columns with the numerical columns
            x_encode = pd.concat([encode_frame, data_numerical_frame], axis=1)
            logging.info(f"Concatenate the one-hot encoded categorical columns with the numerical columns")
            return x_encode

        except Exception as e:
            raise Exception(f"Transformation Error_OneHot", e)

    def Feature_Target(self):
        try:
            x_encode = self.One_Hot_Encoder()

            # split data into features and target values:
            logging.info("splitting data into features and target frames")
            x = x_encode.drop(columns=["selling_price"], axis=1)
            y = x_encode["selling_price"]
            logging.info(f"shape of feature dataset:{x.shape}")
            logging.info(f"shape of feature dataset:{y.shape}")

            return x, y

        except Exception as e:
            raise Exception(f"Transformation Error_OneHot", e)

    def Train_Test_Split(self):
        try:
            x, y = self.Feature_Target()

            # train test split:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

            # checking shape and dimension:
            logging.info("shape of x_train{} and have dimension: {}".format(x_train.shape, x_train.ndim))
            logging.info("shape of y_train{} and have dimension: {}".format(y_train.shape, y_train.ndim))
            logging.info("shape of x_test{}  and have dimension: {}".format(x_test.shape, x_test.ndim))
            logging.info("shape of y_test{} and have dimension: {}".format(y_test.shape, x_test.ndim))
            return x_train, x_test, y_train, y_test
        except Exception as e:
            raise Exception(f"Transformation train_test_split_error ", e)

#Transformation().Train_Test_Split()