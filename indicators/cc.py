import numpy as np
from jesse.indicators.cc import cc as jesse_cc

def calculate_cc(
    candles: np.ndarray,
    wma_period: int,
    roc_short_period: int,
    roc_long_period: int,
    source_type: str,
    sequential: bool
) -> np.ndarray:
    
    result = jesse_cc(
        candles,
        wma_period=wma_period,
        roc_short_period=roc_short_period,
        roc_long_period=roc_long_period,
        source_type=source_type,
        sequential=sequential
    )
    
    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)















    





