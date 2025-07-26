import numpy as np
from jesse.indicators.mom import mom as jesse_mom

def calculate_mom(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_mom(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
