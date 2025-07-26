import numpy as np
from jesse.indicators.wma import wma as jesse_wma

def calculate_wma(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_wma(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
