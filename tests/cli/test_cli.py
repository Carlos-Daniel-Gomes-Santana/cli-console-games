from src.cli import hello
from click.testing import CliRunner

def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert result.output == "Hello World\n"
