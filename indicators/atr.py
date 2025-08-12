import numpy as np
from jesse.indicators.atr import atr as jesse_atr

def calculate_atr(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_atr(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
