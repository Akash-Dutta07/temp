from jesse.indicators.linearreg import linearreg
import numpy as np

def calculate_linearreg(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    values = linearreg(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    return  np.where(np.isnan(values), None, values).tolist()
    
