"""Multi-repo probe: proves this repo works concurrently with the others."""

REPO_SLUG = 'gamma'


def repo_slug():
    """Return this repo's slug: ``gamma``."""
    return REPO_SLUG


if __name__ == '__main__':
    print(repo_slug())
