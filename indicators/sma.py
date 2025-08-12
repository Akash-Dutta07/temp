import numpy as np
from jesse.indicators.sma import sma as jesse_sma

def calculate_sma(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_sma(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
   