import numpy as np
from jesse.indicators.kst import kst as jesse_kst


def calculate_kst(
    candles: np.ndarray,
    sma_period1: int,
    sma_period2: int,
    sma_period3: int,
    sma_period4: int,
    roc_period1: int,
    roc_period2: int,
    roc_period3: int,
    roc_period4: int,
    signal_period: int,
    source_type: str,
    sequential: bool
):
    result = jesse_kst(
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
        sequential=sequential
    )

    line, signal = result.line, result.signal

    if sequential:
        line = np.array(line)
        signal = np.array(signal)

        line = line[~np.isnan(line)]
        signal = signal[~np.isnan(signal)]

        return {
            "line": line.tolist(),
            "signal": signal.tolist()
        }
    else:
        return {
            "line": line,
            "signal": signal
        }
