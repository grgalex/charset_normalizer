#!/usr/bin/env python
from __future__ import annotations

import os
import sys

from setuptools import setup

USE_MYPYC = True

if USE_MYPYC:
    from mypyc.build import mypycify

    MYPYC_MODULES = mypycify(
        [
            "src/charset_normalizer/md.py",
        ],
        debug_level="3",
        opt_level="0",
    )
else:
    MYPYC_MODULES = None

setup(name="charset-normalizer", ext_modules=MYPYC_MODULES)
