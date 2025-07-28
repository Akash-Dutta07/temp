import numpy as np
from jesse.indicators.cksp import cksp as jesse_cksp

def calculate_cksp(candles: np.ndarray, p: int = 10, x: float = 1.0, q: int = 9):
    # Always sequential for your use-case
    return jesse_cksp(candles, p=p, x=x, q=q, sequential=True)
