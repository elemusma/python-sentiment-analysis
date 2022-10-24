import pandas as pd # import the pandas library
from datetime import datetime
# import csv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

# nltk.download('vader_lexicon')

df1 = pd.read_csv("TSLA-Headlines.csv")
df1.columns=['Title','Date','Score']

dfEodPrice = pd.read_csv('TSLA-Historical-Data.csv')
# dfEodPrice2 = pd.read_csv('TSLA-HD.csv')
# print(dfEodPrice)
# type(dfEodPrice['Date'][1])
# print(df1)
dfEodPrice['Date'] = dfEodPrice['Date'].astype('datetime64[ns]')
# dfEodPrice.to_csv('TSLA-Historical-Data.csv')
# print(dfEodPrice['Date'][1])

# dfEodPrice2 = dfEodPrice.drop(['Open','High','Low','Close','Volume'], axis=1) 
#drop unwanted rows
# dfEodPrice2.set_index('Date', inplace=True) #set date column as index
# dfEodPrice2.to_csv('TSLA-Historical-Data.csv', index=['Date'])

dfEodPrice['Returns'] = dfEodPrice['Adj Close']/dfEodPrice['Adj Close'].shift(1) - 1 # calculate daily returns
dfEodPrice.to_csv('TSLA-Historical-Data.csv')
# print(dfEodPrice)


# newDate1 = datetime.strptime('Dec. 6, 2019', '%b. %d, %Y').date()
# print(newDate1)

# newDate2 = datetime.strptime('20 Oct 2022', '%d %b %Y').date()
# print(newDate2)

# for dateOfArticles in df1['Date']:
#     newdate=datetime.strptime(dateOfArticles, '%d %b %Y').date()
    # print(newdate)
    # df1['Date'] = df1['Date'].replace({dateOfArticles, newdate})
    # df1.to_csv('TSLA-Headlines.csv')
    # print(df1['Date'])
    # print(dateOfArticles)

# print(df1['Date'])
# print(df1.columns)



results = []

for headline in df1['Title']:
    pol_score = SIA().polarity_scores(headline) # run analysis
    pol_score['headline'] = headline # add headlines for viewing
    results.append(pol_score)

# print(results)

df1['Score'] = pd.DataFrame(results)['compound']
# df1.to_csv('TSLA-Headlines.csv')
# print(df1)

# df2 = df1.groupby(['New Date']).sum()
# df1['New Date'] = df1.to_csv('TSLA-Headlines.csv')