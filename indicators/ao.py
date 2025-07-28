import numpy as np
from jesse.indicators import ao
from jesse.helpers import slice_candles

def calculate_ao(candles: np.ndarray, sequential: bool = True) -> dict:
    sliced = slice_candles(candles, 100)
    result = ao(sliced, sequential=sequential)

    if sequential:
        osc = [round(float(v), 6) if not np.isnan(v) else None for v in result.osc]
        change = [round(float(v), 6) if not np.isnan(v) else None for v in result.change]
    else:
        osc = None if np.isnan(result.osc) else round(float(result.osc), 6)
        change = None if np.isnan(result.change) else round(float(result.change), 6)

    return {
        "osc": osc,
        "change": change
    }
