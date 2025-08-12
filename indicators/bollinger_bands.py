import numpy as np
from jesse.indicators import bollinger_bands

def calculate_bollinger_bands(
    candles: np.ndarray,
    period: int,
    devup: float,
    devdn: float,
    matype: int,
    devtype: int,
    source_type: str,
    sequential: bool
):
    result = bollinger_bands(
        candles,
        period=period,
        devup=devup,
        devdn=devdn,
        matype=matype,   
        devtype=devtype,
        source_type=source_type,
        sequential=sequential
    )

    # Convert np.nan to None
    return {
        "upperband": [None if np.isnan(v) else v for v in result.upperband],
        "middleband": [None if np.isnan(v) else v for v in result.middleband],
        "lowerband": [None if np.isnan(v) else v for v in result.lowerband],
    }
