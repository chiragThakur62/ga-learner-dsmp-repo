# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here

df=pd.read_csv(path)

df.head(5)

X=pd.DataFrame(df.iloc[:,df.columns != 'list_price'])
y=df['list_price']
# code ends here

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=6)


# --------------
import matplotlib.pyplot as plt

# code starts here        

cols=X_train.columns




# code ends here



# --------------
# Code starts here



corr=X_train.corr().abs()


upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))

# Find index of feature columns with correlation greater than 0.95
to_drop = [column for column in upper.columns if any(upper[column] > 0.75)]

X_train.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)

X_test.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor=LinearRegression()

# fit model on training data

regressor.fit(X_train, y_train)

# predict on test features

y_pred = regressor.predict(X_test)


mse=mean_squared_error(y_test, y_pred)

r2=r2_score(y_test, y_pred)



# --------------
# Code starts here



residual = y_test - y_pred
# Code ends here


