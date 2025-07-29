import numpy as np
from jesse.indicators.vi import vi as jesse_vi
from jesse.helpers import same_length
from typing import Union

def replace_nan_with_none(arr):
    return [None if np.isnan(x) else float(x) for x in arr]

def calculate_vi(candles: np.ndarray, period: int = 14, sequential: bool = False) -> dict:
    vi_values = jesse_vi(candles, period=period, sequential=sequential)
    plus, minus = vi_values.plus, vi_values.minus

    if sequential:
        plus = same_length(candles, plus)
        minus = same_length(candles, minus)
        return {
            "plus": replace_nan_with_none(plus),
            "minus": replace_nan_with_none(minus)
        }
    else:
        return {
            "plus": None if np.isnan(plus) else float(plus),
            "minus": None if np.isnan(minus) else float(minus)
        }
