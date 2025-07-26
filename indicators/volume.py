import numpy as np
from jesse.indicators.volume import volume as jesse_volume
from typing import Union

def calculate_volume(candles: np.ndarray, period: int, sequential: bool) -> Union[dict, list]:
    vol, ma = jesse_volume(candles, period=period, sequential=sequential)

    if sequential:
        return {
            "volume": [None if np.isnan(x) else float(x) for x in vol],
            "ma": [None if np.isnan(x) else float(x) for x in ma]
        }
    return {
        "volume": float(vol),
        "ma": float(ma)
    }
