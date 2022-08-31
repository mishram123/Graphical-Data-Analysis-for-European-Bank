import pandas as pd
from matplotlib import pyplot as plt
import csv

plt.style.use('seaborn')

data = pd.read_csv('Bank Customer Churn Prediction.csv')
rows = []
with open("Bank Customer Churn Prediction.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

age_clean = []
avg_credit_age = []
avg_credit_card_status = []
credit_card_status = []
card_status = ['yes', 'no']
sex = []
avg_credit_sex = []
avg_salary_sex = []
countries = []
countries_balance = []


for item in rows:
    if item[4] not in age_clean:
        age_clean.append(item[4])
        age_temp = item[4]
        counter = 0
        sum=0
        for item1 in rows:
            if item1[4] == age_temp:
                sum+= int(item[1])
                counter+=1
        avg_credit = sum/counter
        avg_credit_age.append(avg_credit)
    if item[8] not in credit_card_status:
        credit_card_status.append(item[8])
        temp = item[8]
        counter = 0
        sum = 0
        for item1 in rows:
            if item1[8] == temp:
                sum+= int(item[1])
                counter+=1
        avg_credit = sum/counter
        avg_credit_card_status.append(avg_credit)
    if item[3] not in sex:
        sex.append(item[3])
        temp = item[3]
        counterCredit = 0
        sumCredit = 0
        counterSalary = 0
        sumSalary = 0
        for item1 in rows:
            if item1[3] == temp:
                sumCredit+= int(item[1])
                counterCredit+=1
                sumSalary+=float(item[10])
                counterSalary+=1
        avg_credit = sumCredit / counterCredit
        avg_credit_sex.append(avg_credit)
        avg_salary = sumSalary/counterSalary
        avg_salary_sex.append(avg_salary)
    if item[2] not in countries:
        countries.append(item[2])
        temp = item[2]
        sumBalance = 0
        for item1 in rows:
            if item1[2] == temp:
                sumBalance += float(item1[6])
        countries_balance.append(sumBalance)

countries_balance_total = 0
for item in countries_balance:
    countries_balance_total += item

countries_balance_percentage = []
for item in countries_balance:
    percent = float(item)/countries_balance_total
    countries_balance_percentage.append(percent)


plot1 = plt.figure(1)
plt.scatter(age_clean, avg_credit_age, c = 'black' , cmap='viridis', alpha = 0.8)

plt.xscale('linear')
plt.yscale('linear')

plt.title('Average Credit Score by Age', fontsize = 25)
plt.xlabel('Age', fontsize = 18)
plt.ylabel('Average Credit Score', fontsize = 18)

plot2 = plt.figure(2)
colors = ['blue', 'red']
plt.barh(card_status, avg_credit_card_status, color = colors)

plt.title('Average Credit Score by Card Ownership', fontsize = 25)
plt.xlabel('Average Credit Score', fontsize = 18)
plt.ylabel('Ownership', fontsize = 18)

for i, v in enumerate(avg_credit_card_status):
    plt.text(v+3, i+0.25, str(v), color = 'black', fontsize = 8, fontweight = 'bold')


plot3 = plt.figure(3)
colors = ['blue', 'red']
plt.barh(sex, avg_credit_sex, color = colors)

plt.title('Average Credit Score by Sex', fontsize = 25)
plt.xlabel('Average Credit Score', fontsize = 18)
plt.ylabel('Sex', fontsize = 18)

for i, v in enumerate(avg_credit_sex):
    plt.text(v+3, i+0.25, str(v), color = 'black', fontsize = 8, fontweight = 'bold')

plot4 = plt.figure(4)
colors = ['blue', 'red']
plt.barh(sex, avg_salary_sex, color = colors)

plt.title('Average Salary by Sex', fontsize = 25)
plt.xlabel('Average Salary', fontsize = 18)
plt.ylabel('Sex', fontsize = 18)

for i, v in enumerate(avg_salary_sex):
    plt.text(v+3, i+0.25, str(v), color = 'black', fontsize = 8, fontweight = 'bold')

plot5 = plt.figure(5)
plt.pie(countries_balance_percentage, labels = countries, autopct='%1.1fR', shadow = True, startangle= 90)

plt.title('Percentage Wealth Ownership by Country')
plt.legend(countries, title = 'Countries', loc = "center left", bbox_to_anchor = (1, 0, 0.5, 1))



plt.show()