import numpy as np
from jesse.indicators.vwap import vwap as jesse_vwap

def calculate_vwap(candles: np.ndarray, source_type: str, anchor: str, sequential: bool):
    result = jesse_vwap(
        candles=candles,
        source_type=source_type,
        anchor=anchor,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
