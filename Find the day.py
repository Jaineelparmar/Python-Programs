#From the given date find the day on that date
#(%A = Day, %d = Date, %B = Month, %Y = Year)

from datetime import datetime
import pandas as pd 
import numpy as np

current_date = pd.to_datetime("20Jan2020")
print(current_date)

day = current_date.strftime('%A %d %B %Y')
print(day)