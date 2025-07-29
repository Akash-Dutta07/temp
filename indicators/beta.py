from jesse.indicators.beta import beta
import numpy as np

def calculate_beta(main_candles, benchmark_candles, period: int):
    values = beta(
        main_candles,
        benchmark_candles,
        period=period,
        sequential=True
    )

    return {
        "beta": np.where(np.isnan(values), None, values).tolist()
    }
