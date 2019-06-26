# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here


df=pd.read_csv(path)
p_a=len(df[df['fico']>700])/len(df)

print(p_a)

p_b=len(df[df['purpose']=='debt_consolidation'])/len(df)

print(p_b)

df1=df[df['purpose']=='debt_consolidation']

p_a_b=len(df1[df1['fico']>700])/len(df1)

print(p_a_b)

result=(p_a_b==p_b)


print(result)






# code ends here


# --------------
# code starts here


prob_lp=len(df[df['paid.back.loan'] == 'Yes'])/len(df)


prob_cs=len(df[df['credit.policy'] == 'Yes'])/len(df)


new_df=df[df['paid.back.loan'] == 'Yes']


prob_pd_cs=len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)

print(prob_pd_cs)
bayes=prob_pd_cs*prob_lp/prob_cs

print(bayes)

# code ends here


# --------------
# code starts here



# code ends here

df['purpose'].value_counts().plot.bar()

df1=df[df['paid.back.loan'] == 'No']

df1['purpose'].value_counts().plot.bar()


# --------------
# code starts here



inst_median=df['installment'].median()

inst_mean=df['installment'].mean()
# code ends here

df['installment'].hist(bins=3)


inst_median=df['log.annual.inc'].median()

insta_mean=df['log.annual.inc'].mean()
# code ends here

df['log.annual.inc'].hist(bins=3)


