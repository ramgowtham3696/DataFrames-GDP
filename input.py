import pandas as pd
import numpy as np
energy2=pd.read_excel('energy1.xls')
df1=pd.DataFrame(energy2)
df1.columns.values[0] = 'Country'
df2=df1.drop([0])
df2['Energy Supply']*=1000000
df3=df2.set_index('Country')
df4=df3.rename(index={"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"})

#GDP..............................
gdp1=pd.read_csv('world.csv',skiprows=4)
gdp2=pd.DataFrame(gdp1)
gdp3=gdp2.rename(columns={'Country Name':'Country'})
gdp4=gdp3.set_index('Country')
gdp5=gdp4.rename(index={"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"})
gdp6=gdp5.drop(gdp3.columns[[60,61,62]],axis=1)
#print(gdp6.head())
#Scimen.................................
scimen1=pd.read_excel('scimagojr.xlsx')
scimen2=pd.DataFrame(scimen1)
scimen=scimen2.set_index('Country')
d_1=pd.merge(pd.merge(df4,gdp6,on='Country'),scimen,on='Country')
print(d_1.head())