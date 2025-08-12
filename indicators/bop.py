import numpy as np
from jesse.indicators.bop import bop as jesse_bop

def calculate_bop(candles: np.ndarray, sequential: bool) -> list:
    result = jesse_bop(
        candles=candles,
        sequential=sequential
    )
    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 

  