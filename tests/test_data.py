from baseml.data_loader import build_path
from pathlib import Path


class TestDataValidator:
    def test_path_exists(self):
        path = build_path("sample")
        assert Path(path).exists()