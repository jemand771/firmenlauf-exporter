import csv
import json
from pathlib import Path


INPUT_PATH = Path("./data")
OUTPUT_PATH = Path("./intenta-data")


def main():
    OUTPUT_PATH.mkdir(exist_ok=True, parents=True)
    if not INPUT_PATH.is_dir():
        print("missing input data")
        exit(0)
    for in_path in INPUT_PATH.glob("*.results.json"):
        with open(in_path) as f:
            data = json.load(f)
        filtered_data = [
            obj for obj in data
            if obj["firma"] == "Intenta GmbH"
        ]
        if not filtered_data:
            continue
        with open(OUTPUT_PATH / in_path.relative_to(INPUT_PATH).with_suffix(".csv"), "w") as f:
            writer = csv.DictWriter(f, filtered_data[0].keys())
            writer.writeheader()
            for row in filtered_data:
                writer.writerow(row)


if __name__ == "__main__":
    main()
