Import("env")
from subprocess import call
import os

print "[PREBUILD] BEGIN ---"

def run_cppcheck(source, target, env):
    print("Starting cppcheck...\n")
    call(["cppcheck", os.getcwd()+"src/", "--enable=all"])
    print("Finished cppcheck...\n")

env.AddPreAction("buildprog", run_cppcheck)

print "[PREBUILD] ENDED ---"