from jesse.indicators.mwdx import mwdx
import numpy as np

def calculate_mwdx(candles, factor: float, source_type: str):
    values = mwdx(
        candles,
        factor=factor,
        source_type=source_type,
        sequential=True
    )

    return  np.where(np.isnan(values), None, values).tolist()
    
