import numpy as np
from jesse.indicators.vwma import vwma as jesse_vwma

def calculate_vwma(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_vwma(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 