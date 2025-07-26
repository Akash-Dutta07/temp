import numpy as np
from jesse.indicators import bollinger_bands_width

def calculate_bollinger_bands_width(candles: np.ndarray, period: int = 20, mult: float = 2, source_type: str = "close"):
    return bollinger_bands_width(candles, period=period, mult=mult, source_type=source_type, sequential=True)
