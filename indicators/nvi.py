from jesse.indicators.nvi import nvi
import numpy as np

def calculate_nvi(candles: np.ndarray, source_type: str, sequential: bool):
    values = nvi(
        candles=candles,
        source_type=source_type,
        sequential=sequential
    )

    return np.where(np.isnan(values), None, values).tolist()
    
