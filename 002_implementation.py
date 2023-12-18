from unittest.mock import patch
from io import StringIO
from protocol import Protocol, main, readin
import pytest

@pytest.fixture
def protocol_instance():
    return Protocol()

@patch("builtins.input", side_effect=["Request", "Hello, World!"])
def test_readin_valid_input(protocol_instance, monkeypatch):
    monkeypatch.setattr('__main__.pr', protocol_instance)
    itype, message = readin()
    assert itype == 1
    assert message == "Hello, World!"

@patch("builtins.input", side_effect=["InvalidType", "Hello, World!"])
def test_readin_invalid_input(protocol_instance, monkeypatch):
    monkeypatch.setattr('__main__.pr', protocol_instance)
    with pytest.raises(ValueError, match="Unknown Type"):
        readin()

@patch("sys.stdout", new_callable=StringIO)
@patch("builtins.input", side_effect=["Request", "Hello, World!"])
def test_main(protocol_instance, mock_input, mock_stdout, monkeypatch):
    monkeypatch.setattr('__main__.pr', protocol_instance)
    main()
    output = mock_stdout.getvalue()
    assert "Encoded Data" in output
    assert "Decoded Type" in output
    assert "Decoded Length" in output
    assert "Decoded Value" in output
