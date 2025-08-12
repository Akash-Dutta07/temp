import numpy as np
from jesse.indicators.tsf import tsf as jesse_tsf

def calculate_tsf(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_tsf(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)