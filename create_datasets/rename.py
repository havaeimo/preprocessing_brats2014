import os 
#import sys
from os.path import join
from os.path import isdir
import pdb

'''
This script changes the directory name from 000x to HG_000x. you can also change the HG to LG to preform the same process on LG dicrectories
'''

pdb.set_trace()
list_dir = [d for d in os.listdir('.') if isdir(join('.',d))]

for name in list_dir:
    old_name = join('.',name)
    d_name = 'HG_' + name
    new_name = join('.',d_name)
    command = 'mv ' + old_name + ' ' + new_name
    os.system(command)
