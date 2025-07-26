import numpy as np
from jesse.indicators import bollinger_bands

def calculate_bollinger_bands(
    candles: np.ndarray,
    period: int = 20,
    devup: float = 2,
    devdn: float = 2,
    matype: int = 0,
    devtype: int = 0,
    source_type: str = "close"
):
    result = bollinger_bands(
        candles,
        period=period,
        devup=devup,
        devdn=devdn,
        matype=matype,
        devtype=devtype,
        source_type=source_type,
        sequential=True
    )

    # Convert np.nan to None
    return {
        "upperband": [None if np.isnan(v) else v for v in result.upperband],
        "middleband": [None if np.isnan(v) else v for v in result.middleband],
        "lowerband": [None if np.isnan(v) else v for v in result.lowerband],
    }
