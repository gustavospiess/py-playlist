import os

from logs import log_function


__version__ = '0.0.2'


@log_function
def expand_path(path):
    user_expanded = os.path.expanduser(path)
    vars_expanded = os.path.expandvars(user_expanded)
    abs_path = os.path.abspath(vars_expanded)
    return abs_path
