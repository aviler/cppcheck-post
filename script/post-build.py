#
# This script does nothing. Is here only for example purpose
#

# Both AddPreAction() and AddPostAction() require a target and
# targets are only available for platformio.ini "post:" scripts
# So only use these functions in a post build environment
# ref. https://github.com/platformio/platformio-core/issues/2973#issuecomment-527423454

# List of possible targets for the above mentioned functions
# https://docs.platformio.org/en/latest/projectconf/advanced_scripting.html#before-pre-and-after-post-actions

Import("env")
from subprocess import call
import os

print "[POSTBUILD] BEGIN ---"

def run_pre(source, target, env):
  print("\nStarting PRE ACTION...\n")
  print("Finished PRE ACTION.\n")

def run_post(source, target, env):
  print("\nStarting POST ACTION...\n")
  print("Finished POST ACTION.\n")

# run_pre is called before the actual program packagin
env.AddPreAction("buildprog", run_pre)

# run_post is called after the upload finishes
env.AddPostAction("upload", run_post)

print "[POSTBUILD] ENDED ---"