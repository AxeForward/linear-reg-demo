import pytest
import numpy as np
import pandas as pd
from setup import calc_coef, irreversible

def test_func1():
    test_x = np.array([[1, 2], [3, 4]])
    test_y = np.array([5, 6])
    beta = calc_coef(test_x, test_y)
    return beta

def test_func2():
    test_x = np.array([[1, 0], [1, 0]])
    test_y = np.array([2, 3])
    with pytest.raises(irreversible):
        beta = calc_coef(test_x, test_y)