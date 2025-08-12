import numpy as np
from jesse.indicators.cci import cci as jesse_cci

def calculate_cci(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_cci(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)





 
