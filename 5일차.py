import sys
import runpy

target = sys.argv[1]

if not target.endswith(".py"):
    print("it isn't python script.")
else:
    runpy.run_path(target)