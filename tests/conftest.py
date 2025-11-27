import os
import sys


# Ensure `src` is on sys.path so tests can import virtual_pet during local test runs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
