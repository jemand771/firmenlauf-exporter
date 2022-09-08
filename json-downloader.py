import json
from pathlib import Path

import requests

API_URL = "https://www.davengo.com/event/result/schnellestellede-firmenlauf-chemnitz-2022/search/list"
POST_JSON = dict(
    query={},
    type="extended"
)
OUTPUT_DIR = Path("./data")


def paginated_request(category: str, offset: int=0):
    print(f"requesting results {category=} {offset=}")
    r = requests.post(API_URL, json=POST_JSON | dict(category=category, offset=offset))
    assert r.status_code == 200
    if r.json()["results"] == [] or "navigation" not in r.json():
        return []
    return [
        *r.json()["results"],
        *paginated_request(category=category, offset=r.json()["navigation"]["nextOffset"])
    ]


def main():
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    r = requests.get("https://www.davengo.com/event/result/schnellestellede-firmenlauf-chemnitz-2022/init")
    assert r.status_code == 200
    for category in r.json()["categories"]:
        catname = category["id"]
        results = paginated_request(category=catname)
        fields = category["fields"]
        with open(OUTPUT_DIR / f"{catname}.fields.json", "w") as f:
            json.dump(fields, f, indent=2, ensure_ascii=False)
        with open(OUTPUT_DIR / f"{catname}.results.json", "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()