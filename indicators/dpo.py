import numpy as np
from jesse.indicators.dpo import dpo as jesse_dpo

def calculate_dpo(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_dpo(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 
 
