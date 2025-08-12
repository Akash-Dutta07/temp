import numpy as np
from jesse.indicators.trix import trix as jesse_trix

def calculate_trix(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_trix(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 