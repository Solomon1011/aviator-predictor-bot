import numpy as np

def suggest_cashout(history):

    if len(history) < 20:
        return 1.5

    avg = np.mean(history)

    if avg < 2:
        return 1.4
    elif avg < 3:
        return 1.8
    else:
        return 2.2
