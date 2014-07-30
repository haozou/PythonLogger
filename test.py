import os, sys
import re
from optparse import OptionParser
from log import getLogger

LOG = getLogger(__name__)

class Main:

    def __init__(self, args=None):
        self.__parseoptions(args)

    def __parseoptions(self, args):
        usage = "usage: %prog [options]"
        parser = OptionParser(usage)
        parser.add_option('-f', '--file', action='store', type="string",
                            dest='file', help='the filename used to deal with')
        parser.add_option('--verbose', action='store_true', default=False,
                            help = 'enable the debugging mode')
        (options, args) = parser.parse_args()

        self.file = options.file
        self.verbose = options.verbose
        if self.verbose:
            LOG.enable_stdout_debug()
        if self.file is None:
            LOG.error("error: please provide the file name")
            parser.print_help()
        LOG.debug("hello")
main = Main(sys.argv)
