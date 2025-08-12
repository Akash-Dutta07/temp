import numpy as np
from jesse.indicators.ttm_squeeze import ttm_squeeze as jesse_ttm_squeeze

def calculate_ttm_squeeze(
    candles: np.ndarray,
    length_ttms: int,
    bb_mult_ttms: float,
    kc_mult_low_ttms: float
) -> bool:
    return bool(jesse_ttm_squeeze(
        candles=candles,
        length_ttms=length_ttms,
        bb_mult_ttms=bb_mult_ttms,
        kc_mult_low_ttms=kc_mult_low_ttms
    ))
