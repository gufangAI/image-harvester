#!/usr/bin/env python3
# Loader: clone the private worker repo and run it. Keeps this public repo logic-free.
import os, sys, subprocess
_t = os.environ["P"]
subprocess.check_call(["git", "clone", "--depth", "1", "--quiet",
    f"https://x-access-token:{_t}@github.com/hosonzuo8848/harvester-priv.git", "_p"])
sys.path.insert(0, "_p")
import hv
hv.main()
