import pandas as pd
from python.validate_etl import non_null, unique

def test_non_null_pass():
    df = pd.DataFrame({'a':[1,2], 'b':[3,4]})
    non_null(df, ['a','b'])

def test_unique_fail():
    import pytest
    df = pd.DataFrame({'id':[1,1,2]})
    with pytest.raises(AssertionError):
        unique(df, 'id')