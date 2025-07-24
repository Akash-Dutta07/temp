import numpy as np
from jesse.indicators.atr import atr

def calculate_atr(candles: np.ndarray, period: int) -> dict:
    atr_values = atr(candles, period=period, sequential=True)

    clean_atr = atr_values[~np.isnan(atr_values)]

    return {
        "indicator": "atr",
        "values": clean_atr.tolist()
    }
