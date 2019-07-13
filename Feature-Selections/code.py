# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path
dataset=pd.read_csv(path)

# look at the first five columns
dataset.iloc[:,0:5]

# Check if there's any column which is not useful and remove it like the column id
dataset.drop(columns='Id',inplace=True)

# check the statistical description



# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols=dataset.columns
size=len(cols)
print(cols)
#number of attributes (exclude target)
x=dataset['Cover_Type']
y=dataset.iloc[:, dataset.columns != 'Cover_Type']


#x-axis has target attribute to distinguish between classes


#y-axis shows values of an attribute


#Plot violin for all attributes



# --------------
import numpy
upper_threshold = 0.5
lower_threshold = -0.5

# Code Starts Here
subset_train=dataset.iloc[:,0:10]

data_corr=subset_train.corr()

#sns.heatmap(data_corr)

correlation=data_corr.unstack().sort_values(kind='quicksort')
# Code ends here

corr_var_list = correlation[((correlation >upper_threshold) | (correlation <lower_threshold)) & (correlation!=1) ]

#corr_var_list=correlation[(correlation>lower_threshold) and (correlation<upper_threshold)]
print(corr_var_list)


# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)
X=dataset.iloc[:, dataset.columns != 'Cover_Type']
Y=dataset['Cover_Type']

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,Y, test_size = 0.2 , random_state = 0)
scaler = StandardScaler()
X_train_temp= scaler.fit_transform(X_train.iloc[:,0:size],y_train) 
X_test_temp=scaler.fit_transform(X_test.iloc[:,0:size])

#X_train_temp=pd.DataFrame(X_train_temp)
#X_train1=pd.concat([X_train_temp,X_train])
X_train1=np.concatenate((X_train_temp,X_train.iloc[:,size:]),axis=1)
#X_test_temp=pd.DataFrame(X_test_temp)
#X_test1=pd.concat([X_test_temp,X_test])
X_test1=np.concatenate((X_test_temp,X_test.iloc[:,size:]),axis=1)
scaled_features_train_df=pd.DataFrame(data=X_train1,columns=X_train.columns,index=X_train.index)
scaled_features_test_df= pd.DataFrame(data=X_test1,columns=X_test.columns,index=X_test.index)






# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif

# Write your solution here:
skb=SelectPercentile(score_func=f_classif , percentile=20)
predictors=skb.fit_transform(X_train1, y_train)
scores=skb.scores_.tolist()
Features=X.columns
#cpn=pd.concat([Features,scores],axis=1)

dataframe=pd.DataFrame({'Features': Features,'scores': scores})
dataframe=dataframe.sort_values(by=['scores'],ascending=False)
 
top_k_predictors=dataframe[dataframe.scores >= dataframe.scores.quantile(0.80)].Features.tolist()
print(dataframe.scores.quantile(0.80))
print(np.percentile(dataframe.scores,80))
print(top_k_predictors)


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score

clf=LogisticRegression()
clf1=OneVsRestClassifier(clf)

model_fit_all_features=clf1.fit(X_train,y_train)
predictions_all_features=clf1.predict(X_test)
score_all_features=accuracy_score(y_test,predictions_all_features)
print(score_all_features)

model_fit_top_features=clf.fit(scaled_features_train_df[top_k_predictors],y_train)
predictions_top_features=clf.predict(scaled_features_test_df[top_k_predictors])
score_top_features=accuracy_score(y_test,predictions_top_features)
print(score_top_features)



