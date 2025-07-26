import numpy as np
from typing import Union
from jesse.helpers import get_candle_source
from jesse.indicators.tema import tema as jesse_tema

def calculate_tema(
    candles: np.ndarray,
    period: int,
    source_type: str,
    sequential: bool
) -> Union[float, np.ndarray]:
    source = get_candle_source(candles, source_type)
    result = jesse_tema(source, period=period, sequential=sequential)

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
