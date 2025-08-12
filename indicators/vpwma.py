import numpy as np
from jesse.indicators.vpwma import vpwma as jesse_vpwma

def calculate_vpwma(candles: np.ndarray, period: int, power: float, source_type: str, sequential: bool):
    result = jesse_vpwma(
        candles=candles,
        period=period,
        power=power,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 