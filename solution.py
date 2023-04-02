import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    a = 0.047
    b = 2 * np.mean(x) - a
    n = len(x)
    variance = ((b - a) ** 2) / 12
    z = norm.ppf(1 - p / 2)
    interval = (b - z * np.sqrt(variance / n), b + z * np.sqrt(variance / n))
    return interval

