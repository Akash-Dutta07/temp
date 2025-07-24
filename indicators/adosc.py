import numpy as np
from typing import Union
from jesse.helpers import same_length

def adosc(
    candles: np.ndarray,
    fast_period: int = 3,
    slow_period: int = 10,
    sequential: bool = False
) -> Union[float, np.ndarray]:
    high = candles[:, 3]
    low = candles[:, 4]
    close = candles[:, 2]
    volume = candles[:, 5]

    hl_diff = high - low
    hl_diff = np.where(hl_diff == 0, np.nan, hl_diff)  # Avoid division by zero

    mfm = ((close - low) - (high - close)) / hl_diff
    mfv = mfm * volume

    # Replace NaNs with 0s for smoother EMA
    mfv = np.nan_to_num(mfv)

    def ema(data: np.ndarray, period: int) -> np.ndarray:
        alpha = 2 / (period + 1)
        result = np.zeros_like(data)
        result[0] = data[0]
        for i in range(1, len(data)):
            result[i] = alpha * data[i] + (1 - alpha) * result[i - 1]
        return result

    fast_ema = ema(mfv, fast_period)
    slow_ema = ema(mfv, slow_period)

    adosc_vals = fast_ema - slow_ema

    if sequential:
        return same_length(candles, adosc_vals)
    return adosc_vals[-1]
