import numpy as np
from jesse.indicators.cksp import cksp as jesse_cksp

def calculate_cksp(candles: np.ndarray, p: int, x: float, q: int, sequential: bool):
    long, short = jesse_cksp(
        candles=candles,
        p= p, 
        x= x, 
        q= q,
        sequential=sequential
    )

    if sequential:
        return {
            "long": [None if np.isnan(x) else float(x) for x in long],
            "short": [None if np.isnan(x) else float(x) for x in short]
        }
    else:
        return {
            "long": float(long),
            "short": float(short)
        }
   

 