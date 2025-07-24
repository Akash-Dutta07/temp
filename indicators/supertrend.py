import numpy as np
from jesse.indicators.supertrend import supertrend

def calculate_supertrend(candles: np.ndarray, period: int = 10) -> dict:
    trend, changed = supertrend(candles, period=period, factor=3, sequential=True)

    # Remove NaNs from the trend and changed arrays
    clean_trend = trend[~np.isnan(trend)]
    clean_changed = changed[~np.isnan(changed)]

    return {
        "indicator": "supertrend",
        "trend": clean_trend.tolist(),
        "changed": clean_changed.tolist()
    }
