import numpy as np
from jesse.indicators.emv import emv as jesse_emv

def calculate_emv(candles: np.ndarray, length: int, div: int, sequential: bool):
    result = jesse_emv(
        candles=candles,
        length=length, 
        div=div,
        sequential=sequential
    )

    if sequential:
        # Convert np.ndarray to list and replace NaN with None
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)


  
  
  
