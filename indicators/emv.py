import numpy as np
from jesse.indicators.emv import emv as jesse_emv

def calculate_emv(candles: np.ndarray, length: int = 14, div: int = 10000):
    result = jesse_emv(candles, length=length, div=div, sequential=True)
    return [round(float(val), 6) if not np.isnan(val) else None for val in result]
