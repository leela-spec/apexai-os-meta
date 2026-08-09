"""Closed exception hierarchy for lmbench. Stdlib only.

Every lmbench exception is a `BenchError`, so a test can assert the hierarchy is
closed (`isinstance(exc, BenchError)`) rather than trusting call sites to remember
which module's error type to catch.
"""

from __future__ import annotations


class BenchError(Exception):
    """Base for every error this package raises."""


class PolicyError(BenchError):
    """A policy definition is malformed or internally inconsistent."""


class FixtureError(BenchError):
    """A fixture is malformed, or an answer-hiding invariant was violated at load time."""


class AdapterError(BenchError):
    """A model/runtime adapter transport or protocol failure."""


class InfraInvalid(BenchError):
    """The trial environment itself failed, was tampered with, or could not be
    verified -- this is never an actor result, pass or fail."""
