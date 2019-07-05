# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here

df=pd.read_csv(path)
df.iloc[:,0:5]

X=df.iloc[:, df.columns != 'insuranceclaim']
y=df['insuranceclaim']
# Code ends here

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size = 0.2 , random_state = 6)






# --------------
import matplotlib.pyplot as plt


# Code starts here

q_value = X_train['bmi'].quantile(0.95)
plt.boxplot(X_train['bmi'], q_value)
# Code ends here




# --------------
# Code starts here



# Code ends here

relation=X_train.corr()

print(relation)


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here

cols=['children','sex','region','smoker']
print(cols)
fig,axes=plt.subplots(2,2)



# Code ends here


# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here

lr=LogisticRegression()

grid=GridSearchCV(estimator=lr,param_grid=parameters)

grid.fit(X_train , y_train)

y_pred=grid.predict(X_test)

accuracy=accuracy_score(y_test, y_pred)
# Code ends here


# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics

# Code starts here


score=roc_auc_score(y_test, y_pred)
# Code ends here

y_pred_proba=grid.predict_proba(X_test)[:,1]




roc_auc=roc_auc_score(y_test, y_pred_proba)


