import numpy as np
from jesse.indicators.tema import tema as jesse_tema

def calculate_tema(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_tema(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)
 