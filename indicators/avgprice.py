from jesse.indicators.avgprice import avgprice
import numpy as np

def calculate_avgprice(candles: np.ndarray, sequential: bool):
    values = avgprice(
        candles=candles,
        sequential=sequential
    )

    return np.where(np.isnan(values), None, values).tolist()
