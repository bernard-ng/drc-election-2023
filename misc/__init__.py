import os
import csv
import json

import pandas as pd

# Paths
ROOT_DIR = os.path.dirname(os.path.curdir)
DATA_DIR = os.path.join(ROOT_DIR, 'dataset')

PROVINCE_ID_RANGE = range(1, 32)
API_BASE_URL = 'https://www.cartographie.ceni.cd/mapapi.php'


def load_csv_dataset(path: str, limit: int = None) -> list:
    print(f">> Loading CSV dataset from {path}")
    data = []
    with open(os.path.join(DATA_DIR, path), "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
            if limit and len(data) >= limit:
                break

    return data


def save_json_dataset(data, path: str) -> None:
    print(f">> Saving JSON dataset to {path}")
    with open(os.path.join(DATA_DIR, path), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))


def save_csv_dataset(data, path: str, columns: list = None) -> None:
    print(f">> Saving CSV dataset to {path}")
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATA_DIR, path), index=False, columns=columns)
