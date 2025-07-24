import numpy as np
from typing import Union
from jesse.helpers import same_length

def chop(
    candles: np.ndarray,
    period: int = 14,
    scalar: float = 100,
    drift: int = 1,
    sequential: bool = False
) -> Union[float, np.ndarray]:
    high = candles[:, 3]
    low = candles[:, 4]
    close = candles[:, 2]

    tr = np.maximum(high[1:], close[:-1]) - np.minimum(low[1:], close[:-1])
    tr = np.insert(tr, 0, np.nan)  # align length

    atr_sum = np.full(len(candles), np.nan)
    high_max = np.full(len(candles), np.nan)
    low_min = np.full(len(candles), np.nan)

    for i in range(period - 1, len(candles)):
        atr_sum[i] = np.sum(tr[i - period + 1 : i + 1])
        high_max[i] = np.max(high[i - period + 1 : i + 1])
        low_min[i] = np.min(low[i - period + 1 : i + 1])

    range_ = high_max - low_min
    with np.errstate(divide='ignore', invalid='ignore'):
        chop_val = scalar * np.log10(atr_sum / range_) / np.log10(period)

    if sequential:
        return same_length(candles, chop_val)

    return chop_val[-1]
