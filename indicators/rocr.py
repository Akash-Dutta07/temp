import numpy as np
from jesse.indicators.rocr import rocr as jesse_rocr

def calculate_rocr(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_rocr(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
