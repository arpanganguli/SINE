#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:13:47 2021

@author: arpanganguli
"""

# import packages
import sqlalchemy as sa
import pandas as pd
from sqlalchemy import create_engine

# create engine
engine= create_engine('sqlite:////Users/arpanganguli/Documents/GitHub/SINE/Database/CCS.db', echo=True) # sqlite:////absolute/path/to/file.db

query_string = "SELECT * FROM CCS"
df = pd.read_sql(sql=query_string, con=engine)

print(df.head())