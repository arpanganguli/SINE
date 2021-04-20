#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:50:34 2021

@author: arpanganguli
"""

# import packages
import sqlalchemy as sa
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

df_working = df.copy(deep=True)
print(df_working.head())

print(df_working.dtypes) # checking the data types of all columns

df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"
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

print(df_working.dtypes) # checking if the data types have changed to category

df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"]] = df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"]].apply(lambda x: x.cat.codes)

"""
df_working[["Age"
            ,"Gender"
            ,"Annual Income"
            ,"Educational Qualification"
            ,"No. of Family Members"
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
            ,"Outlook on Inflation - one year ahead"]].apply(lambda x: x.cat.codes)
                                                                     
df_working.drop(df_working[df_working[["Age"
                                      ,"Gender"
                                      ,"Annual Income"
                                      ,"Educational Qualification"
                                      ,"No. of Family Members"
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
                                      ,"Outlook on Inflation - one year ahead"]] == -1].index, inplace=True)


df_working.drop(df_working[df_working[["Age", "Gender"]] == -1].index, inplace=True)
"""


