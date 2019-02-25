#Importing Library for DataSelection
from nsepy import get_history
from datetime import date

import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

df = get_history(symbol='TCS',
                   start=date(2015,1,1),
                   end=date(2015,12,31))

#Since only OCLHV source data is required
df = df[['Open','High', 'Low','Close','Volume']]

df.plot() ##Visualizing Stock Data
plt.show()


##Calculation of Week Moving Averages
##Assumption --Holidays are only on Saturdays and Sunday
def week_ma (x) :
    string = str(x) + ' Week MA'
    df[string] = df['Close'].rolling(window = 5*x).mean()
    ##Since the df does not contain the data for stock market holidays hence rolling window of 5 is used to calcuate moving average from weekday to weekday
    ##For example : 4 Week MA of a stock on Friday is calculated from Friday 4 weeks back
i = 4
while(i<=52):
    week_ma(i)
    i = i+12
    
##Handling Stock Market Holidays
df_holidays = df.iloc[[0,1]]
j = 2
while(j<=df.shape[0]):
    df_holidays = df_holidays.append(pd.Series(index=df.columns),ignore_index=True)
    df_holidays = df_holidays.append(pd.Series(index=df.columns), ignore_index=True)
    df_holidays = df_holidays.append(df.iloc[j:j+5])
    j = j+5


df['10D MA'] = df['Close'].rolling(window = 10).mean()
df['75D MA'] = df['Close'].rolling(window = 75).mean()

ax1 = plt.subplot2grid((12,1),(0,0),rowspan = 12, colspan = 1)


ax1.plot(df.index,df['10D MA'])
ax1.plot(df.index,df['75D MA'])
plt.show()

##Volume Shock




    
    
    




