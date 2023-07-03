"""
    Author: Carlos Daniel Gomes Santana
    Description: Unit Tests for commands of CLI
"""
from click.testing import CliRunner

from src.cli import hello


def test_hello_command():
    """Unit Test for hello command of CLI"""
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert result.output == "Hello World\n"
