import os
from os import system
from os.path import isdir, join, isfile
import pdb
import argparse
home = '/home/local/USHERBROOKE/havm2701'
c3d = home + '/libs/c3d-1.0.0-Linux-x86_64/bin/./c3d'


def LoadPath(path,basename):
    "WRITE SOME THING"

    list_dir = [join(path,join(d,f)) for d in os.listdir(path) if isdir(join(path,d)) for f in  os.listdir(join(path,d)) if basename in f ]
    list_name = [f for d in os.listdir(path) if isdir(join(path,d)) for f in  os.listdir(join(path,d)) if basename in f]
    path = {}
    for f,name in zip(list_dir,list_name):
    	if 'T1c' in name:
    		path['T1c'] = f
    	elif 'T2' in name:
    		path['T2'] = f
    	elif 'Flair' in name:
    		path['Flair'] = f
    	elif 'T1' in name:
    		path['T1'] = f
    	else:
    		print 'file does not exist for '+name
    		path = NaN	
    return path					 


def remove_file(input):
	"WRITE SOME THING"

	if input == {}:
		print 'File does not exit'
		return 0 
		
	items = ['T1c','T2','T1','Flair']
	
	for item in items:
		os.remove(input[item])	



	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate the DICE score for a BrainSet')
	parser.add_argument('path', type=str)
	parser.add_argument('basename', type=str)
	args = parser.parse_args()
	mypath = args.path
	basename = args.basename
	brains = {}
	brains['paths'] = [join(mypath,d) for d in os.listdir(mypath) if isdir(join(mypath,d))]
	brains['names'] = [d for d in os.listdir(mypath) if isdir(join(mypath,d))]

	for path,name in zip(brains['paths'],brains['names']):
		print 'Processing ' + name
		mask_basename = path + '/' + name + '_processed'
		modality_paths = LoadPath(path,basename)
		remove_file(modality_paths)
		
		


