import numpy as np
from jesse.indicators.ttm_trend import ttm_trend as jesse_ttm_trend

def calculate_ttm_trend(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_ttm_trend(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else bool(x) for x in result]
    else:
        return bool(result)
 