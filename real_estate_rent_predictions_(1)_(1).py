# -*- coding: utf-8 -*-
"""Real_estate_rent_predictions (1) (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bPrdfs2v5geWza1aQsZWS1z6qmAk6m38

Problem Statement:

In the real estate industry, determining the appropriate rental price for a property is crucial for
property owners, tenants, and property management companies. Accurate rent predictions can
help landlords set competitive prices, tenants make informed rental decisions, and property
management companies optimize their portfolio management.
The goal of this project is to develop a data-driven model that predicts the rental price of
residential properties based on relevant features. By analyzing historical rental data and
property attributes, the model aims to provide accurate and reliable rent predictions.

```
# This is formatted as code
```
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pip install openpyxl

data = pd.read_excel('House_Rent_Train.xlsx')

"""# **Data Preprocessing**"""

pd.set_option('display.max_columns', 500)

data.columns

data.head()

data.tail()

print("total_columns ----->>>>>", data.shape[1])
print("total_rows----->>>>>", data.shape[0])

data.drop(columns = ['id'],inplace=True)

data.info()

#need to change activation data object to dateandtime
# bathroom float to int
#cup_board float to int
#floor float to int
#total_floor float to int
#amenities convert to right format
#balconies float to int

percent_missing = data.isnull().sum() * 100 / len(data)
missing_values = pd.DataFrame({'percent_missing': percent_missing})
missing_values.sort_values(by ='percent_missing' , ascending=False)

data.dropna(subset=['longitude'], inplace=True) # longitude latitude
data.dropna(subset=['latitude'], inplace=True)

print(data.isnull().sum().sort_values(ascending=False))

"""*IMPUTATION*"""

#data.dropna(subset=['locality'], inplace=True)

from geopy.geocoders import Nominatim
import pandas as pd


missing_localities = data[data['locality'].isnull()]

# Initialize geocoder
geolocator = Nominatim(user_agent="reverse_geocoding")

# Function to get locality from latitude and longitude
def get_locality(latitude, longitude):
    location = geolocator.reverse((latitude, longitude), language='en')
    return location.address

# Iterate over rows with missing localities and fill them
for index, row in missing_localities.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    locality = get_locality(latitude, longitude)
    # Update the 'locality' column with the obtained value
    data.at[index, 'locality'] = locality

pip install geopy

data.locality.nunique()

data['locality'].value_counts().head(60)

data['locality'].value_counts().tail(60)

import pandas as pd

