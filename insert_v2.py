import pandas as pd
from faker import Faker
import random as rd
import requests
import time
import json


URL = "https://dt2lr5gew5.execute-api.eu-central-1.amazonaws.com/O/orders"

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

Quantity = data["Quantity"].values.tolist()


import datetime; 
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#while True:
for i in range(1):
    order={}
    n = rd.randint(1,10)
    time.sleep(rd.randint(1,15))
    CID_Name = rd.choice(CustomerID_Name)
    order["CustomerID"]=CID_Name[0]
    order["CustomerName"] = CID_Name[1]
    order["Address"] = fake.address()
    order["PhoneNumber"] = fake.phone_number()
    order["InvoiceDate"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for a in range(n):
        Stock_Desc_Unit = rd.choice(Stock_Desc_Unit_lst)
        order["StockCode"] = Stock_Desc_Unit[0]
        order["Description"] = Stock_Desc_Unit[1]
        order["UnitPrice"] = Stock_Desc_Unit[2]
        order["Quantity"]  = rd.choice(Quantity)
        order_json = json.dumps(order)
        response = requests.post(URL, json = order, headers=headers)
        print(order_json)
        print(response)