import numpy as np
from jesse.indicators.aroon import aroon
from typing import List, Tuple

def calculate_aroon(candles: np.ndarray, period: int, sequential=True) -> dict:
    down, up = aroon(candles, period=period, sequential=True)
    # Replace NaN with None for JSON serialization
    down_clean = [None if np.isnan(val) else val for val in down]
    up_clean = [None if np.isnan(val) else val for val in up]
    return {
        "aroon_down": down_clean,
        "aroon_up": up_clean
    }