# Graphical-Data-Analysis

I am very interested in the world of data science. I decided to do this project to help me learn and understand basic data science principles. I intend to use this learning experience to catapult me towards future, more complex, data analysis.

I have uploaded the csv data file I used. It contains data from a bank in Europe regarding credit scores, account holder sex, credit card ownership status, etc..

With This data, I want to answer statistical questions and use python programming and matplotlib to find answers.

First Question: Is there a linear correlation between an account holder's age and their credit score?
To solve this question, I parsed through the data and found the average credit scores for each age. Then I plotted the results on a scatter plot.

![CreditScorebyAge](https://user-images.githubusercontent.com/56270716/187733603-289cbb8e-5d98-486a-9aab-3cb1353d568b.png)

From this graph, we can see that there is no linear correlation between an account holders age and their credit score

Second Question? Does Credit card ownership or an account holder's sex make a difference on their credit score?
To solve this question, I again parsed through the data to find average credit scores for different sexes and credit card ownership status. I then decided to make a bar plot as it is an easy way of noticing large difference between values.

![CreditScorebyCardStatus](https://user-images.githubusercontent.com/56270716/187735017-5515263a-9047-4fff-ba40-f2fc7adeb88d.png)

![CreditScorebySex](https://user-images.githubusercontent.com/56270716/187735047-183e5146-4899-4984-897e-a7d1c5c9133e.png)

From this data, we find that credit card ownership and an account holder's sex do not influence credit score as their values are relatively similar to one another.

For card ownership, there is only a 1.79% difference in credit score between card holders and non-holders. With such a small margin, we cannot conclude that card ownership affects credit score

For account holder sex, there is only a 4.11% difference in credit score between male and female account holders. With such a small margin, we cannot conclude that sex affects credit score. Other factors may come into play to explain the 4% difference

Third Question: Is there a significant gender pay gap in Western Europe?
To solve this question, I again parsed through the data to find average estimated salaries for different sexes. I then decided to make a bar plot as it is an easy way of noticing large difference between values.

![SalarybySex](https://user-images.githubusercontent.com/56270716/187736895-df4156c3-009d-43d0-9b63-74982538b1de.png)

With over 38% difference in salaries between the sexes. There is surely an imbalance between the salaries or men and women on average. While this statistic may be alarming. It is important to note this statistic does not take into account account holder occupation. This statistic only represents the general sample of account holders at this bank. More information is required to better understand this disparity: Are there differences in occupation between the sexes? Are more men working higher paying jobs? Is there a small minority of men skewing the data? Are men paid more than women in the same occupation? These are just a few questions we can answer if provided more data.

Final Question: What is the proportion of wealth in the bank for each country?
I found the total balance of all French, German, and Spanish account holders. Then I made a pie chart to see how the each country affects the total distribution of wealth.

![WealthbyCountry](https://user-images.githubusercontent.com/56270716/187738654-53aead98-db44-42a7-a211-5cd016e16155.png)

Here, we can see that German and French account holders hold almost equal portions of wealth in the bank. However, the Spanish account holders hold close to half the percentages of the other two nations. We can use our data or find more data to evaluate possible reasons. 1: Could there be significantly more french and german account holders? Do spanish account holders make less money than their wester EU counterparts? Was Spain facing economic downturn at the time of this study?

Overall, This project was just the beginning of my adventures in data analytics. I intend to improve my skills. I may either come back and extrapolate more concolusions from this data, or take my skills to another csv file.

