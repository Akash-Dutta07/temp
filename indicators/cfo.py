import numpy as np
from jesse.indicators.cfo import cfo as jesse_cfo

def calculate_cfo(candles: np.ndarray, period: int, scalar: float, source_type: str, sequential: bool):
    result = jesse_cfo(
        candles,
        period=period,
        scalar=scalar,
        source_type=source_type,
        sequential=sequential
    )
    
    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)





 