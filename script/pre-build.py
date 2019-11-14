#
# This script runs cppcheck before the build process
#

Import("env")
from subprocess import call
import os

print "[PREBUILD] BEGIN ---"

# os.getcwd() returns the project absolute path not this file path
call(["cppcheck", os.getcwd()+"/src/", "--enable=all"])


print "[PREBUILD] ENDED ---"