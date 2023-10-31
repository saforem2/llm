"""
llm/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function
import logging
import os
from typing import Optional
from enrich.console import is_interactive, get_console
# import warnings

from mpi4py import MPI
from enrich.handler import RichHandler
import tqdm
# from rich import print
# from enrich import get_logger
from pathlib import Path
