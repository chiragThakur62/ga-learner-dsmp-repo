# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
#Code starts here 

data['Gender'].replace('-','Agender',inplace=True)

gender_count=data['Gender'].value_counts()

print(gender_count)
gender_count.plot.bar(rot=0, subplots=True)
#plt.bar(data['Gender'],gender_count)
#plt.show()


# --------------
#Code starts here
alignment=data['Alignment'].value_counts()

alignment.plot.pie()


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]


sc_covariance=sc_df.cov().iloc[0,1]
print(sc_covariance)

sc_strength=sc_df['Strength'].std()
print(sc_strength)

sc_combat=sc_df['Combat'].std()
print(sc_combat)

sc_pearson= sc_covariance/(sc_strength*sc_combat)




ic_df=data[['Intelligence','Combat']]


ic_covariance=ic_df.cov().iloc[0,1]
print(ic_covariance)


ic_intelligence=ic_df['Intelligence'].std()
print(ic_intelligence)



ic_combat=ic_df['Combat'].std()
print(ic_combat)

ic_pearson= ic_covariance/(ic_intelligence*ic_combat)



# --------------
#Code starts here


total_high=data['Total'].quantile(.99)

super_best=data[data['Total'] > total_high]

super_best_names=list(super_best['Name'])

print(super_best_names)



# --------------
#Code starts here



f, (ax_1, ax_2 , ax_3) = plt.subplots(3)

data.boxplot(column='Intelligence',ax=ax_1)
ax_1.set_title('Intelligence')


data.boxplot(column='Speed',ax=ax_2)
ax_2.set_title('Speed')

data.boxplot(column='Power',ax=ax_3)
ax_3.set_title('Power')



