import ska_helpers

__version__ = ska_helpers.get_version(__package__)

from .fep1_mong_check import \
    FEP1MongCheck, main, \
    model_path


def test(*args, **kwargs):
    """
    Run py.test unit tests.
    """
    import testr
    return testr.test(*args, **kwargs)
