import numpy as np
from jesse.indicators.efi import efi as jesse_efi

def calculate_efi(candles: np.ndarray, period: int, source_type: str, sequential: bool):
    result = jesse_efi(
        candles=candles,
        period=period,
        source_type=source_type,
        sequential=sequential
    )

    if sequential:
        return [None if np.isnan(x) else float(x) for x in result]
    else:
        return float(result)


 