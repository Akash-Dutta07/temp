import numpy as np
from jesse.indicators import cfo

def calculate_cfo(candles: np.ndarray, period: int = 14, scalar: float = 100, source_type: str = "close"):
    return cfo(candles, period=period, scalar=scalar, source_type=source_type, sequential=True)
