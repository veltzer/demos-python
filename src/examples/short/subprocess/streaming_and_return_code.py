"""
This is an example of how to use the subprocess module for streaming
"""

import subprocess

with subprocess.Popen(
    ['ls','-l'],
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
) as p:
    # do not use p.stdout.readlines() in the next line as it will block...
    for line in p.stdout:
        line = line.decode().rstrip()
        print(f"line is [{line}]")
    p.wait()
    print(f"return code is [{p.returncode}]")

# This next examples does not work
# pylint: disable=using-constant-test
if False:
    with subprocess.Popen(
        ['ls','-l'],
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as p:
        # this is another version but which gives you an addition last line of ''
        while p.poll() is None:
            line = p.stdout.readline().decode().rstrip()
            print(f"line is [{line}]")
        p.wait()
        print(f"return code is [{p.returncode}]")
