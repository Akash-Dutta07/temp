import numpy as np
from jesse.indicators import wt

def calculate_wt(
    candles: np.ndarray,
    wtchannellen: int,
    wtaveragelen: int,
    wtmalen: int,
    oblevel: int,
    oslevel: int,
    source_type: str,
    sequential: bool
):
    result = wt(
        candles=candles,
        wtchannellen=wtchannellen,
        wtaveragelen=wtaveragelen,
        wtmalen=wtmalen,
        oblevel=oblevel,   
        oslevel=oslevel,
        source_type=source_type,
        sequential=sequential
    )

    # Convert np.nan to None and cast to float
    def safe_float_list(arr):
        return [None if np.isnan(v) else float(v) for v in arr]

    if sequential:
        return {
            "wt1": safe_float_list(result.wt1),
            "wt2": safe_float_list(result.wt2),
            "wtCrossUp": safe_float_list(result.wtCrossUp),
            "wtCrossDown": safe_float_list(result.wtCrossDown),
            "wtOversold": safe_float_list(result.wtOversold),
            "wtOverbought": safe_float_list(result.wtOverbought),
            "wtVwap": safe_float_list(result.wtVwap),
        }
    else:
        return {
            "wt1": float(result.wt1),
            "wt2": float(result.wt2),
            "wtCrossUp": float(result.wtCrossUp),
            "wtCrossDown": float(result.wtCrossDown),
            "wtOversold": float(result.wtOversold),
            "wtOverbought": float(result.wtOverbought),
            "wtVwap": float(result.wtVwap)
        }