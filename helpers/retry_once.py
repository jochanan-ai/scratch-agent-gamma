"""Call a function once more on failure, optionally filtered by type."""

from typing import Any, Callable, TypeVar

_T = TypeVar("_T")


def retry_once(
    fn: Callable[..., _T],
    *args: Any,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
    **kwargs: Any,
) -> _T:
    """Call ``fn``; on a matching exception, retry exactly once.

    Returns ``fn()``'s result on success. If the first call raises an
    exception that is an instance of one of the types in ``exceptions``,
    the call is attempted one more time; the retry's result is returned,
    or the retry's exception is re-raised if it also fails. Any other
    exception is re-raised immediately without a retry.

    ``exceptions`` defaults to ``(Exception,)`` and may be a tuple of
    exception classes or a single exception class.
    """
    try:
        return fn(*args, **kwargs)
    except exceptions:
        return fn(*args, **kwargs)
