from jesse.indicators.avgprice import avgprice
import numpy as np

def calculate_avgprice(candles):
    values = avgprice(
        candles,
        sequential=True
    )

    return {
        "avgprice": np.where(np.isnan(values), None, values).tolist()
    }
