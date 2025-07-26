import numpy as np
from jesse.indicators import tsi as jesse_tsi

def calculate_tsi(candles: np.ndarray, long_period: int, short_period: int, source_type: str, sequential: bool):
    result = jesse_tsi(
        candles=candles,
        long_period=long_period,
        short_period=short_period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
