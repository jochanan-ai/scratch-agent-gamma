"""Truncate a string to n characters, appending an ellipsis when cut."""

ELLIPSIS = "…"


def truncate(text: str, n: int) -> str:
    """Return `text` cut to `n` characters with an ellipsis appended.

    Strings at or under `n` characters pass through unchanged.
    """
    if len(text) <= n:
        return text
    return text[:n] + ELLIPSIS
