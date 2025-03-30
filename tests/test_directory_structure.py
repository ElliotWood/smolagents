import pytest
from pathlib import Path

REQUIRED_DIRS = [
    "src/smolagents",
    "tests",
    "docs",
    "examples",
    "memory"
]

REQUIRED_FILES = [
    "pyproject.toml",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    ".github/workflows/tests.yml"
]

class TestDirectoryStructure:
    @pytest.mark.parametrize("dir_path", REQUIRED_DIRS)
    def test_required_directories_exist(self, dir_path):
        path = Path(dir_path)
        assert path.exists(), f"Missing required directory: {dir_path}"
        assert path.is_dir(), f"Path is not a directory: {dir_path}"

    @pytest.mark.parametrize("file_path", REQUIRED_FILES)
    def test_required_files_exist(self, file_path):
        path = Path(file_path)
        assert path.exists(), f"Missing required file: {file_path}"
        assert path.is_file(), f"Path is not a file: {file_path}"

    def test_init_files(self):
        for dir_path in REQUIRED_DIRS:
            init_path = Path(dir_path) / "__init__.py"
            # Special case for tests directory
            if dir_path == "tests":
                continue  # Skip checking __init__.py in tests directory
            if dir_path.startswith("src"):
                assert init_path.exists(), f"Missing __init__.py in {dir_path}"
            else:
                assert not init_path.exists(), f"Unexpected __init__.py in {dir_path}"