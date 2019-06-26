# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",", skip_header=1)
print(data)
data = np.asarray(data)
print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.asarray(new_record)
print(new_record)

#Code starts here
census =np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)



age_mean=np.mean(age)
print(age_mean)

age_std=np.std(age)
print(age_std)


# --------------
#Code starts here
#Code starts here

#high=census[census[:,1]>10]


race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)

if len_0 <=min(len_0,len_1,len_4,len_3,len_2):
    minority_race=0
if len_1 <=min(len_0,len_1,len_4,len_3,len_2):
    minority_race=1
if len_2 <=min(len_0,len_1,len_4,len_3,len_2):
    minority_race=2
if len_3 <=min(len_0,len_1,len_4,len_3,len_2):
    minority_race=3
else:
    minority_race=4

print(minority_race)


# --------------
#Code starts here

senior_citizens=census[census[:,0]>60]
working_hours_sum=0
senior_citizens_len=0

working_hours_sum =sum(senior_citizens[:,6])

senior_citizens_len=len(senior_citizens)
avg_working_hours = (working_hours_sum)/senior_citizens_len

print(working_hours_sum)
print(senior_citizens_len)
print(avg_working_hours)






# --------------
#Code starts here
high=census[census[:,1]>10]
avg_pay_high=0
avg_pay_low=0
low=census[census[:,1]<=10]
count1=0
count2=0

print(high)
print(low)

avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])

print(avg_pay_high)
print(avg_pay_low)


