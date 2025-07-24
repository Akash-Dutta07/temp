import numpy as np
from typing import Union
from collections import namedtuple
from jesse.helpers import same_length

CKSP = namedtuple('CKSP', ['long', 'short'])

def cksp(
    candles: np.ndarray,
    p: int = 10,
    x: float = 1.0,
    q: int = 9,
    sequential: bool = False
) -> Union[CKSP, CKSP]:
    high = candles[:, 3]
    low = candles[:, 4]

    tr = np.maximum(high[1:], candles[:-1, 2]) - np.minimum(low[1:], candles[:-1, 2])
    tr = np.insert(tr, 0, tr[0])  # pad to match original length

    atr = np.full(len(tr), np.nan)
    for i in range(p - 1, len(tr)):
        atr[i] = np.mean(tr[i - p + 1 : i + 1])

    long_stop = np.full(len(tr), np.nan)
    short_stop = np.full(len(tr), np.nan)

    for i in range(p - 1, len(tr)):
        long_stop[i] = np.max(high[i - p + 1 : i + 1]) - x * atr[i]
        short_stop[i] = np.min(low[i - p + 1 : i + 1]) + x * atr[i]

    final_long = np.full(len(tr), np.nan)
    final_short = np.full(len(tr), np.nan)

    for i in range(q - 1, len(tr)):
        final_long[i] = np.max(long_stop[i - q + 1 : i + 1])
        final_short[i] = np.min(short_stop[i - q + 1 : i + 1])

    if sequential:
        return CKSP(
            long=same_length(candles, final_long),
            short=same_length(candles, final_short)
        )

    return CKSP(
        long=final_long[-1],
        short=final_short[-1]
    )
