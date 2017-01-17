# python startup file
import sys
import readline
import os
import rlcompleter
# tab completion
readline.parse_and_bind('tab: complete')
histfile = os.path.join(os.environ['HOME'],'.pythonhistory')
