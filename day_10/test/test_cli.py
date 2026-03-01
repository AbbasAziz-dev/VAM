from unittest.mock import patch
from app.cli import main

@patch("app.cli.process_folder")
@patch("sys.argv", ["cli.py", "dummy_folder"])
def test_cli_runs(mock_process):
    mock_process.return_value = {"file.txt": 10}

    main()

    mock_process.assert_called_once_with("dummy_folder")