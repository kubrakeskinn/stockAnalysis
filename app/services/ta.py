import pandas as pd
import pandas_ta as ta

def get_ta_indicators(df):
    # df: pandas DataFrame, OHLCV verisi içermeli
    result = {}
    result['sma20'] = df.ta.sma(length=20).iloc[-1]
    result['sma50'] = df.ta.sma(length=50).iloc[-1]
    result['sma200'] = df.ta.sma(length=200).iloc[-1]
    result['ema12'] = df.ta.ema(length=12).iloc[-1]
    result['ema26'] = df.ta.ema(length=26).iloc[-1]
    result['rsi14'] = df.ta.rsi(length=14).iloc[-1]
    macd = df.ta.macd(fast=12, slow=26, signal=9)
    result['macd'] = macd['MACD_12_26_9'].iloc[-1]
    result['macd_signal'] = macd['MACDs_12_26_9'].iloc[-1]
    result['macd_hist'] = macd['MACDh_12_26_9'].iloc[-1]
    bbands = df.ta.bbands(length=20, std=2)
    result['bb_upper'] = bbands['BBU_20_2.0'].iloc[-1]
    result['bb_middle'] = bbands['BBM_20_2.0'].iloc[-1]
    result['bb_lower'] = bbands['BBL_20_2.0'].iloc[-1]
    return result 