import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:

    k = np.ceil(p * len(x)).astype(int)
    alpha_quantile = np.sort(x)[k]

    left = 0.047
    right = alpha_quantile
    return (left, right)

