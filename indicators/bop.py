import numpy as np
from jesse.indicators import bop
from jesse.helpers import slice_candles

def calculate_bop(candles: np.ndarray, sequential: bool = True) -> list:
    sliced = slice_candles(candles, 100)
    result = bop(sliced, sequential=sequential)

    if sequential:
        return [round(float(v), 6) if not np.isnan(v) else None for v in result]
    else:
        return None if np.isnan(result) else round(float(result), 6)
