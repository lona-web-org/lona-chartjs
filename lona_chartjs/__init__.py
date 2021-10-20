try:
    from .widgets import *  # NOQA

except ImportError:
    pass

VERSION = (0, 1, 2)
VERSION_STRING = '{}'.format('.'.join([str(i) for i in VERSION]))
