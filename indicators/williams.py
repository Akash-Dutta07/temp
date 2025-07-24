import numpy as np
from jesse.indicators.willr import willr

def calculate_williams_r(candles: np.ndarray, period: int) -> dict:
    wr_values = willr(candles, period=period, sequential=True)
    clean_wr = wr_values[~np.isnan(wr_values)]

    return {
        "indicator": "williams_r",
        "values": clean_wr.tolist()
    }
