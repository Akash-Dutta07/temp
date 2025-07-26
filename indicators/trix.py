import numpy as np
from jesse.indicators.trix import trix as jesse_trix
from typing import Union

def calculate_trix(
    candles: np.ndarray,
    period: int,
    source_type: str,
    sequential: bool
) -> Union[float, list]:
    result = jesse_trix(candles, period=period, source_type=source_type, sequential=sequential)

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    return None if np.isnan(result) else float(result)
