from jesse.indicators.pvi import pvi
import numpy as np

def calculate_pvi(candles, source_type: str):
    values = pvi(
        candles,
        source_type=source_type,
        sequential=True
    )

    return np.where(np.isnan(values), None, values).tolist()
    
