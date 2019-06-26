# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv(path)


loan_status=data['Loan_Status'].value_counts()

loan_status.plot(kind='bar')
#Code starts here



# --------------
#Code starts here


property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))


plt.xlabel('Property Area')
plt.ylabel('Loan Status')

# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()


# --------------
#Code starts here

education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))


plt.xlabel('Education Status')
plt.ylabel('Loan Status')

# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()


# --------------
#Code starts here



graduate=data[data['Education'] == 'Graduate']

not_graduate=data[data['Education'] == 'Not Graduate']


graduate.plot( kind='density',label='Graduate')
not_graduate.plot( kind='density',label='Not Graduate')





#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here


fig ,(ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))
# Stacked bar-chart representing percentages

plt.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set_title('Applicant Income')

plt.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set_title('Coapplicant Income')


data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']


plt.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set_title('Total Income')



