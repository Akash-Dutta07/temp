import numpy as np
from jesse.indicators.roc import roc as jesse_roc

def calculate_roc(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_roc(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
