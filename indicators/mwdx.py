from jesse.indicators.mwdx import mwdx
import numpy as np

def calculate_mwdx(candles: np.ndarray, factor: float, source_type: str, sequential: bool):
    values = mwdx(
        candles=candles,
        factor=factor,
        source_type=source_type,
        sequential=sequential
    )

    return  np.where(np.isnan(values), None, values).tolist()
    
