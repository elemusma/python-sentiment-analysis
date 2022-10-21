import pandas as pd # import the pandas library
from datetime import datetime

df1 = pd.read_csv("TSLA-Headlines.csv", encoding='windows-1250', header=None)
df1.columns=['Title','Date']
# print(df1)

newDate1 = datetime.strptime('Dec. 6, 2019', '%b. %d, %Y').date()
print(newDate1)