import numpy as np
from jesse.indicators import cmo

def calculate_cmo(candles: np.ndarray, period: int = 14, source_type: str = "close") -> np.ndarray:
    return cmo(
        candles,
        period=period,
        source_type=source_type,
        sequential=True
    )
