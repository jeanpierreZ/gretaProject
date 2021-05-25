import backtrader as bt


class MyEMA(bt.indicators.ExponentialMovingAverage):
    plotlines = dict(ema=dict(color='black'))
