from jupyterworkflow.data import get_freemont_data
import pandas as pd

def test_freemont_data() :
    data = get_freemont_data()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
