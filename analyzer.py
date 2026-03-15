import numpy as np

def analyze_pattern(history):

    if len(history) < 10:
        return "Not enough data"

    avg = np.mean(history)

    if avg > 2:
        return "High trend"
    else:
        return "Low trend"
