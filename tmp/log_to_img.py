#!/usr/bin/env python3.5
# log_to_img.py, sceext test20161209 1449

import os, sys

def p_raw(lines):
    KEY = ' sceext: '
    BLOCK_SIZE = 256
    
    o = {}
    max_b = 0
    for i in lines:
        if KEY in i:
            p = i.split(KEY)
            one = p[-1].strip()
            j = int(p[0].rsplit('(', 1)[1].split(')', 1)[0])
            
            print('FIXME: j = ' + str(j) + ', len(one) == ' + str(len(one)))
            
            b = int(j / BLOCK_SIZE)
            o[b] = one
            if b > max_b:
                max_b = b
    
    ot = ''
    for i in range(max_b + 1):
        if not i in o:
            print('ERROR: missing block ' + str(i))
        else:
            ot += o[i]
    
    b = bytearray(int(len(ot) / 2))
    for i in range(0, len(ot), 2):
        a = ot[i:i + 2]
        b[int(i / 2)] = int(a, 16)
    return b


def main(args):
    file_name = args[0]
    
    with open(file_name, 'rt') as f:
        text = f.read()
    lines = text.splitlines()
    
    out = p_raw(lines)
    with open(file_name + '.img', 'wb') as f:
        f.write(out)

if __name__ == '__main__':
    main(sys.argv[1:])

# end log_to_img.py


