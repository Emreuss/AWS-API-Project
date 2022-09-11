import pandas as pd
from faker import Faker
import random as rd
import requests
import time
import json


#URL = "https://xxxxxxxxxxxxxxx.amazonaws.com/O/orders"
#URL2 = "https://xxxxxxxxxxxxxxx.amazonaws.com/O/orders"

headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
}

data = pd.read_csv('OnlineRetail.csv', sep = ';')

data["InvoiceNo"] = data["InvoiceNo"].str.replace('A','')
data["InvoiceNo"] = data["InvoiceNo"].str.replace('C','')
data["InvoiceNo"] = data["InvoiceNo"].astype("int64")
data["StockCode"] = data["StockCode"].astype("string")
data["Description"] = data["Description"].astype("string")
data["UnitPrice"] = data["UnitPrice"].str.replace(',','.').astype("float")

cols = ['StockCode','Description', 'UnitPrice']
Stock_Desc_Unit_lst = data[cols].values.tolist()

fake = Faker()

def create_data(x):
    project_data = {}
    for i in range(x):
        project_data[i] = {}
        project_data[i]['CustomerID'] = i + 1
        project_data[i]['Name'] = fake.name()

    return project_data

df = pd.DataFrame(create_data(5000)).transpose()

cols = ['CustomerID','Name']
CustomerID_Name = df[cols].values.tolist()
Q_df = data[data["Quantity"]>0]
Quantity = Q_df["Quantity"].values.tolist()


import datetime; 
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#while True:
for i in range(1):
    order={}
    survey={}
    n = rd.randint(1,10)
    time.sleep(rd.randint(1,15))
    CID_Name = rd.choice(CustomerID_Name)
    order["CustomerID"]= CID_Name[0]
    order["CustomerName"] = CID_Name[1]
    order["Email"] = CID_Name[1].lower().replace(' ','.') + "@gmail.com"
    order["Address"] = fake.address().replace('\n',' ')
    order["PhoneNumber"] = fake.phone_number()[0:10]
    order["InvoiceDate"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    survey["IsOkayProductDescription"] = rd.randint(1,5)
    survey["IsOkayUserInterface"] = rd.randint(1,5)
    survey["GeneralEvaluation"] = rd.randint(1,5)
    survey["WillKeepOrdering"] = rd.randint(1,5)
    #response2 = requests.post(URL2, json = survey, headers=headers)
    print(survey)
    #print(response2)
    for a in range(n):
        Stock_Desc_Unit = rd.choice(Stock_Desc_Unit_lst)
        order["StockCode"] = Stock_Desc_Unit[0]
        order["Description"] = Stock_Desc_Unit[1]
        order["UnitPrice"] = Stock_Desc_Unit[2]
        order["Quantity"]  = rd.choice(Quantity)
        order_json = json.dumps(order)
        #response = requests.post(URL, json = order, headers=headers)
        print(order_json)
        #print(response)
    
    