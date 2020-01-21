from datetime import datetime 
import pandas as pd  
import numpy as np

a = pd.to_datetime('22-01-2020',format='%d-%m-%Y')
b = pd.to_datetime('22-01-2019',format='%d-%m-%Y')

c = a-b
print(c)