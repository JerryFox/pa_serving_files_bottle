ROOT = "/home/jardacarda"   # where are files serving from
PATH_PREFIX = "/files"      # path prefix in browser
INTER_PATH = ""             # if app is not in the root of the hosting server
SHOW_HIDDEN = False         # items with "hidden" prefix

try:
    from hiddenconfig import ROOT, PATH_PREFIX, INTER_PATH, SHOW_HIDDEN
except ImportError:
    try:
        from .hiddenconfig import ROOT, PATH_PREFIX, INTER_PATH, SHOW_HIDDEN
    except ImportError:
        pass
