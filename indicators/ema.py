import jesse.indicators as ta
import numpy as np

def calculate_ema(candles, period: int):
    ema_values = ta.ema(candles, period=period, sequential=True)
    return np.array(ema_values)
