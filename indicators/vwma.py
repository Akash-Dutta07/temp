import numpy as np
from jesse.indicators.vwma import vwma as jesse_vwma
from jesse.helpers import get_candle_source
from typing import Union

def calculate_vwma(candles: np.ndarray, period: int, source_type: str, sequential: bool) -> list:
    source = get_candle_source(candles, source_type)
    result = jesse_vwma(candles, period=period, source_type=source_type, sequential=True)

    return [None if np.isnan(x) else float(x) for x in result]
