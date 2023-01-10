import numpy as np
import pandas_datareader as pd_web
import matplotlib.pyplot as plt
import datetime as dt


# class robot:
#     def __init__(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age
#
#     def introduce_self(self):
#         print("My name is " + self.name)
#
# r1 = robot('Gabriele', 'verde', 26)
# r1.introduce_self()

# class robot:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#
#     def introduce_self(self):
#         print("My name is " + self.name)
#
# r1 = Robot("Tom", "red", 30)
# r2 = Robot("Jerry", "blue", 40)
#
# r1.introduce_self()
# r2.introduce_self()


class GetData:
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end

    def price_collection(self):
        price = pd_web.get_data_yahoo(self.ticker, self.start, self.end)
        price = price["Adj Close"].dropna()

        return price

class EquityCurve:
    def __init__(self, price):
        self.price = price

    def plot_equity_curve(self):
        plt.figure(figsize = (7.5, 5))
        ax = self.price.iloc[:, 0].plot(label = 'MSFT')
        self.price.iloc[:, 1].plot(ax = ax)
        plt.legend(bbox_to_anchor = (1,-.25), fancybox=True, ncol=4)
        plt.show()

class LogReturns:
    def __init__(self, prices):
        self.prices = prices

    def log_returns(self):
        log_rets = np.log(1 + self.prices.pct_change().dropna())

        return log_rets


ticker = ['AAPL', '^GSPC']
start = dt.datetime(year = 2021, month = 11, day = 1)
end = dt.datetime(year = 2022, month = 11, day = 1)
r2 = GetData(ticker, start, end)
df = r2.price_collection()
r3 = LogReturns(df)
r3.log_returns()

r4 = EquityCurve(df)
r4.plot_equity_curve()


