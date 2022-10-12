from dispatcher import BaseDispatcher
from patched import *

try:
    import uvloop as _uvloop

    _uvloop.install()
except ImportError:  # pragma: no cover
    pass

__all__ = (
    "BaseDispatcher",
    "Client",
    "Proxy",
    "ProxyDict",
    "Autofill",
    "__version__",
)

__version__ = "0.1.0"
