from fastapi import FastAPI, HTTPException
from models.indicator_request import IndicatorRequest
from services.binance_service import fetch_candles
from indicators.sma import calculate_sma
from indicators.rsi import calculate_rsi
from indicators.ema import calculate_ema
from indicators.macd import calculate_macd
import numpy as np

app = FastAPI()


@app.post("/sma")
async def get_sma(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        sma_values = calculate_sma(candles, data.period)

        # remove NaN if any (precaution)
        sma_clean = np.array(sma_values)
        sma_clean = sma_clean[~np.isnan(sma_clean)]

        return {
            "indicator": "sma",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
            "values": sma_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rsi")
async def get_rsi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        print("✅ Raw candles shape:", candles.shape)
        print("✅ First row:", candles[0])

        rsi_values = calculate_rsi(candles, data.period)

        # remove NaNs for JSON response
        rsi_clean = np.array(rsi_values)
        rsi_clean = rsi_clean[~np.isnan(rsi_clean)]

        return {
            "indicator": "rsi",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
            "values": rsi_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ema")
async def get_ema(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        ema_values = calculate_ema(candles, data.period)
        ema_clean = ema_values[~np.isnan(ema_values)]

        return {
            "indicator": "ema",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
            "values": ema_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/macd")
async def get_macd(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_macd(candles)

        # Clean NaNs from each MACD component
        macd_clean = result["macd"][~np.isnan(result["macd"])]
        signal_clean = result["signal"][~np.isnan(result["signal"])]
        hist_clean = result["hist"][~np.isnan(result["hist"])]

        return {
            "indicator": "macd",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "fast_period": 12,
            "slow_period": 26,
            "signal_period": 9,
            "macd": macd_clean.tolist(),
            "signal": signal_clean.tolist(),
            "histogram": hist_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
