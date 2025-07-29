import numpy as np
from jesse.indicators.wt import wt as jesse_wt

def calculate_wt(
    candles: np.ndarray,
    wtchannellen: int = 9,
    wtaveragelen: int = 12,
    wtmalen: int = 3,
    oblevel: int = 53,
    oslevel: int = -53,
    source_type: str = "hlc3"
):
    return jesse_wt(
        candles,
        wtchannellen=wtchannellen,
        wtaveragelen=wtaveragelen,
        wtmalen=wtmalen,
        oblevel=oblevel,
        oslevel=oslevel,
        source_type=source_type,
        sequential=True
    )
