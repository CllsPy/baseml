from baseml.data_loader import build_path
from pathlib import Path
from baseml.data_loader import load_data

import pytest
import pandas as pd


@pytest.fixture
def base_url():
    return "sample"


@pytest.fixture
def tmp_path():
    return "tests/assets/"


def test_path_exists(base_url, tmp_path):
    tmp = tmp_path
    path = build_path(base_url, tmp)
    assert Path(path).exists(), f"O diretório {path} não existe"


def test_target_name(base_url, tmp_path):
    ds = load_data(base_url, tmp_path)
    required = "target"

    assert required in ds
