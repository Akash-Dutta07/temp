from jesse.indicators.hma import hma
import numpy as np

def calculate_hma(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    values = hma(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    return np.where(np.isnan(values), None, values).tolist()
    
