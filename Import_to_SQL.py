#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:35:34 2021

@author: arpanganguli
"""

# import packages

import pandas as pd
from sqlalchemy import create_engine

# import files

url = r'/Users/arpanganguli/Documents/Professional/Projects/SINE/Database/CCS/CCS_201209.xlsx'
df = pd.read_excel(url)
print(df.head())

# format: mysql://user:pass@host/db

engine = create_engine('mysql://arpanganguli:arpanganguli@localhost/contacts')
