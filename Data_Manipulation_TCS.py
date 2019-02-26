#Importing Library for DataSelection
from nsepy import get_history
from datetime import date

import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

df = get_history(symbol='INFY',
                   start=date(2015,1,1),
                   end=date(2015,12,31))

#Since only OCLHV source data is required
df = df[['Open','High', 'Low','Close','Volume']]

##Visualizing Stock Data
 ##df.plot() 
 ##plt.show()


##Calculation of Week Moving Averages with a function
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
df= df.asfreq('D',method = 'pad')






## 10 Days MA & 75 Days MA after handling Stock Market Holidays
df['10D MA'] = df['Close'].rolling(window = 10).mean()
df['75D MA'] = df['Close'].rolling(window = 75).mean()







##Visualizing 10 Days MA and 75 Days MA
ax1 = plt.subplot2grid((12,1),(0,0),rowspan = 12, colspan = 1)

ax1.plot(df.index,df['10D MA'])
ax1.plot(df.index,df['75D MA'])
plt.show()









##Volume Shock
df_volume = df.Volume
volume_shock = []
volume_direction = []
for i in range(1,df_volume.shape[0]):
    if(abs(df_volume[i]-(df_volume[i-1]))>(df_volume[i-1]*10/100)): ##Volume Shock -  Difference is greater than 10 percent
        volume_shock.append(1)
        volume_direction.append('Positive')
    else:
        volume_shock.append(0)
        volume_direction.append('Negative')

      
volume_shock.insert(0,0) ## Adding first element as 0 in the list 
volume_direction.insert(0,'None') 
df = df.assign(VolumeShock = volume_shock, VolumeDirection = volume_direction)









##Price Shock
df_price = df.Close

price_shock = []
price_direction = []
for i in range(0,df_price.shape[0]-1):
    if(abs(df_price[i+1]-(df_price[i]))>(df_price[i]*2/100)): ##Price Shock -  Difference is greater than 2 percent
        price_shock.append(1)
        price_direction.append('Positive')
    else:
        price_shock.append(0)
        price_direction.append('Negative')
        
      
price_shock.insert(len(price_shock),0) ## Adding last element as 0 in the list
price_direction.insert(len(price_direction),'None') 
df = df.assign(PriceShock = price_shock, PriceDirection = price_direction)








##Pricing Shock Without Volume Shock
df_pv= df.loc[:, ['VolumeShock','PriceShock']].values
pv_shock = []
for i in range(0,df_pv.shape[0]):
    if(df_pv[i,0]==0 and df_pv[i,1]==1):
        pv_shock.append(1)
    else:
        pv_shock.append(0)
        
df = df.assign(PriceWithoutVolumeShock = pv_shock)





df.to_csv('INFY.csv')        
        
        
        
    

    




