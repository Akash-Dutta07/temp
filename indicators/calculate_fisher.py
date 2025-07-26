

import numpy as np
from jesse.indicators.fisher import fisher as jesse_fisher


def np_array_to_list(array: np.ndarray) -> list:
    return array.tolist()

def calculate_fisher(candles: np.ndarray, period: int):
    fisher, signal = jesse_fisher(candles, period=period, sequential=True)
    return {
        "fisher": np_array_to_list(fisher),
        "signal": np_array_to_list(signal)
    }
