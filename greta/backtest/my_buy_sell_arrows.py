# Import the backtrader platform
import backtrader as bt


class MyBuySell(bt.observers.BuySell):
    """
    * `barplot` (default: `False`) Plot buy signals below the minimum and sell signals above the maximum.
    If `False` it will plot on the average price of executions during a bar
    * `bardist` (default: `0.015` 1.5%) Distance to max/min when `barplot` is `True`
    """

    params = (('barplot', True), ('bardist', 0.10))
    plotlines = dict(
        buy=dict(marker='$\u21E7$', color='lime', markersize=12.0),
        sell=dict(marker='$\u21E9$', color='red', markersize=12.0)
    )
