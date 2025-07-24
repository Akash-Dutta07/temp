import numpy as np
from jesse.indicators.roc import roc

def calculate_roc(candles: np.ndarray, period: int) -> dict:
    roc_values = roc(candles, period=period, sequential=True)
    clean_roc = roc_values[~np.isnan(roc_values)]

    return {
        "indicator": "roc",
        "values": clean_roc.tolist()
    }
