import numpy as np
from typing import Union
from jesse.helpers import get_candle_source
from jesse.indicators.ema import ema

def dema(candles: np.ndarray, period: int = 30, source_type: str = "close", sequential: bool = False) -> Union[float, np.ndarray]:
    
    src = get_candle_source(candles, source_type=source_type)

    ema1 = ema(candles, period=period, source_type=source_type, sequential=True)
    ema2 = ema1 if isinstance(ema1, np.ndarray) else np.array([ema1])
    ema2 = ema(ema2, period=period, source_type="close", sequential=True)

    dema_values = 2 * ema1 - ema2

    return dema_values if sequential else dema_values[-1]
