import numpy as np
from jesse.indicators.willr import willr as jesse_willr

def calculate_williams_r(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_willr(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
