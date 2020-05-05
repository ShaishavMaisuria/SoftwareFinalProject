#Author Shaishav Maisuria
#this is file which has deaths occured gloablly
#JHU datasets
# link website https://github.com/CSSEGISandData/COVID-19

import pandas as pd
import pathlib



df2 = pd.read_csv(str(pathlib.Path().absolute())+r"\datasetsJHU\time_series_covid19_deaths_global.csv")


df2.iloc[:,5]
header=list(df2.head(0))
header=header[5:]

dicForRowColumnDeathGlobally = {}
dicAllRowColumnDeathGlobally = {}
dicForRowSumDeathGlobally = {}
dicAllRowSumDeathGlobally = {}
TotalDeathCasesGlobally = 0

for row in header:
    columnDeathGlobally = df2.loc[:, row]
    date = row

    columnDeathGlobally = list(columnDeathGlobally)
    sumPerDay = sum(columnDeathGlobally)
    # print("sum Per day:",sumPerDay)
    TotalDeathCasesGlobally += sumPerDay
    # print("Total Number of Cases:",TotalCases)
    newdf = pd.DataFrame(columnDeathGlobally)
    dicForRowColumnDeathGlobally.clear()
    dicForRowColumnDeathGlobally = {
        date: columnDeathGlobally
    }
    dicAllRowColumnDeathGlobally.update(dicForRowColumnDeathGlobally)
    dicForRowSumDeathGlobally = {
        date: sumPerDay
    }
    dicAllRowSumDeathGlobally.update(dicForRowSumDeathGlobally)

print(dicAllRowSumDeathGlobally)
# print(dic2)
# print("Total Number of Cases:",TotalCases)
date = header
print("-------------------")
print(date)

dataframeDeathNew=pd.DataFrame(dicAllRowSumDeathGlobally, index=[0])
print(dataframeDeathNew)
date=dataframeDeathNew.keys()
print(date)
dataDeathGlobally=dataframeDeathNew.values[0]
print(dataDeathGlobally)






