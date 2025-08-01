import numpy as np
from jesse.indicators.median_ad import median_ad as jesse_median_ad

def calculate_median_ad(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_median_ad(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
