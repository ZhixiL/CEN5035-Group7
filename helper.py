import pandas as pd
import csv

def writeToCSV(responseList, fileName, headers):
    df = pd.DataFrame(responseList, columns=headers)
    df.to_csv(fileName, index=False)  

def readCSV(fileName):
    return list(csv.reader(open(fileName,encoding='UTF-8')))[1:]