# Sample data
data = pd.DataFrame({'locality': [
    'Lore Pride, Ferns City, Bengaluru, Karnataka, India',
    'Koralur, Karnataka,Koralur',
    'Amblipura, 1st Sector',
    'Bannerghatta Road',
    'Krishnappa Layout, Durga Parameshwari Nagar, Bangarappanagar, RR Nagar, Bengaluru, Karnataka 560085, India,Bengaluru',
    'HVR Layout',
    'Someshwara Nagar, Bengaluru, Karnataka, India',
    'West Avenue Road, Doddanekundi, Bengaluru, Karnataka, India',
    'Maruthi Nagar, Madivala',
    'Kaikondrahalli,',
    '29, 21st A Cross Rd, Pragathi Layout, Doddanekundi, Doddanekkundi, Bengaluru, Karnataka 560037, India,Bengaluru',
    'Anjaneya Nagar, Ittamadu, Banashankari 3rd Stage, Banashankari, Bengaluru, Karnataka, India',
    'Nagarbhavi Circle, Outer Ring Road, Jyothi Nagar, Banashankari Stage I, Attiguppe, Bengaluru, Karnataka, India',
    'J P Nagar 5th Phase',
    'Billekahalli',
    '2nd Phase, JP Nagar, Bengaluru, Karnataka, India',
    'Jayanagar, 4th T Block',
    'C.V. Raman Nagar',
    'J P Nagar 2nd Phase',
    'Raja Rajeshwarinagar',
    'Gavipuram',
    'Koramangala 4th Block,HSR Layout 5th Sector',
    'Simhadri layout',
    'Skylark Esta, Seetharampalya, Bengaluru, Karnataka, India',
    '23d, 2nd A Cross Rd, Srinivasnagar, Banashankari, Bengaluru, Karnataka 560050, India,Bengaluru',
    'Wilson Garden,',
    'Jogupalaya',
    'Kottivakkam',
    '33, Hosur Road, Nanjappa Layout, Adugodi, Bengaluru, Karnataka, India',
    'Pattabhirama Nagar,Jayanagar',
    '7th Block Jayanagar',
    'Suddaguntepalya',
    'J. P. Nagar, Bengaluru, Karnataka, India',
    'Marthi Nagar',
    'BTM 2nd Stage, Stage 2, Bengaluru, Karnataka, India',
    'Sarjapur Road, Chikkakannalli, Bengaluru, Karnataka, India',
    'SR Krishnappa Garden, Jayanagar, Bengaluru, Karnataka, India',
    'Yemalur, Bengaluru, Karnataka, India',
    'ITPL Gate 3, Whitefield, Bengaluru, Karnataka, India',
    'HSR layout sector 6',
    'Canara Bank Colony',
    'GNS Residency, Bhagat Singh Main Road, Bommanahalli, Bengaluru, Karnataka, India',
    'Bommenahalli',
    'Chikkalasandra, Bengaluru, Karnataka, India',
    'Koramangala 3 Block, Bengaluru, Karnataka, India',
    'Shastri Nagar',
    'btm layout',
    'Gandhipuram, Whitefield',
    'Haralur Road, PWD Quarters, 1st Sector, Harlur, Bengaluru, Karnataka, India',
    'chennasandra',
    'Hoodi Main Road, Hoodi, Bengaluru, Karnataka, India',
    'Hampi Bus Stand, Hampi Nagar, RPC Layout, Vijaya Nagar, Bengaluru, Karnataka, India',
    'BTM Layout,BTM 2nd Stage',
    'Srinivasnagar, Banashankari',
    '3rdmain 5th cross link road kempegowdalayoutBanashankari, Bengaluru, Karnataka, India',
    'Basaweshwar nagar',
    'Agrahara Dasarahalli',
    '59/3, 1st Cross Rd, Shamanna Reddy Layout, Virat Nagar, Bommanahalli, Bengaluru, Karnataka 560068, India,Bengaluru',
    'KHB Colony',
    'Mahadevapura bus stop, Mahadevapura, Bengaluru, Karnataka, India'
]})

# Extract only the area name
data['locality'] = data['locality'].str.extract(r'([A-Z][a-z]+(?: [A-Z][a-z]+)*)', expand=False)

# Display the result
print(data['locality'])

data

import pandas as pd

# Assuming data is your DataFrame containing the 'locality' column
# Let's create a copy of the 'locality' column to work with
data['locality'] = data['locality'].copy()

# Splitting the 'locality' column based on commas and spaces and taking the first part
data['locality'] = data['locality'].str.split(',').str[0]
data['locality'] = data['locality'].str.split().str[0]

# Displaying the first few rows to verify the changes
print(data['locality'].tail(60))

data['locality'].value_counts()



data['type'].value_counts()

data['type'].fillna(data['type'].mode()[0], inplace = True)

# Assuming 'data' is the name of your DataFrame

# Mapping to consolidate similar categories
type_mapping = {
    'BHK2': 'BHK2',
    'bhk2': 'BHK2',
    'BHK3': 'BHK3',
    'bhk3': 'BHK3',
    'BHK1': 'BHK1',
    'RK1': 'RK1',
    'BHK4': 'BHK4',
    'BHK4PLUS': 'BHK4PLUS',
    '1BHK1': 'BHK1'
}

# Apply the mapping to the 'type' column
data['type'] = data['type'].map(type_mapping)

# Verify the changes
print(data['type'].value_counts())

print(data.isnull().sum().sort_values(ascending=False))

data.locality[0]



"""*CONVERT INTO RIGHT FORMAT*"""

## Convert 'activation' column to datetime
data['activation_date'] = pd.to_datetime(data['activation_date'])

data['activation_date'].dtype

# Replace 'bathroom', 'cup_board', 'floor', 'total_floor', 'balconies' with the actual column names

data['bathroom'] = data['bathroom'].astype(int)
data['cup_board'] = data['cup_board'].astype(int)
data['floor'] = data['floor'].astype(int)
data['total_floor'] = data['total_floor'].astype(int)
data['balconies'] = data['balconies'].astype(int)
data['property_age'] = data['property_age'].astype(int)
data['rent'] = data['rent'].astype(int)

#data['amenities'][0]
data['amenities'][3]

import json

