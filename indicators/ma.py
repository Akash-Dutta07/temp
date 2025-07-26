import numpy as np
from jesse.indicators.ma import ma as jesse_ma

def calculate_ma(candles: np.ndarray, period: int, matype: int, source_type: str, sequential: bool):
    result = jesse_ma(
        candles=candles,
        period=period,
        matype=matype,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
