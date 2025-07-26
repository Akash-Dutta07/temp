import numpy as np
from jesse.indicators.ema import ema as jesse_ema
from jesse.helpers import get_candle_source

def calculate_ema(candles: np.ndarray, period: int = 5, source_type: str = "close", sequential: bool = False):
    source = get_candle_source(candles, source_type)
    result = jesse_ema(source, period, sequential=sequential)

    if sequential:
        return [round(float(r), 6) if not np.isnan(r) else None for r in result]
    else:
        return round(float(result), 6) if not np.isnan(result) else None