# Assuming 'data' is the name of your DataFrame
data['amenities'] = data['amenities'].apply(json.loads)
data['true_amenities_count'] = data['amenities'].apply(lambda x: list(x.values()).count(True))

data.drop(columns = 'amenities', inplace = True)

data['balconies'].value_counts()

data['building_type'].value_counts()

data['water_supply'].value_counts()

data['total_floor'].value_counts()

data.activation_date.value_counts()

data.latitude.value_counts()

data.longitude.value_counts()

data.lease_type.value_counts()

data.lease_type.value_counts()

data.gym.value_counts()

data.lift.value_counts()

data.swimming_pool.value_counts()

data.negotiable.value_counts()

data.furnishing.value_counts()

data.parking.value_counts()

"""NONE means there is not available parking facility"""

data.property_size.value_counts()

data.property_age.value_counts()

data.bathroom.value_counts()

data.facing.value_counts()

data.cup_board.value_counts()

data.floor.value_counts()

data.total_floor.value_counts()

data.water_supply.value_counts()

data.building_type.value_counts()

data.balconies.value_counts()

data.rent.value_counts()

data.true_amenities_count.value_counts()

data.columns

"""**OUTLIERS**"""

data.describe()

"""**#I think there is no outliers beacause here all columns going to categorical except rent column**

Feature Engineering
"""

# Define the age categories
bins = [-1, 0, 5, 10, 15, 20, 25, 30, 40, 50, 100, float('inf')]
labels = ['Unknown', 'New', '5-10 years', '10-15 years', '15-20 years', '20-25 years',
          '25-30 years', '30-40 years', '40-50 years', '50-100 years', 'Very Old']

# Create a new column 'age_category'
data['prop_age_category'] = pd.cut(data['property_age'], bins=bins, labels=labels, right=False)

# Display the counts in each age category
print(data['prop_age_category'].value_counts())

import pandas as pd

# Assuming 'activation_date' is the name of your column with activation dates
data['activation_date'] = pd.to_datetime(data['activation_date'])

# Extracting month and day
data['activation_month'] = data['activation_date'].dt.month
data['activation_day'] = data['activation_date'].dt.day

# Display the updated DataFrame
print(data[['activation_date', 'activation_month', 'activation_day']])

data.drop(columns=['activation_date', 'activation_day'], inplace=True)

data.drop(columns=['latitude', 'longitude','prop_age_category'], inplace=True)

data

pd.DataFrame(data.dtypes.value_counts()).T

data.shape

integer_data_cols = [var for var in data.columns if data[var].dtype == 'int64']
integer_data_cols

for i in integer_data_cols:
  print(f'Column "{i}" is divided into "{len(data[i].value_counts())}" categories.')

object_data_cols = [var for var in data.columns if data[var].dtype == 'object']
object_data_cols

for i in object_data_cols:
  print(f'Column "{i}" is divided into "{len(data[i].value_counts())}" categories.')

"""## **EDA(data visualization)**"""

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the name of your DataFrame

# List of columns to plot
columns_to_plot = ['gym', 'lift', 'swimming_pool', 'negotiable', 'property_age', 'bathroom', 'cup_board',
                   'floor', 'total_floor', 'balconies', 'true_amenities_count', 'activation_month']

# Set up subplots
fig, axes = plt.subplots(nrows=len(columns_to_plot), ncols=1, figsize=(10, 5 * len(columns_to_plot)))

# Loop through columns and create count plots
for i, column in enumerate(columns_to_plot):
    sns.countplot(x=column, data=data, ax=axes[i], palette='viridis')
    axes[i].set_title(f'Distribution of {column}')
    axes[i].set_xlabel('Count')
    axes[i].set_ylabel('')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the name of your DataFrame

# List of columns to plot
columns_to_plot = ['type', 'lease_type', 'furnishing', 'parking', 'facing', 'water_supply', 'building_type']

# Set up subplots
fig, axes = plt.subplots(nrows=len(columns_to_plot), ncols=1, figsize=(10, 5 * len(columns_to_plot)))

# Loop through columns and create count plots
for i, column in enumerate(columns_to_plot):
    sns.countplot(x=column, data=data, ax=axes[i])
    axes[i].set_title(f'Distribution of {column}')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the name of your DataFrame

# Set up the figure and axis
plt.figure(figsize=(10, 6))

# Scatter plot
sns.scatterplot(x='property_age', y='rent', data=data, alpha=0.6, color='blue')

