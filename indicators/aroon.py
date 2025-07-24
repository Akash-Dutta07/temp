import numpy as np
from typing import Union
from collections import namedtuple
from jesse.helpers import same_length

AROON = namedtuple('AROON', ['down', 'up'])

def aroon(candles: np.ndarray, period: int = 14, sequential: bool = False) -> Union[AROON, AROON]:
    highs = candles[:, 3]
    lows = candles[:, 4]

    def calc_aroon(data: np.ndarray, find_high: bool) -> np.ndarray:
        result = np.full(len(data), np.nan)
        for i in range(period, len(data)):
            window = data[i - period + 1:i + 1]
            idx = np.argmax(window) if find_high else np.argmin(window)
            days_since = period - idx - 1
            result[i] = ((period - days_since) / period) * 100
        return result

    aroon_up = calc_aroon(highs, find_high=True)
    aroon_down = calc_aroon(lows, find_high=False)

    if sequential:
        return AROON(
            down=same_length(candles, aroon_down),
            up=same_length(candles, aroon_up)
        )

    return AROON(down=aroon_down[-1], up=aroon_up[-1])
