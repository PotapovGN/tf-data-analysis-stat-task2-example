import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    m = x.mean()
    left = ( (m - 0.047) / (1 - (alpha / 2)) ) + 0.047
    right = ( (m - 0.047) / (alpha / 2) ) + 0.047
    return (left, right)


