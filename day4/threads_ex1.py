#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
import threading
from my_devices import device_list as devices

def run_cmd(device, cmd=""):
    net_connect = ConnectHandler(**device)
    print()
    print('#' * 80)
    print(net_connect.send_command(cmd))
    print()
    print('#' * 80)
    print()

def main():
    for device in devices:
        thread = threading.Thread(target=run_cmd, args=(device, "show arp"))
        thread.start()
    main_thread = threading.currentThread()

    for a_thread in threading.enumerate():
        if a_thread != main_thread:
            a_thread.join()


if __name__ == '__main__':
    main()
