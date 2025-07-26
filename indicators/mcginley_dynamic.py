import numpy as np
from jesse.indicators.mcginley_dynamic import mcginley_dynamic as jesse_mcginley

def calculate_mcginley(candles: np.ndarray, period: int, k: float, source_type: str, sequential: bool):
    result = jesse_mcginley(
        candles=candles,
        period=period,
        k=k,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
