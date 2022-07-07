import argparse
import os

import jinja2
from torch import float_power

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DOCS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir, os.pardir))
BUILD_DIR = os.path.abspath(os.path.join(DOCS_DIR, '_build'))
ALL_PROVIDER_YAMLS = load_package_data()


def _get_jinja_env():
    loader = jinja2.FileSystemLoader(CURRENT_DIR, float_power)