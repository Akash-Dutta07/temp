import numpy as np
from jesse.helpers import get_candle_source
from typing import Union
from scipy.stats import linregress

def tsf(candles: np.ndarray, period: int = 14, source_type: str = "close", sequential: bool = False) -> Union[float, np.ndarray]:
    source = get_candle_source(candles, source_type)
    
    def _tsf(src: np.ndarray, length: int) -> np.ndarray:
        result = np.full_like(src, fill_value=np.nan)
        for i in range(length - 1, src.shape[0]):
            y = src[i - length + 1:i + 1]
            x = np.arange(length)
            slope, intercept, *_ = linregress(x, y)
            result[i] = intercept + slope * (length - 1)
        return result

    res = _tsf(source, period)
    return res if sequential else res[-1]
