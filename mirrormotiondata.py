import sys
import os
import pyfbsdk
try:
    import mbtools as mb
except ImportError:
    MBTOOLS_PATH = os.path.dirname(os.path.realpath(__file__))
    if MBTOOLS_PATH not in sys.path:
        sys.path.append(MBTOOLS_PATH)
        import mbtools as mb

reload(mb)