# Set plot labels
plt.title('Scatter Plot of Rent vs. Property Age')
plt.xlabel('Property Age')
plt.ylabel('Rent')

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the name of your DataFrame

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the histogram for 'rent'
sns.histplot(data['rent'], bins=30, kde=True, color='skyblue', ax=ax)

# Adding labels and title
ax.set_xlabel('Rent')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Rent')

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the name of your DataFrame

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the histogram for 'rent'
sns.histplot(data['property_size'], bins=20, kde=True, color='skyblue', ax=ax)

# Adding labels and title
ax.set_xlabel('property_size')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of property_size')

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the name of your DataFrame

# List of categorical columns
categorical_columns = ['type', 'lease_type', 'furnishing', 'parking', 'facing', 'water_supply', 'building_type']

# Set up subplots
fig, axes = plt.subplots(nrows=len(categorical_columns), ncols=1, figsize=(10, 5 * len(categorical_columns)))

# Loop through categorical columns and create bar plots
for i, column in enumerate(categorical_columns):
    # Calculate average rent for each category and sort by rent
    average_rent_by_category = data.groupby(column)['rent'].mean().sort_values()

    sns.barplot(x=column, y='rent', data=data, ax=axes[i], order=average_rent_by_category.index, palette='viridis')
    axes[i].set_title(f'Rent vs {column}')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Average Rent')

plt.tight_layout()
plt.show()

# List of columns to plot
columns_to_plot = ['gym', 'lift', 'swimming_pool', 'negotiable', 'property_age',
                   'bathroom', 'cup_board', 'floor', 'total_floor', 'balconies', 'true_amenities_count', 'activation_month']

# Set up subplots
fig, axes = plt.subplots(nrows=len(columns_to_plot), ncols=1, figsize=(10, 5 * len(columns_to_plot)))

# Loop through columns and create bar plots
for i, column in enumerate(columns_to_plot):
    sns.barplot(x=column, y='rent', data=data, ax=axes[i], ci=None, palette='viridis')
    axes[i].set_title(f'Rent vs {column}')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Average Rent')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the name of your DataFrame

# Set up the figure
plt.figure(figsize=(10, 6))

# Scatter plot for 'property_size' vs 'rent'
sns.scatterplot(x='property_size', y='rent', data=data, alpha=0.5, color='skyblue')

# Adding labels and title
plt.xlabel('Property Size')
plt.ylabel('Rent')
plt.title('Scatter Plot: Property Size vs Rent')

plt.show()

# Calculate the average rent for each locality and sort by rent
average_rent_by_locality = data.groupby('locality')['rent'].mean().sort_values(ascending=False)

# Select the top 10 localities
top_localities = average_rent_by_locality.head(15).index

# Filter the data for the top localities
data_top_localities = data[data['locality'].isin(top_localities)]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(15, 6))

# Create the bar plot for 'locality' vs 'rent'
sns.barplot(x='locality', y='rent', data=data_top_localities, ci=None, order=top_localities, palette='viridis')

# Adding labels and title
ax.set_xlabel('Locality')
ax.set_ylabel('Average Rent')
ax.set_title('Top 10 Localities vs Average Rent')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# Create a correlation matrix (replace 'data' with your DataFrame)
correlation_matrix = data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(14, 12))

# Create a heatmap with the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)

# Show the plot
plt.show()

data.drop(columns = 'activation_month', inplace = True)

"""# **Encoding Categorical Variables**"""

data

data['building_type'].value_counts() # two, none, 4 , both

#LEBEL ENCODING (ORDER IS THERE SO I AM GOING FOR THIS , HOW I FIND HERE ORDER IS THERE I REFER THE VS PLOT THERE SHOWING A ORDER BAR PLOT)
data['type'] = data['type'].map({'RK1':0,'BHK1':1,'BHK2':2,'BHK3':3,'BHK4':4,'BHK4PLUS':5})
data['lease_type'] = data['lease_type'].map({'BACHELOR':0,'ANYONE':1,'FAMILY':2,'COMPANY':3})
data['furnishing'] = data['furnishing'].map({'NOT_FURNISHED':0,'SEMI_FURNISHED':1,'FULLY_FURNISHED':2})
data['parking'] = data['parking'].map({'TWO_WHEELER':0,'NONE':1,'FOUR_WHEELER':2,'BOTH':3})
data['facing'] = data['facing'].map({'N':0,'S':1,'E':2,'W':3, 'NE':4, 'NW':5, 'SE':6, 'SW':7})
data['water_supply'] = data['water_supply'].map({'CORPORATION':0,'CORP_BORE':1,'BOREWELL':2})
data['building_type'] = data['building_type'].map({'IF':0,'IH':1,'AP':2,'GC':3})

