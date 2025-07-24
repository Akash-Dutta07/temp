import numpy as np
from jesse.indicators.adx import adx

def calculate_adx(candles: np.ndarray, period: int) -> dict:
    adx_values = adx(candles, period=period, sequential=True)
    clean_adx = adx_values[~np.isnan(adx_values)]

    return {
        "indicator": "adx",
        "values": clean_adx.tolist()
    }
