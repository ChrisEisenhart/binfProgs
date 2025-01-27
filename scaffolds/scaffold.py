#!/usr/bin/env python2.7
# Chris Eisenhart - My generic scaffold for python scripts.  Feel free to use without citation


"""
Put something here
"""
import os
import sys
import argparse
import logging
log = None # The global logger is defined, it will be initiated after the user commands are read

def parseArgs(args): 
    """
    Parse the command line arguments into useful python objects.  '--' variables are optional
    set_defaults only applies when the argument is not provided (it won't override)
    """
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument("inFile",
                        help = " The input file",
                        action = "store")
    parser.add_argument("outFile",
                        help = " The output file",
                        action = "store")
    parser.add_argument("--verbose",
                        help = " The verbosity level for stdout messages (default INFO)",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        action = "store")

    parser.set_defaults(verbose = "INFO")

    options = parser.parse_args()

    # Basic logging config and update the logging verbosity level
    logging.basicConfig(format='[%(filename)s %(funcName)s %(lineno)d %(levelname)s] %(message)s', level=options.verbose)

    # Define a file for the log object to write too
    fh = logging.FileHandler(__file__ + '.log')

    # Create the logger and add the file handler to it
    global log
    log = logging.getLogger(__name__)
    log.addHandler(fh)
    return options



def main(args):
    """
    Basic file parsing. Open the input file, read it one line at a time to a list.
    Open the output file, go over the list one element at a time and write it to the output file.

    If file size is a concern then loading it into a list may not be feasible.  In these cases handle
    each line at a time and immediately write it to the output file.
    """ 
    options = parseArgs(args)
    in_file_contents = None
    log.info("Reading in file {}".format(options.inFile))
    with open(options.inFile, "r") as in_file:
        in_file_contents = [line.strip().split() for line in in_file]

    log.info("Writing out file {}".format(options.outFile))
    with open(options.outFile, "w") as out_file:
        for line in in_file_contents:
            out_file.write("\t".join(line) + "\n")

    log.info("Finished!".format(options.outFile))


if __name__ == "__main__" :
    sys.exit(main(sys.argv))
