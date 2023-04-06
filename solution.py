import pandas as pd
import numpy as np

from scipy.stats import norm


import pandas as pd
import numpy as np

from scipy.stats import norm
def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    m = x.mean()
    left =  (m - 0.047) / (1 - (alpha / 2)) 
    right =  (m - 0.047) / (alpha / 2) 
    return (left, right)

