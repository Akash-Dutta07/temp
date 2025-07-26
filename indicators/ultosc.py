import numpy as np
from jesse.indicators.ultosc import ultosc as jesse_ultosc

def calculate_ultosc(candles: np.ndarray, timeperiod1: int, timeperiod2: int, timeperiod3: int, sequential: bool):
    result = jesse_ultosc(
        candles=candles,
        timeperiod1=timeperiod1,
        timeperiod2=timeperiod2,
        timeperiod3=timeperiod3,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
