import numpy as np
from typing import Union
from jesse.helpers import same_length

def ad(candles: np.ndarray, sequential: bool = False) -> Union[float, np.ndarray]:
    high = candles[:, 3]
    low = candles[:, 4]
    close = candles[:, 2]
    volume = candles[:, 5]

    hl_diff = high - low
    hl_diff = np.where(hl_diff == 0, np.nan, hl_diff)  # prevent division by zero

    money_flow_multiplier = ((close - low) - (high - close)) / hl_diff
    money_flow_volume = money_flow_multiplier * volume

    ad_line = np.nancumsum(money_flow_volume)

    if sequential:
        return same_length(candles, ad_line)
    return ad_line[-1]
