import os
import sys
from typing import Any

# Настраиваем видимость папки src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.decorators import log


def test_log_console_success(capsys: Any) -> None:
    """Тестирует успешный вывод лога в консоль."""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_console_error(capsys: Any) -> None:
    """Тестирует вывод лога об ошибке в консоль."""

    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_file_success(tmp_path: Any) -> None:
    """Тестирует успешную запись лога в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def greet(name: str) -> str:
        return f"Hello, {name}"

    assert greet("Alex") == "Hello, Alex"

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "greet ok\n" == content


def test_log_file_error(tmp_path: Any) -> None:
    """Тестирует запись лога об ошибке в файл."""
    log_file = tmp_path / "test_error.log"

    @log(filename=str(log_file))
    def fail_func() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail_func()

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "fail_func error: ValueError. Inputs: (), {}" in content
