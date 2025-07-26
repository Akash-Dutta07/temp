import numpy as np
from jesse.indicators import dm
from jesse.helpers import slice_candles

def calculate_dm(candles: np.ndarray, period: int = 14) -> dict:
    sliced = slice_candles(candles, period + 100)
    result = dm(sliced, period, sequential=True)

    plus = [round(float(v), 6) if not np.isnan(v) else None for v in result.plus]
    minus = [round(float(v), 6) if not np.isnan(v) else None for v in result.minus]

    return {
        "plus": plus,
        "minus": minus
    }
