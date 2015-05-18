import os
import sys

here = os.path.abspath(os.path.split(__file__)[0])
repo_root = os.path.abspath(here)

sys.path.insert(0, repo_root)
sys.path.insert(0, os.path.join(repo_root, "six"))
sys.path.insert(0, os.path.join(repo_root, "html5lib"))
sys.path.insert(0, os.path.join(repo_root, "wptserve"))
sys.path.insert(0, os.path.join(repo_root, "pywebsocket", "src"))
