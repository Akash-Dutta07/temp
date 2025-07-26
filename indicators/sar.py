import numpy as np
from jesse.indicators.sar import sar as jesse_sar

def calculate_sar(candles: np.ndarray, acceleration: float, maximum: float, sequential: bool):
    result = jesse_sar(
        candles=candles,
        acceleration=acceleration,
        maximum=maximum,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
