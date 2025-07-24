from fastapi import FastAPI, HTTPException

from models.indicator_request import IndicatorRequest
from models.indicator_request import NoPeriodIndicatorRequest
from models.indicator_request import ADOSCRequest
from indicators.cksp import cksp
from indicators.chop import chop
from indicators.correl import correl


from services.binance_service import fetch_candles
from indicators.sma import calculate_sma
from indicators.rsi import calculate_rsi
from indicators.ema import calculate_ema
from indicators.macd import calculate_macd
from indicators.bollinger import calculate_bollinger
from indicators.atr import calculate_atr
from indicators.supertrend import calculate_supertrend
from indicators.vwap import calculate_vwap
from indicators.adx import calculate_adx
from indicators.cci import calculate_cci
from indicators.williams import calculate_williams_r
from indicators.roc import calculate_roc
from indicators.cmo import calculate_cmo
from indicators.apo import calculate_apo
from indicators.ppo import calculate_ppo
from indicators.mfi import calculate_mfi
from indicators.coppock import calculate_coppock
from indicators.donchian import calculate_donchian
from indicators.obv import calculate_obv
from indicators.efi import calculate_efi
from indicators.aroon import aroon
from indicators.ao import ao
from indicators.bop import bop
from indicators.ad import ad
from indicators.bollinger_bands_width import bollinger_bands_width
from indicators.cfo import cfo
from indicators.adosc import adosc
from models.indicator_request import CKSPRequest
from models.indicator_request import CHOPRequest
from models.indicator_request import CorrelRequest







import numpy as np
from fastapi.responses import JSONResponse
from services.binance_service import fetch_candles
from models.indicator_request import IndicatorRequest


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


@app.post("/bollinger")
async def get_bollinger(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_bollinger(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/atr")
async def get_atr(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_atr(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/supertrend")
async def get_supertrend(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_supertrend(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/vwap")
async def get_vwap(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_vwap(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/adx")
async def get_adx(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_adx(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/cci")
async def get_cci(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_cci(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/williams_r")
async def get_williams_r(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_williams_r(candles, data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})    


@app.post("/roc")
async def get_roc(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_roc(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/cmo")
async def get_cmo(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_cmo(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/apo")
async def get_apo(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_apo(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})    


@app.post("/ppo")
async def get_ppo(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_ppo(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/mfi")
async def get_mfi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_mfi(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/coppock")
async def get_coppock(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_coppock(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/donchian")
async def get_donchian(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_donchian(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/obv")
async def get_obv(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_obv(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/efi")
async def get_efi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_efi(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/aroon")
async def get_aroon(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = aroon(candles, data.period)

    return {
        "indicator": "aroon",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "aroon_down": result.down.tolist() if isinstance(result.down, np.ndarray) else result.down,
        "aroon_up": result.up.tolist() if isinstance(result.up, np.ndarray) else result.up
    }


@app.post("/ao")
async def get_ao(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = ao(candles)

    return {
        "indicator": "ao",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "ao_osc": result.osc.tolist() if isinstance(result.osc, np.ndarray) else result.osc,
        "ao_change": result.change.tolist() if isinstance(result.change, np.ndarray) else result.change
    }


@app.post("/bop")
async def get_bop(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = bop(candles)

    return {
        "indicator": "bop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/ad")
async def get_ad(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = ad(candles)

    return {
        "indicator": "ad",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/bollinger_bands_width")
async def get_bbw(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = bollinger_bands_width(candles, data.period)

    return {
        "indicator": "bollinger_bands_width",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/cfo")
async def get_cfo(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = cfo(candles, period=data.period)

    return {
        "indicator": "cfo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/adosc")
async def get_adosc(data: ADOSCRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = adosc(
        candles,
        fast_period=data.fast_period,
        slow_period=data.slow_period
    )

    return {
        "indicator": "adosc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/cksp")
async def get_cksp(data: CKSPRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = cksp(candles, p=data.p, x=data.x, q=data.q)

    return {
        "indicator": "cksp",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "p": data.p,
        "x": data.x,
        "q": data.q,
        "long_stop": result.long.tolist() if isinstance(result.long, np.ndarray) else result.long,
        "short_stop": result.short.tolist() if isinstance(result.short, np.ndarray) else result.short
    }


@app.post("/chop")
async def get_chop(data: CHOPRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = chop(
        candles,
        period=data.period,
        scalar=data.scalar,
        drift=data.drift
    )

    return {
        "indicator": "chop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "scalar": data.scalar,
        "drift": data.drift,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/correl")
async def get_correl(data: CorrelRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = correl(candles, period=data.period)

    return {
        "indicator": "correl",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }





