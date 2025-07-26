import numpy as np
from jesse.indicators.rocp import rocp as jesse_rocp

def calculate_rocp(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_rocp(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
