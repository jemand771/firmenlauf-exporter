import json

import numpy as np


with open("data/Einzelwertung.results.json") as f:
    times = []
    for entry in json.load(f):
        hours, minutes, seconds = map(int, entry["nettoTime"].split(":"))
        times.append(round(60 * hours + minutes + seconds / 60, 2))
    bars, bins = np.histogram(times, bins=60, range=(0, 60))
    print("bins:", ",".join(str(bin_) for bin_ in bins))
    print("bars:", ",".join(str(bar) for bar in bars))
