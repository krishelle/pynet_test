from __future__ import print_function

net_devices = {'ip_addr': '10.10.10.10', 'password': 'mypass', 'username': 'khardson', 'vendor': 'junos', 'model': '209'}

for key, val in net_devices.items():
    print(key, val)

net_devices['password'] = 'newpass'
net_devices['secret'] = 'shhhhhhh'
new_key = net_devices.get('device_type', 'cisco_ios')

print(net_devices)
print('my new key is {}'.format(new_key))
