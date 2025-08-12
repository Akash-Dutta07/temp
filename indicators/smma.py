import numpy as np
from jesse.indicators.smma import smma as jesse_smma

def calculate_smma(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_smma(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 