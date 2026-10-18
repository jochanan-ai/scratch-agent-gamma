"""Onboarding shadow-cycle artifact for the gateway-infra factory pipeline.

This file exists to prove the factory pipeline end-to-end against this repo
as part of the shadow dev cycle (task issue #9, tier t2). It is intentionally
minimal: a single documented function exercising the full write path.
"""


def add(a, b):
    """Return the sum of ``a`` and ``b``."""
    return a + b
