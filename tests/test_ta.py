import pandas as pd
from app.services.ta import get_ta_indicators

def test_ta_indicators():
    data = {
        'close': [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
        'open': [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],
        'high': [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        'low': [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],
        'volume': [1000]*21
    }
    df = pd.DataFrame(data)
    ta = get_ta_indicators(df)
    assert 'sma20' in ta
    assert 'rsi14' in ta 