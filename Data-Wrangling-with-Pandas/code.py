# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 


bank=pd.read_csv(path)
#print(bank)
# code starts here

categorical_var=bank.select_dtypes(include = 'object')

print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')

print(numerical_var)





# code ends here


# --------------
# code starts here


#code ends here
banks=bank.drop('Loan_ID', axis=1)
#print(banks)

sums=banks.isnull().sum()
print(sums)

bank_mode=banks.mode
print(bank_mode)

banks=banks.fillna(bank_mode)
print(banks)


# --------------
# code starts here





# check the avg_loan_amount
avg_loan_amount = banks.pivot_table(index=["Gender","Married","Self_Employed"],values="LoanAmount")


print (avg_loan_amount)
# code ends here


# --------------
# code starts here





loan_approved_se=len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']== 'Y')])

loan_approved_nse=len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status']== 'Y')])
# code ends here

percentage_se=(loan_approved_se/614)*100
print(percentage_se)

percentage_nse=(loan_approved_nse/614)*100
print(percentage_nse)


# --------------
# code starts here

loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)

#print(loan_term)


big_loan_term=len(loan_term[loan_term >=25])

print(big_loan_term)
# code ends here


# --------------
# code starts here


loan_groupby =banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']

mean_values=loan_groupby.agg(np.mean)

# code ends here


