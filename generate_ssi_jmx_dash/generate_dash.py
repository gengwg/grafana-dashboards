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

def get_services(FC):
    services = []
    with open('service_port_mapping_{}.txt'.format(FC)) as f:
        for line in f:
            services.append(line.split()[0])
    return services

#def print_html_doc(FC, SITE):
def print_html_doc():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)
    for FC, SITE in fc_site_pairs:
        output= j2_env.get_template('template.json').render(
            services=get_services(FC), fc=FC, site=SITE, ver=VER
            #services=get_services(), fc='ind1', site='6280', ver=7
            # services=['customerOrderService', 'webDialogPickModuleService']
        )

        with open("{}.json".format(FC), "w") as fh:
            fh.write(output)

if __name__ == '__main__':
    #for fc, site in fc_site_pairs:
    #    print_html_doc(fc, site)
    print_html_doc()



