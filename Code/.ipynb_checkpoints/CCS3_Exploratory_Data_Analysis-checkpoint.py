#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:50:34 2021

@author: arpanganguli
"""

# import packages
import pandas as pd
from sqlalchemy import create_engine
import os
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

# import files
HOME = os.path.dirname(os.getcwd())
URL = 'sqlite:///' + os.path.join(HOME, 'Database/CCS.db')

engine = create_engine(URL, echo = True) # sqlite:////absolute/path/to/file.db
# ALITER: engine = create_engine('sqlite:////Users/arpanganguli/Documents/Projects/SINE/Database/CCS.db', echo = True) # sqlite:////absolute/path/to/file.db

# initial query
query_string = "SELECT * FROM CCS"
df = pd.read_sql(sql=query_string, con=engine)
print(df.head())

# barplot - 'Perception on Inflation - compared to one year ago'
# sns.set_style("dark")
# sns.countplot(x=df["Round"], hue=df["City"])
# plt.xticks(rotation=90)
# plt.legend(loc="lower left")

for i in df.columns[12:]:
    fig = plt.figure()
    sns.set_style("dark")
    sns.countplot(x=df["Round"], hue=df[i])
    plt.xticks(rotation=90, label="round")
    plt.title(i)
    fig.savefig(HOME+"/Plots/"+i+".png")