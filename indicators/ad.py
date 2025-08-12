import numpy as np
from jesse.indicators.ad import ad as jesse_ad

def calculate_ad(candles: np.ndarray, sequential: bool):
    result = jesse_ad(
        candles=candles,
        sequential=sequential
    )
    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)