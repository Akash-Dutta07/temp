from jesse.indicators import rsi
import numpy as np

def calculate_rsi(candles: np.ndarray, period: int) -> np.ndarray:
    return rsi(candles, period=period, sequential=True) 