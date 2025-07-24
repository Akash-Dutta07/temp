import numpy as np
from typing import Union
from jesse.helpers import get_candle_source, same_length

def cfo(
    candles: np.ndarray,
    period: int = 14,
    scalar: float = 100,
    source_type: str = "close",
    sequential: bool = False
) -> Union[float, np.ndarray]:
    source = get_candle_source(candles, source_type)

    forecast = np.full(len(source), np.nan)

    for i in range(period - 1, len(source)):
        y = source[i - period + 1 : i + 1]
        x = np.arange(period)

        # Linear regression coefficients (slope m, intercept b)
        m, b = np.polyfit(x, y, 1)
        predicted = m * (period - 1) + b
        forecast[i] = ((source[i] - predicted) / predicted) * scalar if predicted != 0 else np.nan

    if sequential:
        return same_length(candles, forecast)

    return forecast[-1]
