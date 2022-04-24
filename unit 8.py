#######################################################
# Name:       Michael Cunningham
# Class:      CIS-2531-VCM01
# Assignment: Homework 8
# Instructor: Mohammad Morovati
# Purpose:    reading/sorting Gas Prices
######################################################
import pandas as pd 

data = pd.read_csv('GasPrice.txt', sep=":", header=None, names=["Dates", "Price"])
df = pd.DataFrame(data)
#Converting object formatted date in mm-dd-yyyy to date format in yyyy-mm-dd
df['Dates']= pd.to_datetime(df['Dates'])

print("\n---Average Price per year---")
result = df.groupby(df.Dates.dt.to_period("Y"))['Price'].mean()
for year, records in result.items():
    print(f"Average price of {year} = {records}")

print("\n---Average Price per Month---")
result = df.groupby(df.Dates.dt.to_period("M"))['Price'].mean()
for month, records in result.items():
    print(f"Average price of {month} = {records}")

print("\n---Highest Price Per year---")
result = df.groupby(df.Dates.dt.to_period("Y"))['Price'].max()
for year, records in result.items():
    print(f"Highest price of {year} = {records}")

print("\n---Lowest Price Per year---")
result = df.groupby(df.Dates.dt.to_period("Y"))['Price'].min()
for year, records in result.items():
    print(f"Lowest price of {year} = {records}")

#gas_price_ascending.txt is written with the List of Price, Lowest to Highest
result = df.sort_values(by=["Price"],ascending=True)
result.to_csv('gas_price_ascending.txt', header=False, index=False, sep=':', mode='a')
#gas_price_decending.txt is written with the List of Price, Highest to Lowest
result = df.sort_values(by=["Price"],ascending=False)
result.to_csv('gas_price_decending.txt', header=False, index=False, sep=':', mode='a')