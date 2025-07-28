from jesse.indicators.kst import kst
from jesse.helpers import get_candle_source
import numpy as np

def calculate_kst(candles: np.ndarray, sma_period1: int, sma_period2: int, sma_period3: int, sma_period4: int,
                  roc_period1: int, roc_period2: int, roc_period3: int, roc_period4: int,
                  signal_period: int, source_type: str) -> dict:
    kst_line, kst_signal = kst(
        candles,
        sma_period1=sma_period1,
        sma_period2=sma_period2,
        sma_period3=sma_period3,
        sma_period4=sma_period4,
        roc_period1=roc_period1,
        roc_period2=roc_period2,
        roc_period3=roc_period3,
        roc_period4=roc_period4,
        signal_period=signal_period,
        source_type=source_type,
        sequential=True
    )
    
    return {
        "kst_line": np.where(np.isnan(kst_line), None, kst_line).tolist(),
        "kst_signal": np.where(np.isnan(kst_signal), None, kst_signal).tolist()
    }
