from unittest.mock import patch, mock_open
from app.processor import process_folder

@patch("app.processor.os.listdir")
@patch("app.processor.os.path.isfile")
@patch("builtins.open", new_callable=mock_open, read_data="hello")
def test_process_folder(mock_open_fn, mock_isfile, mock_listdir):
    mock_listdir.return_value = ["a.txt", "b.txt"]
    mock_isfile.return_value = True

    result = process_folder("dummy_folder")

    assert result["a.txt"] == 5
    assert result["b.txt"] == 5