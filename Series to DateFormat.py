#Convert the given series of string to date format
from datetime import datetime
import numpy as np
import pandas as pd 

dob = pd.Series(["08Oct17", "21Nov18", "31Dec19", "20Jan20"])
dob = dob.str[:-2] + ' 20' + dob.str[-2:]
#print(dob[:-2])
#print(dob[-2:])
#print(dob.str[:-2])
#print(dob.str[-2:])
print(dob)
pd.to_datetime(dob, format = '%d%b%Y')