import numpy as np
from jesse.indicators import correl

def calculate_correl(
    candles: np.ndarray,
    period: int = 5
) -> np.ndarray:
    return correl(candles, period=period, sequential=True)
