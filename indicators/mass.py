import numpy as np
from jesse.indicators.mass import mass as jesse_mass

def calculate_mass(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_mass(
        candles=candles,
        period=period,
        sequential=sequential
    )
    if sequential:
        # Convert np.ndarray to list and replace NaN with None
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
