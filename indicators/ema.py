import numpy as np
from jesse.indicators.ema import ema as jesse_ema



def calculate_ema(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_ema(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)


  