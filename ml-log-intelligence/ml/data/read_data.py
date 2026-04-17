from pathlib import Path
from typing import Union

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "scripts" / "test.jsonl"


def load_data(path: Union[str, Path] = DATA_PATH) -> pd.DataFrame:
    data_path = Path(path)
    return pd.read_json(data_path, lines=True)


data_frame = load_data()
