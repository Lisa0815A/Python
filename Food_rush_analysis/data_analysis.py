import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import random

#-------------------------------------------
#01. Data Generation for Food Rush Analysis
#-------------------------------------------

#number of orders 10,000
num_orders = 10000

#Date range for 5 years
start_date = datetime(2020,1,1)
end_date = datetime(2025,1,1)
date_range = pd.date_range(start_date,end_date).to_pydatetime().tolist()

#sample dishes and categories
dishes = ['Pizza','Burger','Pasta','Sandwich','Fries','Coke','Salad','Icecream']
categories = ['Fast Food','Fast Food','Italian','Fast Food','Fast Food','Beverage','Healthy','Dessert']
prices = [120,350,250,150,80,50,100,70]

#payment types and cities
payment_types = ['Cash','Card','Online']
cities = ['Berhampur','Bhubaneswar','Cuttack']

#generate random data
data = []
for i in range(num_orders):
  idx =random.randint(0,len(dishes)-1)
  date = random.choice(date_range)
  time = datetime.strptime(f"{random.randint(10,22)}:{random.randint(0,59)}","%H:%M").time()
  quantity = random.randint(1,5)
  price = prices[idx]
  total = price * quantity
  payment = random.choice(payment_types)
  city = random.choice(cities)
  rating = random.randint(1,5)

  data.append([i+1,date.date(),time,dishes[idx],categories[idx],quantity,price,total,payment,city,rating])

  #creating dataframe
  df = pd.DataFrame(data,columns = ["OrderID","Date","Time","Dish","Category","Quantity","Price","Total","PaymentType","City","Rating"])

  #save to csv
  df.to_csv("Food_rush_data.csv",index=False)
  print("Data generated and saved to Food_rush_data.csv")