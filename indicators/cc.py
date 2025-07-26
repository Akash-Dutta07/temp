import numpy as np
from jesse.indicators import cc

def calculate_cc(
    candles: np.ndarray,
    wma_period: int = 10,
    roc_short_period: int = 11,
    roc_long_period: int = 14,
    source_type: str = "close"
) -> np.ndarray:
    return cc(
        candles,
        wma_period=wma_period,
        roc_short_period=roc_short_period,
        roc_long_period=roc_long_period,
        source_type=source_type,
        sequential=True
    )
