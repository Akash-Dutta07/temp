import numpy as np
from jesse.indicators.macd import macd as jesse_macd

def calculate_macd(candles: np.ndarray, fast_period: int, slow_period: int, signal_period: int,
                   source_type: str, sequential: bool):
    macd_line, signal_line, hist = jesse_macd(
        candles=candles,
        fast_period=fast_period,
        slow_period=slow_period,
        signal_period=signal_period,
        source_type=source_type,
        sequential=sequential
    )
    if sequential:
        return {
            "macd": macd_line.tolist(),
            "signal": signal_line.tolist(),
            "histogram": hist.tolist()
        }
    else:
        return {
            "macd": float(macd_line),
            "signal": float(signal_line),
            "histogram": float(hist)
        }
