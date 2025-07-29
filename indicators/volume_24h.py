import numpy as np
from typing import Union
from jesse.helpers import slice_candles, same_length

def calculate_volume_24h(
    candles: np.ndarray,
    candles_per_day: int = 24,
    ma_period: int = None,
    sequential: bool = True
) -> Union[float, dict]:
    """
    24-Hour Volume with optional Moving Average

    :param candles: np.ndarray
    :param candles_per_day: int - number of candles representing 24 hours
    :param ma_period: int or None - MA of 24h volume
    :param sequential: bool - return array or single value
    :return: dict containing 24h volume and optional MA
    """

    candles = slice_candles(candles, sequential)
    volume = candles[:, 5]

    vol_24h = np.full_like(volume, np.nan)
    for i in range(candles_per_day - 1, len(volume)):
        vol_24h[i] = np.sum(volume[i - candles_per_day + 1:i + 1])

    ma = None
    if ma_period is not None:
        ma = np.full_like(vol_24h, np.nan)
        for i in range(ma_period - 1, len(vol_24h)):
            if not np.isnan(vol_24h[i - ma_period + 1:i + 1]).any():
                ma[i] = np.mean(vol_24h[i - ma_period + 1:i + 1])
        ma = same_length(candles, ma)

    # Helper to convert np.nan to None
    def safe_list(arr: np.ndarray) -> list:
        return [None if np.isnan(x) else float(x) for x in arr]

    if sequential:
        return {
            "volume_24h": safe_list(vol_24h),
            "volume_24h_ma": safe_list(ma) if ma is not None else None
        }
    else:
        return {
            "volume_24h": None if np.isnan(vol_24h[-1]) else float(vol_24h[-1]),
            "volume_24h_ma": None if ma is None or np.isnan(ma[-1]) else float(ma[-1])
        }
