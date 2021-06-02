"""
Some OS Examples

Book p.510

Date: Oliver Zott
Version: 1.0 / 13.09.2019
"""

import os
import sys

''' import os functions '''
# Some commands
print(os.environ['USERPROFILE'])
print(os.getpid())
print(os.cpu_count())

# use sys commands
# os.system("mkdir teeest")

# use popen to execute command in cmd
output = os.popen("dir /B C:\\")
files = [line.strip() for line in output]
print(files)

''' import sys functions (runtime environment) '''
