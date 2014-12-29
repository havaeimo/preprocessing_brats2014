import os 
#import sys
from os.path import join
from os.path import isdir
import pdb

pdb.set_trace()
list_dir = [d for d in os.listdir('.') if isdir(join('.',d))]

for name in list_dir:
    old_name = join('.',name)
    d_name = 'LG_' + name
    new_name = join('.',d_name)
    command = 'mv ' + old_name + ' ' + new_name
    os.system(command)