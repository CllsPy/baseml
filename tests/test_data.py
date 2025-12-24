from baseml.data_loader import build_path
from pathlib import Path
from baseml.data_loader import load_data

import pytest
import pandas as pd

@pytest.fixture
def base_url():
    return "sample"

def test_path_exists(base_url):
    tmp = "tests/assets/"
    path = build_path(base_url, tmp)
    assert Path(path).exists(), f"O diretório {path} não existe"

def test_target_name():
    pass