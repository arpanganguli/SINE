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

# import files
HOME = os.path.dirname(os.getcwd())
URL = 'sqlite:///' + os.path.join(HOME, 'Database/CCS.db')

engine = create_engine(URL, echo = True) # sqlite:////absolute/path/to/file.db
# ALITER: engine = create_engine('sqlite:////Users/arpanganguli/Documents/Projects/SINE/Database/CCS.db', echo = True) # sqlite:////absolute/path/to/file.db

# initial query
query_string = "SELECT * FROM CCS"
df = pd.read_sql(sql=query_string, con=engine)
print(df.head())

df_working = df.copy(deep=True) # deep copy to preserve original dataframe
df_working.dropna(how="all") # delete null and na values
df_working.drop('Assembly Constituency Name', inplace=True, axis=1)

df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"
            ,"Occupation of Respondent"
            ,"Perception on General Economic condition - compared to one year ago"
            ,"Outlook on General Economic condition - one year ahead"
            ,"Perception on Household income - compared to one year ago"
            ,"Outlook on Household income - one year ahead"
            ,"Perception on Household spending - compared to one year ago"
            ,"Outlook on Household spending - one year ahead"                    
            ,"Perception on essential spending - compared to one year ago"       
            ,"Outlook on essential spending - one year ahead"                   
            ,"Perception on non-essential spending - compared to one year ago"    
            ,"Outlook on non-essential spending - one year ahead"                   
            ,"Perception on Employment scenario - compared to one year ago"    
            ,"Outlook on Employment scenario - one year ahead"                   
            ,"Perception on General prices - compared to one year ago"               
            ,"Outlook on General prices - one year ahead"                          
            ,"Perception on Inflation - compared to one year ago"                   
            ,"Outlook on Inflation - one year ahead"]] = df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"
            ,"Occupation of Respondent"
            ,"Perception on General Economic condition - compared to one year ago"
            ,"Outlook on General Economic condition - one year ahead"
            ,"Perception on Household income - compared to one year ago"
            ,"Outlook on Household income - one year ahead"
            ,"Perception on Household spending - compared to one year ago"
            ,"Outlook on Household spending - one year ahead"                    
            ,"Perception on essential spending - compared to one year ago"       
            ,"Outlook on essential spending - one year ahead"                   
            ,"Perception on non-essential spending - compared to one year ago"    
            ,"Outlook on non-essential spending - one year ahead"                   
            ,"Perception on Employment scenario - compared to one year ago"    
            ,"Outlook on Employment scenario - one year ahead"                   
            ,"Perception on General prices - compared to one year ago"               
            ,"Outlook on General prices - one year ahead"                          
            ,"Perception on Inflation - compared to one year ago"                   
            ,"Outlook on Inflation - one year ahead"]].astype('category')
df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"]] = df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"]].apply(lambda x: x.cat.codes)
print(df_working.head())