pip install category_encoders

# Perform leave-one-out encoding for card_type, card_number, and tid
from category_encoders import LeaveOneOutEncoder

looe_encoder = LeaveOneOutEncoder(cols=['locality'])
data = looe_encoder.fit_transform(data, data['rent'])

data

"""# **SPLIT THE DATA**"""

X = data.drop('rent',axis=1)
y = data['rent']
#splitting the data into training and testing sets with the ratio of 8:2
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=70)

print(X_train)
print(X_test)

print(len(y_train))
print(len(y_test))

"""# **SCALE THE DATA**"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_scaled ,X_test_scaled

"""# **MODEL FITING**"""

# there are 4 steps in fitting a model 1.import, 2.initial, 3.Fit, 4. Prediction

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb

"""##**Linear regression**"""

from sklearn.linear_model import LinearRegression #import
linear_model = LinearRegression(fit_intercept=True) #initialise
linear_model.fit(X_train,y_train) #fit - all magic
print(linear_model.predict(X_test))     #predict
print(y_test)

linear_model.score(X_test, y_test)

from sklearn.model_selection import cross_val_score
# synatx : cross_val_score(model, fts_train, target_train, bins).mean()
cross_val_linear_model=cross_val_score(linear_model,X_train,y_train,cv=10).mean()
cross_val_linear_model

"""# **K Nearest Neighbor Regression**"""

knn_values=np.arange(1,50)
cross_val_knn=[]
for k in knn_values:
    knn_regressor=KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train_scaled,y_train)
    print("K value : ", k, " train score : ", knn_regressor.score(X_train_scaled,y_train)  ,"cross_val_score : ", cross_val_score(knn_regressor,X_train_scaled,y_train,cv = 10).mean())
    cross_val_knn.append(cross_val_score(knn_regressor,X_train_scaled,y_train,cv = 10).mean())

# for model creation and model evaluation
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

cross_val_knn_regressor=max(cross_val_knn)

print("The best K-Value is 16 and Cross_val_score is",cross_val_knn_regressor )

#Implementing K Nearest Neighbor Regression
knn_regressor=KNeighborsRegressor(n_neighbors=19)
knn_regressor.fit(X_train_scaled,y_train)

cross_val_knn_regressor=cross_val_score(knn_regressor,X_train_scaled,y_train,cv=15).mean()
cross_val_knn_regressor

"""# **Decision Tree Regression**"""

#Choosing the best of depth Value
from sklearn.tree import DecisionTreeRegressor

max_depth=np.arange(1,20)
cross_val_dt=[]
for d in max_depth:
    dt_regressor= DecisionTreeRegressor(max_depth=d, random_state=0)
    dt_regressor.fit(X_train,y_train)
    print("Depth : ", d, " train Score  : ", dt_regressor.score(X_train,y_train), "cross_val_score : ", cross_val_score(dt_regressor,X_train,y_train,cv = 10).mean())
    cross_val_dt.append(cross_val_score(dt_regressor,X_train,y_train,cv = 10).mean())

cross_val_dt_regressor=max(cross_val_dt)

print("The best depth is 8 and Cross_val_score is:",cross_val_dt_regressor)

# Implementing Decision Tree Regression
dt_regressor=DecisionTreeRegressor(max_depth=6, random_state=0)
dt_regressor.fit(X_train,y_train)

cross_val_dt_regressor=cross_val_score(dt_regressor,X_train,y_train,cv=10).mean()
cross_val_dt_regressor

ftImp = list(zip(dt_regressor.feature_importances_, data.columns[:-1]))
imp = pd.DataFrame(ftImp, columns = ["Importance","Feature"])
imp.sort_values("Importance",ascending = False,inplace=True)
imp

"""# **Random Forest Regression**"""

#Choosing the best depth value
from sklearn.ensemble import RandomForestRegressor

