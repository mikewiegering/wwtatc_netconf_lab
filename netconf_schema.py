#!/usr/bin/env python

import sys
import yaml
import xml.etree.ElementTree as ET

from ncclient import manager

def main(yang_module):
    # Load the device details from YAML file
    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    # Retrieve the model from the device
    with manager.connect(**device, hostkey_verify=False) as mgr:

        # retrieve the model
        schema = mgr.get_schema(yang_module).xml

        # save the model locally
        with open(yang_module +'.yang', 'w') as out:
            xml_root = ET.fromstring(schema)
            yang_content = list(xml_root)[0].text
            out.write(yang_content)

if __name__ == '__main__':
    main(sys.argv[1])