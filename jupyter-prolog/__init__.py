"""Prolog for JupyterHub/Lab"""
__version__ = '0.0.1'

from .prolog import Prolog_Magics

def load_ipython_extension(ipython):
    ipython.register_magics(Prolog_Magics)
