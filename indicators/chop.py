import numpy as np
from jesse.indicators.chop import chop as jesse_chop

def calculate_chop(candles: np.ndarray, period: int, scalar: float, drift: int, sequential: bool):
    result = jesse_chop(
        candles,
        period=period,
        scalar=scalar,
        drift=drift,
        sequential=sequential
    )
    
    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)







 