max_depth=np.array([2,4,8,10,11,12,13,15,18,20])
cross_val_rf=[]
for d in max_depth:
    rf_regressor=RandomForestRegressor(max_depth=d, random_state=0)
    rf_regressor.fit(X_train,y_train)
    print("Depth : ", d, "cross_val_score : ", cross_val_score(rf_regressor,X_train,y_train,cv = 15).mean())
    cross_val_rf.append(cross_val_score(rf_regressor,X_train,y_train,cv = 15).mean())

cross_val_rf_regressor=max(cross_val_rf)

print("The best depth is 20 and Cross_val_score is:",cross_val_rf_regressor)

#Implementing Random Forest Regression

rf_regressor=RandomForestRegressor(max_depth=20, random_state=0)
rf_regressor.fit(X_train,y_train)

cross_val_rf_regressor=cross_val_score(rf_regressor,X_train,y_train,cv=15).mean()
cross_val_rf_regressor

"""# **Extreme Gradient Boosting Regression**"""

#Choosing the best Learning Rate
import xgboost as xgb

cross_val_xgb=[]
for lr in [0.01,0.05,0.08,0.1,0.2,0.25,0.3]:
    xgb_regressor= xgb.XGBRegressor(learning_rate = lr,n_estimators=100)
    xgb_regressor.fit(X_train,y_train)
    print("Learning rate : ", lr,"cross_val_score:", cross_val_score(xgb_regressor,X_train,y_train,cv = 15).mean())
    cross_val_xgb.append(cross_val_score(xgb_regressor,X_train,y_train,cv = 15).mean())

cross_val_xgb_regressor=max(cross_val_xgb)

print("The best Learning rate is 0.2 and Cross_val_score is:",cross_val_xgb_regressor)

#Implementing Extreme Gradient Boosting Regression

xgb_regressor= xgb.XGBRegressor(learning_rate =0.2,n_estimators=100) # initialise the model
xgb_regressor.fit(X_train,y_train) #train the model

cross_val_xgb_regressor=cross_val_score(xgb_regressor,X_train,y_train,cv=15).mean()
cross_val_xgb_regressor

print("Cross Validation Score for Linear Regression Model:",cross_val_linear_model)
print("Cross Validation Score for K-Nearest Neighbors Regression Model:",cross_val_knn_regressor)
print("Cross Validation Score for Decision Tree Regression Model: ",cross_val_dt_regressor)
print("Cross Validation Score for Random Forest Regression Model: ",cross_val_rf_regressor)
print("Cross Validation Score for Extreme-Gradient Boosting Regression Model: ",cross_val_xgb_regressor)

"""# **R2 Score for Machine-Learning Models**"""

from sklearn.metrics import r2_score

y_pred_lr=linear_model.predict(X_test)
y_pred_knn=knn_regressor.predict(X_test)
y_pred_dt= dt_regressor.predict(X_test)
y_pred_rf=rf_regressor.predict(X_test)
y_pred_xgb=xgb_regressor.predict(X_test)

R2_score_lr=r2_score(y_test,y_pred_lr)
R2_score_knn=r2_score(y_test,y_pred_knn)
R2_score_dt=r2_score(y_test,y_pred_dt)
R2_score_rf=r2_score(y_test,y_pred_rf)
R2_score_xgb=r2_score(y_test,y_pred_xgb)

print("R2 Score for Linear Regression Model:",R2_score_lr)
print("R2 Score for K-Nearest Neighbors Regression Model:",R2_score_knn)
print("R2 Score for Decision Tree Regression Model: ",R2_score_dt)
print("R2 Score for Random Forest Regression Model: ",R2_score_rf)
print("R2 Score for Extreme-Gradient Boosting Regression Model: ",R2_score_xgb)

"""# **Suggestion to Sellers and buyers-Solving problem statements based on Feature Importance**"""

xgb_regressor.feature_importances_

data.columns

sorted_idx = dt_regressor.feature_importances_.argsort()
plt.figure(figsize=(10,5))
plt.barh(data.columns[sorted_idx], xgb_regressor.feature_importances_[sorted_idx])
plt.xlabel("Random Forest Feature Importance")
plt.title("Feature Importance")
plt.show()

xgb_regressor.feature_importances_

sorted_idx = xgb_regressor.feature_importances_.argsort()
plt.figure(figsize=(10,5))
plt.barh(data.columns[sorted_idx], xgb_regressor.feature_importances_[sorted_idx])
plt.xlabel("Extreme Gradient Boosting Feature Importance")
plt.title("Feature Importance")
plt.show()

