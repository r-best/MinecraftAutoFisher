"""
Automated Fishing Program for Minecraft

Command Line Usage
^^^^^^^^^^^^^^^^^^
    .. code:: bash

        python -m mc-autofisher [--levdist x] [--tesspath x] [-s|--new-bbox] [...]
"""
from .fisher import start
from .screengrabber import grab
