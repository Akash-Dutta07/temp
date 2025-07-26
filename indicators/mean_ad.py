import numpy as np
from jesse.indicators.mean_ad import mean_ad as jesse_mean_ad

def calculate_mean_ad(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_mean_ad(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
