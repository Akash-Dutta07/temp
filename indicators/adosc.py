import numpy as np
from jesse.indicators.adosc import adosc as jesse_adosc

def calculate_adosc(candles: np.ndarray, fast_period: int, slow_period: int,
                   sequential: bool):
    result = jesse_adosc(
        candles=candles,
        fast_period=fast_period,
        slow_period=slow_period,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)


