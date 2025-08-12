import numpy as np
from jesse.indicators.keltner import keltner as jesse_keltner

def calculate_keltner(candles: np.ndarray, period: int, multiplier: float, matype: int, source_type: str, sequential: bool):
    kc = jesse_keltner(
        candles,
        period=period,
        multiplier=multiplier,
        matype=matype,
        source_type=source_type,
        sequential=sequential
    )
    if sequential:
        return {
            "upperband": [float(v) if not np.isnan(v) else None for v in kc.upperband],
            "middleband": [float(v) if not np.isnan(v) else None for v in kc.middleband],
            "lowerband": [float(v) if not np.isnan(v) else None for v in kc.lowerband]
        }
    else:
        return {
            "upperband": float(kc.upperband),
            "middleband": float(kc.middleband),
            "lowerband": float(kc.lowerband)
        }
