from jesse.indicators.alma import alma
import numpy as np

def calculate_alma(candles, period: int, sigma: float, distribution_offset: float, source_type: str):
    values = alma(
        candles,
        period=period,
        sigma=sigma,
        distribution_offset=distribution_offset,
        source_type=source_type,
        sequential=True
    )

    return np.where(np.isnan(values), None, values).tolist()
    
