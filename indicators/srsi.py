import numpy as np
from jesse.indicators.srsi import srsi as jesse_srsi

def calculate_srsi(candles: np.ndarray, period: int = 14, source_type: str = "close"):
    return jesse_srsi(
        candles,
        period=period,
        source_type=source_type,
        sequential=True
    )
