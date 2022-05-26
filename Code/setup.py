import numpy as np
import pandas as pd
import os

class irreversible(Exception):
    """
    Pop up
    """

def calc_coef(arr_x, arr_y):
    XX = np.matmul(arr_x.T, arr_x)
    if np.linalg.det(XX) == 0:
        raise irreversible('Matrix Irreversible')
    else:
        inv_XX = np.linalg.inv(XX)
        temp = np.matmul(inv_XX, arr_x.T)
        arr_coef = np.matmul(temp, arr_y)
        return arr_coef

data_path = '../Data/calc_data.xlsx'
df = pd.read_excel(data_path, index_col=0, parse_dates=['Date'])
df['const'] = 1
y = df.IdxMonRet.values
X = df[['Rmrf_mc', 'Smb_mc', 'Hml_mc', 'const']].values

beta = calc_coef(X, y)
print("alpha = ", beta[3])




