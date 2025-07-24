import numpy as np
from typing import Union
from jesse.helpers import same_length

def bop(candles: np.ndarray, sequential: bool = False) -> Union[float, np.ndarray]:
    open_ = candles[:, 1]
    high = candles[:, 3]
    low = candles[:, 4]
    close = candles[:, 2]

    range_ = high - low
    range_ = np.where(range_ == 0, np.nan, range_)  # Avoid division by zero

    result = (close - open_) / range_

    if sequential:
        return same_length(candles, result)

    return result[-1]
