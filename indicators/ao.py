import numpy as np
from collections import namedtuple
from typing import Union
from jesse.helpers import same_length

AO = namedtuple('AO', ['osc', 'change'])

def ao(candles: np.ndarray, sequential: bool = False) -> Union[AO, AO]:
    median_price = (candles[:, 3] + candles[:, 4]) / 2  # (high + low) / 2

    sma_5 = np.convolve(median_price, np.ones(5)/5, mode='valid')
    sma_34 = np.convolve(median_price, np.ones(34)/34, mode='valid')

    min_len = min(len(sma_5), len(sma_34))
    osc = sma_5[-min_len:] - sma_34[-min_len:]

    # Align to original length
    full_osc = np.full(len(candles), np.nan)
    full_osc[-len(osc):] = osc

    if sequential:
        return AO(
            osc=same_length(candles, full_osc),
            change=np.append([np.nan], np.diff(full_osc))
        )
    return AO(
        osc=full_osc[-1],
        change=full_osc[-1] - full_osc[-2] if not np.isnan(full_osc[-2]) else np.nan
    )
