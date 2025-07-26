import numpy as np
from jesse.indicators.mfi import mfi as jesse_mfi

def calculate_mfi(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_mfi(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        # Convert np.ndarray to list and replace NaN with None
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
