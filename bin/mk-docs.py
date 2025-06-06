#!/usr/bin/env python3

import os
import sys
import json
import datetime
import logging

if __name__ == '__main__':

    import optparse
    opt_parser = optparse.OptionParser()
        
    opt_parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Be chatty (default is false)')
    options, args = opt_parser.parse_args()
    
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    whoami = sys.argv[0]
    whoami = os.path.abspath(whoami)

    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    docs_json = os.path.join(root, "docs.json")
    docs_md = os.path.join(root, "DOCS.md")    

    fh_json = open(docs_json, "r")
    fh_md = open(docs_md, "w")    
    
    dt = datetime.date.today()
    ymd = dt

    fh_md.write("## Documentation\n\n")    
    fh_md.write("_This section was generated [by robots](bin/mk-docs.py) on %s, derived from the [docs.json](docs.json) file_\n\n" % (ymd))

    docs = json.load(fh_json)

    for details in docs:
        
        fh_md.write("### %s\n\n" % details['name'])

        fh_md.write("%s\n\n" % details['description'])
        fh_md.write("* %s\n\n" % details['url'])

