import httpx
import numpy as np

async def fetch_candles(symbol: str, interval: str, limit: int = 100):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol.upper(),
        "interval": interval,
        "limit": limit
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        raw_data = response.json()

    # Correct order based on Jesse: [timestamp, open, close, high, low, volume]
    candles = np.array([
        [
            int(item[0]),     # timestamp
            float(item[1]),   # open
            float(item[4]),   # close
            float(item[2]),   # high
            float(item[3]),   # low
            float(item[5])    # volume
        ]
        for item in raw_data
    ])

    return candles
