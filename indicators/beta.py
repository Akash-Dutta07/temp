from jesse.indicators.beta import beta
import numpy as np

def calculate_beta(candles, benchmark_candles, period: int, sequential: bool):
    values = beta(
        candles=candles,
        benchmark_candles=benchmark_candles,
        period=period,
        sequential=sequential
    )

    return {
        "beta": np.where(np.isnan(values), None, values).tolist()
    }
