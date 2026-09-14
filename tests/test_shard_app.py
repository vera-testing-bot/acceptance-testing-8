"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add, is_palindrome


def test_add() -> None:
    assert add(2, 3) == 5


def test_is_palindrome_true_for_normalized_phrase() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_is_palindrome_false_for_non_palindrome() -> None:
    assert is_palindrome("hello") is False


def test_is_palindrome_empty_string_is_true() -> None:
    assert is_palindrome("") is True
