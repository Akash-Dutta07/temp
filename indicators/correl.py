import numpy as np
from jesse.indicators.correl import correl as jesse_correl

def calculate_correl(candles: np.ndarray, period: int, sequential: bool):
    result = jesse_correl(
        candles=candles,
        period=period,
        sequential=sequential
    )

    if sequential:
        # Convert np.ndarray to list and replace NaN with None
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)


  
  
  
