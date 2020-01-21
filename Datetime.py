#Find the past and future dates from the given current date.
from datetime import datetime
import pandas as pd
import numpy as np


#Past date (10 days back)
current_date = pd.to_datetime('20-01-2020', format='%d-%m-%Y')
#print(current_date)
diff = pd.DateOffset(10)
#print(diff)
new_date = current_date - diff
print("The new date is", new_date)


#Future date (10 days ahead)
current_date = pd.to_datetime('20-01-2020', format='%d-%m-%Y')
#print(current_date)
diff = pd.DateOffset(10)
#print(diff)
new_date = current_date + diff
print("The new date is", new_date)