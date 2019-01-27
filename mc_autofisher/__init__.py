"""
Automated Fishing Program for Minecraft

Command Line Usage
^^^^^^^^^^^^^^^^^^
    .. code:: bash

        python -m mc-autofisher [--levdist x] [--tesspath x] [-s|--new-bbox] [...]
    
    **Arguments:**
        ``--levdist x``: Integer (default 5)
            The maximum Levenshtein distance allowed for text matching, accounts for slight
            errors in Tesseract's text recognition, i.e. 'Fishing Gobber' instead of 'Fishing Bobber'
        ``--tesspath x``: String
            The path to your Tesseract installation, usually unnecessary unless you have some special setup
        ``--new-bbox`` or ``-s``
            Tells the program you want to run the screengrabber and record the new bounding box in the config
            file. The screengrabber will run by default if there is not a bounding box already recorded in the
            config file and you have not manually provided coordinates on the command line

    **Other Parameters:**
        If four flagless arguments are present they will be treated as manually-entered
        coordinates of the top left and bottom right corners of the bounding box and will take precedence
        over ``--new-bbox`` and the coordinates in the config file
    
    **Examples:**
        .. code:: bash

            $ python -m mc-autofisher                               # Runs with parameters from config file

            $ python -m mc-autofisher 50 50 100 100                 # Runs with specified bounding box, all other parameters from config file

            $ python -m mc-autofisher --levdist 1                   # Runs with a maximum Levenshtein distance of 1

            $ python -m mc-autofisher --tesspath /home/Desktop      # Why would you install Tesseract on your Desktop?

            $ python -m mc-autofisher --new-bbox                    # Runs the screengrabber first to allow selection of a new bounding box
"""
__author__ = "Robert Best"
__email__  = "bobbyisbest3@gmail.com"
__version__= "1.2.0"
