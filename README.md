# DISCRIPTION: END-TO-END CAR PRICE PREDICTION
CLICK HERE: [CAR PRICE PREDICTION](https://huggingface.co/spaces/msn-enginenova21/car-price-prediction)

---
---
### Objective : 
Predict the selling price of the car based on the performance and description.

### Dataset_Description: 
- Number of Data columns (total 13 columns):
```
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   year           6717 non-null   int64  
 1   selling_price  6717 non-null   int64  
 2   km_driven      6717 non-null   int64  
 3   fuel           6717 non-null   object 
 4   seller_type    6717 non-null   object 
 5   transmission   6717 non-null   object 
 6   owner          6717 non-null   object 
 7   seats          6717 non-null   float64
 8   mileage_kmpl   6717 non-null   float64
 9   engine_cc      6717 non-null   float64
 10  max_power_bhp  6717 non-null   float64
 11  torque_kgm     6717 non-null   float64
 12  rpm            6717 non-null   float64
types: float64(6), int64(3), object(4)
memory usage: 682.3+ KB

```
Note: csv_dir contains the clean data csv file without any null, duplicate, or missing values.

### Dataset Description:
![Screenshot 2023-10-15 205850](https://github.com/MANOJ-S-NEGI/CarSellingPrice_prediction/assets/99602627/f17a924e-bb46-4c20-944e-945d8274f57d)


### Dataset Plots:
![Screenshot 2023-10-15 205738](https://github.com/MANOJ-S-NEGI/CarSellingPrice_prediction/assets/99602627/54b0cacb-1081-4d47-b5cb-a1d596d55e38)


### Dataset Outlier:
![Screenshot 2023-10-15 205817](https://github.com/MANOJ-S-NEGI/CarSellingPrice_prediction/assets/99602627/91160b7e-c0bb-4c39-a282-d7d6ebe96690)

### Model Building Approach:
##### Step to be performed : 
- We will be going to perform the GridCVSearch to find the best parameter for the RandomForestRegressor
- Using the parameters we will find the best features (this model is trained at threshold= 0.05)
- After finding the best features DBScan algorithm was performed to find the groups of data points that are close to each other based on a density criterion.
- finally, we going to use the Xgboost technique.

  ## DATA ACCURACY ACHIEVED:
  - mean_square_error : 9434757249.8
  - Root_mean_squared_error:97132.7
  - mean_absolute_error : 64489.1
  - R-squared: 0.90
  - Adjusted R-squared: 0.90

#### PREDICTION RESULTS:
![Screenshot 2023-10-15 210004](https://github.com/MANOJ-S-NEGI/CarSellingPrice_prediction/assets/99602627/8f405b66-9b33-4bb7-a18e-b44a4f6b9340)








