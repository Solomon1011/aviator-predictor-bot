import json
import time
import random
from analyzer import analyze_pattern
from strategy import suggest_cashout

HISTORY_FILE = "history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def collect_round():
    # placeholder for real data
    return round(random.uniform(1.0, 10.0), 2)

while True:

    history = load_history()

    crash = collect_round()
    history.append(crash)

    save_history(history)

    print("Crash:", crash)

    pattern = analyze_pattern(history)
    print("Pattern:", pattern)

    suggestion = suggest_cashout(history)
    print("Suggested Cashout:", suggestion)

    print("----------------------")

    time.sleep(5)
