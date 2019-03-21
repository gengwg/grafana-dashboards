#!/usr/bin/env python

import os
import sys

from jinja2 import Environment, FileSystemLoader

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

VER=7

#FC='atl1'
#SITE='8240'

#FC='lax1'
#SITE='8103'

#FC='ind1'
#SITE='6280'

#FC='gsp1'
#SITE='7031'

fc_site_pairs = [('gsp1', '7031'), ('lax1', '8103'), ('atl1', '8240'), ('ind1', '6280'), ('mco1', '7853'), ('phl1', '7356')]

def print_html_doc():
    # Create the jinja2 environment.

    for FC, SITE in fc_site_pairs:
        print "http://graf.wms.walmart.com/d/{}gc/".format(FC)

if __name__ == '__main__':
    #for fc, site in fc_site_pairs:
    #    print_html_doc(fc, site)
    print_html_doc()



