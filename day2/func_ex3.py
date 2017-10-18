from __future__ import print_function

def read_file(file_name):
    with open(file_name) as f:
        output = f.read()
    return output

def get_serial(output):
    lines = output.splitlines()

    for line in lines:
        if 'Processor board ID' in line:
            words = line.strip().split('Processor board ID ')
            sn = words[-1]

    return sn
