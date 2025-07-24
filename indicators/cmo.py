import numpy as np
from jesse.indicators.cmo import cmo

def calculate_cmo(candles: np.ndarray, period: int) -> dict:
    cmo_values = cmo(candles, period=period, sequential=True)
    clean_cmo = cmo_values[~np.isnan(cmo_values)]

    return {
        "indicator": "cmo",
        "values": clean_cmo.tolist()
    }
