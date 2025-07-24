import numpy as np
from typing import Union
from jesse.helpers import same_length

def correl(candles: np.ndarray, period: int = 5, sequential: bool = False) -> Union[float, np.ndarray]:
    high = candles[:, 3]
    low = candles[:, 4]

    result = np.full(len(high), np.nan)

    for i in range(period - 1, len(high)):
        x = high[i - period + 1 : i + 1]
        y = low[i - period + 1 : i + 1]

        if np.std(x) == 0 or np.std(y) == 0:
            result[i] = 0
        else:
            result[i] = np.corrcoef(x, y)[0, 1]

    if sequential:
        return same_length(candles, result)

    return result[-1]
