#!/usr/bin/python3

# Check if there is a device connected through bluetooth.

import pydbus

bus = pydbus.SystemBus()

adapter = bus.get('org.bluez', '/org/bluez/hci0')
mngr = bus.get('org.bluez', '/')

headset_name = 'WI-C200'


def list_connected_devices():
    mngd_objs = mngr.GetManagedObjects()
    for path in mngd_objs:
        con_state = mngd_objs[path].get(
            'org.bluez.Device1', {}).get('Connected', False)
        if con_state:
            addr = mngd_objs[path].get('org.bluez.Device1', {}).get('Address')
            name = mngd_objs[path].get('org.bluez.Device1', {}).get('Name')
            # print(f'Device {name} [{addr}] is connected')
            return name, addr


if __name__ == '__main__':
    name, addr = list_connected_devices()
    # print(f'{name} is connected\n')
    if (name == headset_name):
        print('Auris')
    elif (name != headset_name):
        print('BT')
    else:
        print('N/C')
