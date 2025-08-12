import numpy as np
from jesse.indicators.cmo import cmo as jesse_cmo

def calculate_cmo(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_cmo(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
