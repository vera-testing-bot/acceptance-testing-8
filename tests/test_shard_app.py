"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add  # noqa: E402


def test_add() -> None:
    assert add(2, 3) == 5


def test_stop_marker_present() -> None:
    """Issue #4: stop_marker.txt must exist in repo root with stop-2dd9b304."""
    marker = Path(__file__).resolve().parents[1] / "stop_marker.txt"
    assert marker.is_file()
    assert marker.read_text().strip() == "stop-2dd9b304"
