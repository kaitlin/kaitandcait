__version__ = '2.3.0'

from articles.directives import *
try:
    import listeners
except ImportError:
    # this happens when setup.py is grabbing __version__; nothing to worry
    # about
    pass
