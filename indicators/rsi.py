import numpy as np
from jesse.indicators.rsi import rsi as jesse_rsi

def calculate_rsi(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_rsi(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
