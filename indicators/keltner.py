import numpy as np
from jesse.indicators.keltner import keltner as jesse_keltner

def calculate_keltner(candles: np.ndarray, period: int = 20, multiplier: float = 2, matype: int = 1, source_type: str = "close", sequential: bool = False):
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
            "upperband": [round(float(v), 6) if not np.isnan(v) else None for v in kc.upperband],
            "middleband": [round(float(v), 6) if not np.isnan(v) else None for v in kc.middleband],
            "lowerband": [round(float(v), 6) if not np.isnan(v) else None for v in kc.lowerband]
        }
    else:
        return {
            "upperband": round(float(kc.upperband), 6),
            "middleband": round(float(kc.middleband), 6),
            "lowerband": round(float(kc.lowerband), 6)
        }
