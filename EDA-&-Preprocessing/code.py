# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(path)
#print(data['Rating'])

data.hist(column='Rating', bins=20)

data=data[data['Rating']<=5]

data.hist(column='Rating', bins=20)
#Code ends here


# --------------
# code starts here


# code ends here
total_null=data.isnull().sum()

percent_null=(total_null/data.isnull().count())

missing_data=pd.concat([total_null, percent_null],keys=['Total','Percent'] ,axis=1)

print(missing_data)

data.dropna(inplace=True)


total_null_1=data.isnull().sum()

percent_null_1=(total_null_1/data.isnull().count())

missing_data_1=pd.concat([total_null_1, percent_null_1],keys=['Total','Percent'] ,axis=1)


print(missing_data_1)


# --------------

#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box" , height = 10)

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

data['Installs'].value_counts()


#data['Installs']=data['Installs'].str.translate(None, ",")
#data['Installs'] = data['Installs'].astype(int)
data['Installs']=data['Installs'].str.replace(r'+', '')
data['Installs']=data['Installs'].str.replace(r',', '')

data['Installs']=data['Installs'].astype(int)
#Code ends here

le=LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])





# --------------
#Code starts here

data['Price'].value_counts()


#data['Installs']=data['Installs'].str.translate(None, ",")
#data['Installs'] = data['Installs'].astype(int)
data['Price']=data['Price'].str.replace(r'$', '')

data['Price']=data['Price'].astype(float)
#Code ends here






# --------------

#Code starts here

data['Genres'].unique()
data['Genres']=data['Genres'].str.split(';',n=1,expand=True)
#data['Genres']=data['Genres'].head(1)
#Code ends here

gr_mean = data.groupby(['Genres'],as_index=False)[['Rating']].mean()

gr_mean.describe()

gr_mean=gr_mean.sort_values(by='Rating', ascending=True)


# --------------

#Code starts here


#print(data['Last Updated'])

#Code ends here

data['Last Updated']=pd.to_datetime(data['Last Updated']) 

max_date=pd.to_datetime(max(data['Last Updated']))

print(max_date)
print(data['Last Updated'].head(1))


data['Last Updated Days']=(max_date-data['Last Updated']).dt.days
print((data['Last Updated Days'].head(1)))




