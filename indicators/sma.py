from jesse.indicators import sma
import numpy as np

def calculate_sma(candles: np.ndarray, period: int) -> np.ndarray:
    return sma(candles, period=period, sequential=True) # This looks correct for getting array output