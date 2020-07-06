import os
import pathlib

BASE_DIR: str = pathlib.Path(__file__).parent
CANDY_DIR: str = os.path.join(BASE_DIR, "static/candy")
CANDY_RELATIVE_PREFIX = os.path.join("static", "candy")