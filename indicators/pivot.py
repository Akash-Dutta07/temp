import numpy as np
from jesse.indicators.pivot import pivot as jesse_pivot

def calculate_pivot(candles: np.ndarray, mode: int, sequential: bool):
    pivots = jesse_pivot(candles, mode=mode, sequential=sequential)

    if sequential:
        return {
            "r4": [None if np.isnan(x) else float(x) for x in pivots.r4],
            "r3": [None if np.isnan(x) else float(x) for x in pivots.r3],
            "r2": [None if np.isnan(x) else float(x) for x in pivots.r2],
            "r1": [None if np.isnan(x) else float(x) for x in pivots.r1],
            "pp": [None if np.isnan(x) else float(x) for x in pivots.pp],
            "s1": [None if np.isnan(x) else float(x) for x in pivots.s1],
            "s2": [None if np.isnan(x) else float(x) for x in pivots.s2],
            "s3": [None if np.isnan(x) else float(x) for x in pivots.s3],
            "s4": [None if np.isnan(x) else float(x) for x in pivots.s4],
        }
    else:
        return {
            "r4": float(pivots.r4),
            "r3": float(pivots.r3),
            "r2": float(pivots.r2),
            "r1": float(pivots.r1),
            "pp": float(pivots.pp),
            "s1": float(pivots.s1),
            "s2": float(pivots.s2),
            "s3": float(pivots.s3),
            "s4": float(pivots.s4),
        }
