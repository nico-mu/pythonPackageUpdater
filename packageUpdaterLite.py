#!/usr/bin/env python
# @author nico-mu
# @email nico.muszalczyk@gmail.com
# @create date 12-02-2021 10:37:07
# @modify date 12-02-2021 10:37:07
# @desc updates all python packages on given system

import os
import sys
import pkg_resources
from math import floor
from subprocess import call

def clear():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")

log = False

if len(sys.argv) > 1:
    log = True if sys.argv[1] == "--log" else False

if log:
    f = open('log.txt', 'w')
else:
	f = True

packages = [dist.project_name for dist in pkg_resources.working_set]

for index in range(len(packages)):
    progress = index/len(packages) * 10
    roundedProgress = floor(progress * 2)
    progressBar = int(roundedProgress) * "#"
    emptyBar = int(20 - roundedProgress) * " "
    print(f"[{progressBar}{emptyBar}]\t{round(progress * 10, 1)}%")
    call(f"pip install --upgrade {packages[index]}", shell=True, stdout=f)
    clear()
print(f"[{20*'#'}]\t100.0%")
