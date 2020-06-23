#!/user/bin/env python
import xmltodict
import yaml

from ncclient import manager

def main():
    with open('device.yml', 'r') as fp:
        device = yaml.safe_load(fp.read())

    with manager.connect(**device, hostkey_verify=False) as mgr:
        # Retrieve the configuration from the "running"
        # datastore using a get-config operation
        resp = mgr.get_config('running').xml

        # Load the xml response as a Python dict
        resp_dict = xmltodict.parse(resp)

        #extract the 'data' from the rpc-reply
        running_config = resp_dict['rpc-reply']['data']

        # save the running config locally
        hostname = running_config['native']['hostname']
        with open(hostname + '.runningconfig.xml', 'w') as fp:
            fp.write(resp)

        # display HTTP and HTTPS Server status from config
        ipsettings = running_config['native']['ip']
        print(f"hostname: {hostname}")
        print(f"/HTTP enabled: {ip_settings['http']['server']}")
        print(f"/HTTPS enabled: {ip_settings['http']['secure-server']}")

if __name__ == '__main__':
    main()

