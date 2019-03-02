# Stock Data Analysis


2015-16 Daily OHLCV Data Anaysis for INFY & TCS

-- Created 4,16,....,52 week moving average(closing price) for each stock and index through a function.

-- Handled unequal time series due to stock market holidays.

--Created rolling window of size 10 on each stock/index and then increased the rolling window size to 75 to see how the data looks like.

--Created the following dummy time series:
   1 Volume shocks - If volume traded is 10% higher/lower than previous day - a 0/1 boolean time series for shock, 0/1 dummy-coded time series for direction of shock.
   2 Price shocks - If closing price at T vs T+1 has a difference > 2%, then 0/1 boolean time series for shock, 0/1 dummy-coded time series for direction of shock.
   3 Pricing black swan - If closing price at T vs T+1 has a difference > 2%, then 0/1 boolean time series for shock, 0/1 dummy-coded time series for direction of shock.
   4 Pricing shock without volume shock - based on points a & b - Make a 0/1 dummy time series.
   
--Made 2 multivariaate regression models. The goal was to to predict INFY,TCS prices for tomorrow.
