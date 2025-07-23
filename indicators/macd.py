import jesse.indicators as ta
import numpy as np

def calculate_macd(candles, fast_period=12, slow_period=26, signal_period=9):
    macd_tuple = ta.macd(
        candles,
        fast_period=fast_period,
        slow_period=slow_period,
        signal_period=signal_period,
        sequential=True
    )
    # Returns tuple: (macd_line, signal_line, histogram)
    return {
        "macd": np.array(macd_tuple.macd),
        "signal": np.array(macd_tuple.signal),
        "hist": np.array(macd_tuple.hist)
    }
