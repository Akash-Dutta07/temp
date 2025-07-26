import numpy as np
from typing import Union
from jesse.indicators.ttm_trend import ttm_trend as jesse_ttm_trend
from jesse.helpers import get_candle_source

def calculate_ttm_trend(candles: np.ndarray, period: int, source_type: str, sequential: bool) -> Union[bool, np.ndarray]:
    source = get_candle_source(candles, source_type)
    result = jesse_ttm_trend(candles, period=period, source_type=source_type, sequential=sequential)
    
    if sequential:
        return [None if np.isnan(x) else bool(x) for x in result]
    else:
        return bool(result)
