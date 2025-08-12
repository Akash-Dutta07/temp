import numpy as np
from jesse.indicators.adx import adx as jesse_adx

def calculate_adx(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_adx(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)

