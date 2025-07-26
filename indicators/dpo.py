import numpy as np
from jesse.indicators import dpo
from jesse.helpers import get_candle_source, slice_candles

def calculate_dpo(candles: np.ndarray, period: int = 5, source_type: str = "close") -> np.ndarray:
    source = get_candle_source(candles, source_type)
    sliced = slice_candles(candles, period + 100)
    values = dpo(sliced, period, source_type=source_type, sequential=True)
    return [round(float(v), 6) if not np.isnan(v) else None for v in values]
