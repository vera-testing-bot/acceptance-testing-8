"""Trivial module so an acceptance shard repo has code to change."""


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def is_palindrome(text: str) -> bool:
    """Return True when ``text`` reads the same forwards and backwards.

    Comparison ignores case and any non-alphanumeric characters.
    """
    normalized = [ch.lower() for ch in text if ch.isalnum()]
    return normalized == normalized[::-1]
