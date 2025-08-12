from jesse.indicators.pvi import pvi
import numpy as np

def calculate_pvi(candles: np.ndarray, source_type: str, sequential: bool):
    values = pvi(
        candles=candles,
        source_type=source_type,
        sequential=sequential
    )

    return np.where(np.isnan(values), None, values).tolist()
    
