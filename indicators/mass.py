import numpy as np
from jesse.indicators.mass import mass as jesse_mass

def calculate_mass(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_mass(
        candles=candles,
        period=period,
        sequential=sequential
    )
    if sequential:
        return result.tolist()
    return float(result)
