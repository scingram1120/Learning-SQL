#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import this module to initiate SQL in every notebook
# type import SQL
# then call the function inside this module for it to take effect
# 'SQL.import_SQL()'
# Download this as a py (File> Download as python)
# Move the py in the same directory as the file you want to import
# this module in
def import_SQL():
    import os
    import psycopg2 as ps
    import pandas as pd


    get_ipython().system('pip install ipython-sql')


    import sqlalchemy


    sqlalchemy.create_engine('postgresql://scott:tiger@localhost/mydatabase')


