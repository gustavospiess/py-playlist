from .. import utils
from .. import __version__


def test_version_defined():
    assert __version__ is not None


def test_expand_path():
    assert utils.expand_path('~') != '~'


def test_fstr():
    assert f'a{1+2}' == 'a3'
