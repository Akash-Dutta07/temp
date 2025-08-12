import numpy as np
from jesse.indicators.obv import obv as jesse_obv

def calculate_obv(candles: np.ndarray, sequential: bool):
    result = jesse_obv(
        candles=candles,
        sequential=sequential
    )
    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 
 
