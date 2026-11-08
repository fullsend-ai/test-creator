"""
Unit tests for scripts/list_test_functions.py

Tests extraction of test function definitions from Python test files.
"""

import json

import pytest

from scripts.list_test_functions import list_test_functions, main
from tests.consts.discovery_constants import MIXED_TEST_DISCOVERY_SOURCE


def test_extracts_test_functions_with_docstrings(tmp_path):
    """Should extract function names, line numbers, and docstrings."""
    test_file = tmp_path / "test_example.py"
    test_file.write_text('''
def test_create_notebook():
    """Test notebook creation via API."""
    assert True

def helper_function():
    """Not a test."""
    return 42

def test_delete_notebook():
    assert False
''')

    result = list_test_functions(str(test_file))
    data = json.loads(result)

    assert len(data["functions"]) == 2
    assert data["functions"][0]["name"] == "test_create_notebook"
    assert data["functions"][0]["line"] == 2
    assert data["functions"][0]["docstring"] == "Test notebook creation via API."
    assert data["functions"][1]["name"] == "test_delete_notebook"
    assert data["functions"][1]["docstring"] is None


def test_handles_missing_file(tmp_path):
    """Should raise error if file doesn't exist."""
    with pytest.raises(FileNotFoundError):
        list_test_functions(str(tmp_path / "nonexistent.py"))


class TestListTestFunctionsCLI:
    def test_lists_sync_and_async_test_metadata(self, tmp_path, run_cli):
        test_file = tmp_path / "test_mixed.py"
        test_file.write_text(MIXED_TEST_DISCOVERY_SOURCE)

        exit_code, output = run_cli(main, [str(test_file)])

        assert exit_code == 0
        assert output == {
            "file": str(test_file),
            "functions": [
                {"name": "test_sync", "line": 1, "docstring": "Synchronous test."},
                {"name": "test_async", "line": 5, "docstring": "Asynchronous test."},
                {"name": "test_decorated_async", "line": 10, "docstring": None},
                {"name": "test_async_method", "line": 17, "docstring": "Asynchronous method."},
            ],
        }
