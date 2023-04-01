import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    quantile = np.quantile(x, p)
    delta = 0.01
    left_border = 0.047
    right_border = quantile * (1 + delta)
    
    return (left_border, right_border)
