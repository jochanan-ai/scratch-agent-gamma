"""Call a function once more on failure."""


def retry_once(fn, *args, **kwargs):
    """Call ``fn``; on exception, retry exactly once.

    Returns ``fn()``'s result on success. If the first call raises, the
    call is attempted one more time; the retry's result is returned, or
    the retry's exception is re-raised if it also fails.
    """
    try:
        return fn(*args, **kwargs)
    except Exception:
        return fn(*args, **kwargs)
