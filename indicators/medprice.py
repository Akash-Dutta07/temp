import numpy as np
from jesse.indicators.medprice import medprice as jesse_medprice

def calculate_medprice(candles: np.ndarray, sequential: bool):
    result = jesse_medprice(
        candles=candles,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
