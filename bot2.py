"""
This file contains the PyAIML stress test.  It creates two bots, and connects
them in a cyclic loop.  A lot of output is generated; piping the results to
a log file is highly recommended.
"""
from __future__ import print_function

import aiml

# Create the kernels
kern1 = aiml.Kernel()
kern1.verbose(False)
# kern2 = aiml.Kernel()
# kern2.verbose(False)

# Initialize the kernels

kern1.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
kern1.saveBrain("standard.brn")
# print( "\nInitializing Kernel #2" )
# kern2.bootstrap(brainFile="standard.brn")
# Start the bots off with some basic input.
print( "机器人已上线：" )

# Off they go!
while True:
    presponse = input()
    response0 = kern1.respond(presponse).strip()
    print( "1:", response0, "\n" )
    if presponse == "":
        response = "askquestion"
