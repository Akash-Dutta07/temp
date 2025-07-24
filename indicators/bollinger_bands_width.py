import numpy as np
from typing import Union
from jesse.helpers import get_candle_source, same_length

def bollinger_bands_width(
    candles: np.ndarray,
    period: int = 20,
    mult: float = 2,
    source_type: str = "close",
    sequential: bool = False
) -> Union[float, np.ndarray]:
    source = get_candle_source(candles, source_type)

    sma = np.convolve(source, np.ones(period) / period, mode='valid')
    sma = np.concatenate([np.full(period - 1, np.nan), sma])

    std = np.full(len(source), np.nan)
    for i in range(period - 1, len(source)):
        std[i] = np.std(source[i - period + 1 : i + 1])

    upper_band = sma + mult * std
    lower_band = sma - mult * std

    width = (upper_band - lower_band) / sma

    if sequential:
        return same_length(candles, width)
    return width[-1]
