import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')
#print(passengers)

# Update sex column to numerical
passengers['Sex'] = passengers.Sex.map({'male': 0, 'female' : 1})
#print(passengers)

# Fill the nan values in the age column
#print(passengers['Age'].values)
passengers['Age'].fillna(value = np.mean(passengers.Age), inplace = True)
#print(passengers.Age.values)
# Create a first class column
passengers['FirstClass'] = np.where(passengers.Pclass.values == 1, 1, 0)
#print(passengers)
# Create a second class column
passengers['SecondClass'] = np.where(passengers.Pclass.values == 2, 1, 0)
#print(passengers)
# Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survived = passengers['Survived']
# Perform train, test, split
x_train, x_test, y_train, y_test = train_test_split(features, survived, test_size = 0.8)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
train_features = scaler.fit_transform(x_train)
test_features = scaler.transform(x_test)

# Create and train the model
log_model = LogisticRegression()
log_model.fit(x_train, y_train)

# Score the model on the train data
print(log_model.score(x_train, y_train))

# Score the model on the test data
print(log_model.score(x_test, y_test))

# Analyze the coefficients
print(log_model.coef_)

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([0.0 ,19.0 ,1.0 , 0.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, You])

# Scale the sample passenger features
sample_passengres = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
swim_or_sink = log_model.predict(sample_passengers)
print(swim_or_sink)

swim_or_sink_prob = log_model.predict_proba(sample_passengers)
print(swim_or_sink_prob)
