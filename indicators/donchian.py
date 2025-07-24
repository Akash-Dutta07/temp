import numpy as np
from jesse.indicators.donchian import donchian

def calculate_donchian(candles: np.ndarray, period: int) -> dict:
    upper, middle, lower = donchian(candles, period=period, sequential=True)
    clean_upper = upper[~np.isnan(upper)]
    clean_middle = middle[~np.isnan(middle)]
    clean_lower = lower[~np.isnan(lower)]

    return {
        "indicator": "donchian",
        "upper_band": clean_upper.tolist(),
        "middle_band": clean_middle.tolist(),
        "lower_band": clean_lower.tolist()
    }
