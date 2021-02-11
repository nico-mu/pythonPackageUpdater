import os
import pkg_resources
from argparse import ArgumentParser
from subprocess import call
from tqdm.auto import tqdm

def clear():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")

parser = ArgumentParser(description='Tool for updating installed pyhton packages with pip.')
parser.add_argument("--log", action="store_const", const=True, default=False, help="Add Output to log file")

args, unknown = parser.parse_known_args()

if args.log:
    f = open('log.txt', 'w')
else:
	f = True
packages = [dist.project_name for dist in pkg_resources.working_set]

for index in tqdm(range(len(packages))):
    print("\n\r")
    call(f"pip install --upgrade {packages[index]}", shell=True, stdout=f)
    clear()