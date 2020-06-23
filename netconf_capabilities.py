#! /user/bin/env python

from ncclient import manager

device = {
    'host' : 'r1.lab.local',
    'username' : 'wwt',
    'password' : 'WWTwwt1!',
    'port' : 830
}

def main():
    # Connect to the device using the manager object
    mgr = manager.connect(
      host=device['host'],
      username=device['username'],
      password=device['password'],
      port=device['port'],
      hostkey_verify=False
    )

    # Display Capabilities advertised by the device(server)
    with manager.connect(**device, hostkey_verify=False) as mgr:
        for capability in mgr.server_capabilities:
            print(capability)

    # close the netconf session
    # mgr.close_session()


if __name__ == '__main__':
    main()