"""# **Evaluate Your System on the Test Set**"""

test = pd.read_excel('House_Rent_Test.xlsx')

test.head()

test.tail()

test.shape

test.columns

test.isnull().sum()

test.info()

test.drop(columns = ['id'],inplace=True)

test['type'].value_counts()

test['activation_date'] = pd.to_datetime(test['activation_date'])

test['bathroom'] = test['bathroom'].astype(int)
test['cup_board'] = test['cup_board'].astype(int)
test['floor'] = test['floor'].astype(int)
test['total_floor'] = test['total_floor'].astype(int)
test['balconies'] = test['balconies'].astype(int)
test['property_age'] = test['property_age'].astype(int)
#test['rent'] = test['rent'].astype(int)

import json

# Assuming 'data' is the name of your DataFrame
test['amenities'] = test['amenities'].apply(json.loads)
test['true_amenities_count'] = test['amenities'].apply(lambda x: list(x.values()).count(True))

test.drop(columns = 'amenities', inplace = True)

test.drop(columns=['activation_date', 'latitude', 'longitude'], inplace=True)
#test.drop(columns=['latitude', 'longitude','prop_age_category'], inplace=True)

#LEBEL ENCODING (ORDER IS THERE SO I AM GOING FOR THIS , HOW I FIND HERE ORDER IS THERE I REFER THE VS PLOT THERE SHOWING A ORDER BAR PLOT)
test['type'] = test['type'].map({'RK1':0,'BHK1':1,'BHK2':2,'BHK3':3,'BHK4':4,'BHK4PLUS':5})
test['lease_type'] = test['lease_type'].map({'BACHELOR':0,'ANYONE':1,'FAMILY':2,'COMPANY':3})
test['furnishing'] = test['furnishing'].map({'NOT_FURNISHED':0,'SEMI_FURNISHED':1,'FULLY_FURNISHED':2})
test['parking'] = test['parking'].map({'TWO_WHEELER':0,'NONE':1,'FOUR_WHEELER':2,'BOTH':3})
test['facing'] = test['facing'].map({'N':0,'S':1,'E':2,'W':3, 'NE':4, 'NW':5, 'SE':6, 'SW':7})
test['water_supply'] = test['water_supply'].map({'CORPORATION':0,'CORP_BORE':1,'BOREWELL':2})
test['building_type'] = test['building_type'].map({'IF':0,'IH':1,'AP':2,'GC':3})

# Perform leave-one-out encoding for card_type, card_number, and tid
from category_encoders import LeaveOneOutEncoder

looe_encoder = LeaveOneOutEncoder(cols=['locality'])
test = looe_encoder.fit_transform(test, test['property_size'])

test

import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Create DMatrix objects for XGBoost

dtrain = xgb.DMatrix(data=X_train, label=y_train, enable_categorical=True)
test = xgb.DMatrix(data=test, enable_categorical=True)

import xgboost as xgb

# Assuming you already have dtrain and dtest defined from previous steps

# Specify the XGBoost parameters such as 'max_depth', 'eta', etc.
params = {
    'max_depth': 5,
    'eta': 0.2,
    'objective': 'reg:squarederror',  # Specify the appropriate objective for your problem
}

# Perform cross-validation with 10 folds
cv_results = xgb.cv(
    params=params,
    dtrain=dtrain,
    num_boost_round=100,  # You can adjust the number of boosting rounds
    nfold=10,  # Number of cross-validation folds
    metrics={'rmse'},  # Evaluation metric (Root Mean Squared Error)
    early_stopping_rounds=10,  # Optional: Early stopping rounds
    seed=42  # Optional: Seed for reproducibility
)

# Get the best number of boosting rounds
best_num_boost_rounds = cv_results['test-rmse-mean'].idxmin()

# Re-train the model with the best number of boosting rounds
xgb_reg = xgb.train(params, dtrain, num_boost_round=best_num_boost_rounds)

# Make predictions on the test set
y_pred = xgb_reg.predict(test)

def custom_round(x):
    round_value=round(x*100)
    return round_value/100

y_pred1=np.vectorize(custom_round)(y_pred)

y_pred1

submission =  pd.read_excel('House_Rent_Test.xlsx')

Predicted_rent=pd.DataFrame({'id':submission['id'],'rent':y_pred1})

Predicted_rent.to_csv('Submission.csv', index = False)

Submission = pd.read_csv('Submission.csv')
Submission


