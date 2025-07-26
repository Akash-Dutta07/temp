import numpy as np
from jesse.indicators.vpwma import vpwma as jesse_vpwma
from jesse.helpers import get_candle_source
from typing import Union

def calculate_vpwma(candles: np.ndarray, period: int, power: float, source_type: str, sequential: bool) -> list:
    source = get_candle_source(candles, source_type)
    result = jesse_vpwma(source, period=period, power=power, sequential=True)

    return [None if np.isnan(x) else float(x) for x in result]
