"""
two Cisco routers, four Arista switches, and Juniper SRX
"""
from getpass import getpass

pwd = getpass("Enter standard password")

pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'host': 'cisco1.twb-tech.com',
    'username': 'pyclass',
    'password': pwd,
}
pynet_rtr2 = {
    'device_type': 'cisco_ios',
    'host': 'cisco2.twb-tech.com',
    'username': 'pyclass',
    'password': pwd,
}

pynet_sw1 = {
    'device_type': 'arista_eos',
    'host': 'arista1.twb-tech.com',
    'username': 'pyclass',
    'password': pwd,
}
pynet_sw2 = {
    'device_type': 'arista_eos',
    'host': 'arista2.twb-tech.com',
    'username': 'pyclass',
    'password': pwd,
}
pynet_sw3 = {
    'device_type': 'arista_eos',
    'host': 'arista3.twb-tech.com',
    'username': 'pyclass',
    'password': pwd,
}
pynet_sw4 = {
    'device_type': 'arista_eos',
    'host': 'arista4.twb-tech.com',
    'username': 'pyclass',
    'password': pwd,
}

juniper_srx = {
    'device_type': 'juniper_junos',
    'host': 'srx1.twb-tech.com',
    'username': 'pyclass',
    'password': pwd,
}

device_list = [
    pynet_rtr1,
    pynet_rtr2,
    pynet_sw1,
    pynet_sw2,
    pynet_sw3,
    pynet_sw4,
    juniper_srx,
]
