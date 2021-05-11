
import pandas as pd

#loding the data frame
con=pd.read_csv("C:/Users/hp/Desktop/DataSets/calories_consumed.csv")

con.info()   #For data types and non or null values
# data has no na or nall values 

con.describe() # for mean ,min, max, IQR 

con.shape

con.dtypes

EDA=pd.DataFrame({"columns_name ":con.columns,
                  "mean":con.mean(),
                  "median":con.median(),
                  "mode":con.mode(),
                  "standard_deviation":con.std(),
                  "variance":con.var(),
                  "skewness":con.skew(),
                  "kurtosis":con.kurt()})
EDA

#transforming the columns

# pass a list of functions 
result = con.transform(func = ['sqrt', 'exp','log']) 
  
# Print the result 
print(result) 