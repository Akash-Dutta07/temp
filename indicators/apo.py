import numpy as np
from jesse.indicators.apo import apo as jesse_apo

def calculate_apo(candles: np.ndarray, fast_period: int, slow_period: int, matype: int, source_type: str, sequential: bool):
    result = jesse_apo(
        candles,
        fast_period=fast_period,
        slow_period=slow_period,
        matype=matype,
        source_type=source_type,
        sequential=sequential
    )
    
    if sequential:
        # Replace NaN with None for JSON compatibility
        result = [None if np.isnan(x) else x for x in result]
    else:
        result = [None if np.isnan(result) else result]

    return result
