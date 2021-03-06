#shaishav Maisuria
#this is file includes different dataset and it has all different implemtation such as
#date', 'states', 'positive', 'negative', 'pending', 'hospitalizedCurrently', 'hospitalizedCumulative', 'inIcuCurrently', 'inIcuCumulative', 'onVentilatorCurrently', 'onVentilatorCumulative', 'recovered', 'hash', 'dateChecked', 'death', 'hospitalized', 'posNeg', 'deathIncrease', 'hospitalizedIncrease', 'negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease'
#dataset from Covid 19 Tracking
#https://github.com/COVID19Tracking/covid-tracking-data/blob/master/data/us_daily.csv
#"NOTE: ""total"", ""posNeg"", ""hospitalized"" will be removed in the future." this is based on the repository so please keep in minnd


import pandas as pd
import pathlib


df2 = pd.read_csv(str(pathlib.Path().absolute())+r"\datasetsCovid19Tracking\us_daily.csv")


header=list(df2.head(0))

print(header)

dicForOneRow={}
dicAllRow={}
for row in header:
    column = df2.loc[:,row]
    name=row
    #print(name)
    column=list(column)
    column.reverse()
   # print(column)
    dicForOneRow.clear()
    dicForOneRow={
        name:column
    }
    dicAllRow.update(dicForOneRow)


date=dicAllRow['date']
states=dicAllRow['states']
positiveCases=dicAllRow['positive']
negativeCases=dicAllRow['negative']
pending=dicAllRow['pending']
hospitalizedCurrently=dicAllRow['hospitalizedCurrently']
hospitalizedCumulative= dicAllRow['hospitalizedCumulative']
inIcuCurrently=dicAllRow['inIcuCurrently']
inIcuCumulative=dicAllRow['inIcuCumulative']
onVentilatorCurrently= dicAllRow['onVentilatorCurrently']
recovered= dicAllRow['recovered']
death=dicAllRow['death']
hospitalized=dicAllRow['hospitalized']
deathIncrease= dicAllRow['deathIncrease']
hospitalizedIncrease=dicAllRow['hospitalizedIncrease']
negativeIncrease=dicAllRow['negativeIncrease']
positiveIncrease=dicAllRow['positiveIncrease']
totalTestResultsIncrease=dicAllRow['totalTestResultsIncrease']



