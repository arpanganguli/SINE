# import packages

import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, NVARCHAR, DateTime
import os
import glob

# create SQL database

engine = create_engine('sqlite:////Users/arpanganguli/Documents/Professional/Projects/SINE/Database/CCS.db', echo = True) # sqlite:////absolute/path/to/file.db

meta = MetaData()

CCS = Table(
    'CCS', meta
    ,Column('Index', Integer)
    ,Column('Round', Integer)
    ,Column('Period', DateTime)
    ,Column('City', NVARCHAR)
    ,Column('Age', NVARCHAR)
    ,Column('Gender', NVARCHAR)
    ,Column('Annual Income', NVARCHAR)
    ,Column('Assembly Constituency Name', NVARCHAR)
    ,Column('Educational Qualification', NVARCHAR)
    ,Column('No. of Family Members', NVARCHAR)
    ,Column('No. of Earning members in the family', Integer)
    ,Column('Occupation of Respondent', NVARCHAR)
    ,Column('Perception on General Economic condition - compared to one year ago', NVARCHAR)
    ,Column('Outlook on General Economic condition - one year ahead', NVARCHAR)
    ,Column('Perception on Household income - compared to one year ago', NVARCHAR)
    ,Column('Outlook on Household income - one year ahead', NVARCHAR)
    ,Column('Perception on Household spending - compared to one year ago', NVARCHAR)
    ,Column('Outlook on Household spending - one year ahead', NVARCHAR)
    ,Column('Perception on essential spending - compared to one year ago', NVARCHAR)
    ,Column('Outlook on essential spending - one year ahead', NVARCHAR)
    ,Column('Perception on non-essential spending - compared to one year ago', NVARCHAR)
    ,Column('Outlook on non-essential spending - one year ahead', NVARCHAR)
    ,Column('Perception on Employment scenario - compared to one year ago', NVARCHAR)
    ,Column('Outlook on Employment scenario - one year ahead', NVARCHAR)
    ,Column('Perception on General prices - compared to one year ago', NVARCHAR)
    ,Column('Outlook on General prices - one year ahead', NVARCHAR)
    ,Column('Perception on Inflation - compared to one year ago', NVARCHAR)
    ,Column('Outlook on Inflation - one year ahead', NVARCHAR)
    )

meta.create_all(engine)

# append all Excel files into one large database

root = r'/Users/arpanganguli/Documents/Professional/Projects/SINE/Database/CCS'

url = []
for root, dirs, files in os.walk(root):
    url += glob.glob(os.path.join(root, '*.xlsx'))
    
for file in url:
    df = pd.read_excel(file)
    df.to_sql('CCS', con=engine, if_exists='append')