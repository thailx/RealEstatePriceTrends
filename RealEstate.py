# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xioyEGfgw5Lo7zVA6VToNBPSNLqvAvGJ
"""

import pandas as pd

from google.colab import files

upload = files.upload()

data_all = pd.read_csv('report.csv')

df = data_all.groupby('poster_temp')['time'].count().reset_index()
df = df.sort_values(by=['time'])
df.tail()

data_city = data_all.groupby('area_temp').count().reset_index()
data_city.head(100)
data_city = data_city.sort_values(by=['time'])

df_draw = data_city[-5:].copy()
new_row = pd.DataFrame(data={
    'area_temp': ['Others'],
    'time': [df['time'][:-5].sum()]
})
df_draw = pd.concat([df_draw, new_row])

df_draw.set_index('area_temp', inplace=True)
df_draw.plot.pie(y='time')

data_city = data_all.groupby('area_temp').sum().reset_index()
data_city = data_city.sort_values(by=['final_price'])
data_city.tail(100)

df_draw = data_city[-5:].copy()
new_row = pd.DataFrame(data={
    'area_temp': ['Others'],
    'final_price': [data_city['final_price'][:-5].sum()]
})
df_draw = pd.concat([df_draw, new_row])
df_draw.head(10)

df_draw.set_index('area_temp', inplace=True)
df_draw.plot.pie(y='final_price', autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.3, legend=0)

data_city_mm = data_all.groupby('area_temp').agg({"final_price": "max"})
data_city_mm.sort_values(by=['final_price'], inplace=True)

data_city_mm.plot.bar(figsize=(30, 10))

data_city_mm = data_all.groupby('area_temp')['final_price'].mean().reset_index()
data_city_mm.sort_values(by=['final_price'], inplace=True)
data_city_mm.head(100)

data_city_mm.set_index('area_temp', inplace=True)
data_city_mm.plot.bar(figsize=(25, 10))

"""# New Section"""
