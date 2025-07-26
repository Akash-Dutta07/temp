import numpy as np
from jesse.indicators import di
from jesse.helpers import slice_candles

def calculate_di(candles: np.ndarray, period: int = 14) -> dict:
    sliced = slice_candles(candles, period + 100)  # for stability
    result = di(sliced, period, sequential=True)
    plus, minus = result.plus, result.minus

    plus_clean = [round(float(p), 6) if not np.isnan(p) else None for p in plus]
    minus_clean = [round(float(m), 6) if not np.isnan(m) else None for m in minus]

    return {
        "plus": plus_clean,
        "minus": minus_clean
    }
