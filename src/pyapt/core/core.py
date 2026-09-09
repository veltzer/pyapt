"""
core.py
"""

import json
import os


def read_config():
    file_name = os.path.expanduser("~/.pyapt/config.json")
    with open(file_name, encoding="utf-8") as stream:
        return json.load(stream)


def apply_ppa():
    pass
