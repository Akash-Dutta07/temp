import numpy as np
from jesse.indicators.obv import obv

def calculate_obv(candles: np.ndarray) -> dict:
    obv_values = obv(candles, sequential=True)
    clean_obv = obv_values[~np.isnan(obv_values)]

    return {
        "indicator": "obv",
        "values": clean_obv.tolist()
    }
