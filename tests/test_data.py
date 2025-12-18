from baseml.data_loader import build_path
from pathlib import Path

import pytest
import pandas as pd

@pytest.fixture
def base_url():
    return "sample"

def test_path_exists(base_url):
    path = build_path(base_url)
    assert Path(path).exists(), f"O diretório {path} não existe"