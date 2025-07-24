import numpy as np
from jesse.indicators.cci import cci

def calculate_cci(candles: np.ndarray, period: int) -> dict:
    cci_values = cci(candles, period=period, sequential=True)
    clean_cci = cci_values[~np.isnan(cci_values)]

    return {
        "indicator": "cci",
        "values": clean_cci.tolist()
    }
