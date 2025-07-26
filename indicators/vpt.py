import numpy as np
from jesse.indicators.vpt import vpt as jesse_vpt

def calculate_vpt(candles: np.ndarray, source_type: str, sequential: bool):
    result = jesse_vpt(
        candles=candles,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
