import os
from os import system
from os.path import isdir, join, isfile
import pdb
import argparse
home = '/home/local/USHERBROOKE/havm2701'
c3d = home + '/libs/c3d-1.0.0-Linux-x86_64/bin/./c3d'


def LoadPath(input):
    "WRITE SOME THING"
    path = input[0]
    
    list_dir = [join(path,join(d,f)) for d in os.listdir(path) if isdir(join(path,d)) for f in  os.listdir(join(path,d)) if 'N4ITK' in f and 'matched' not in f and 'mask' not in f and '.mha' in f]
    list_name = [f for d in os.listdir(path) if isdir(join(path,d)) for f in  os.listdir(join(path,d)) if 'N4ITK' in f and 'matched' not in f and 'mask' not in f and '.mha' in f]
    output = {}
    output['paths'] = {}
    output['name'] = input[1]
    for f,name in zip(list_dir,list_name):
    	if 'T1c' in name:
    		output['paths']['T1c'] = f
    	elif 'T2' in name:
    		output['paths']['T2'] = f
    	elif 'Flair' in name:
    		output['paths']['Flair'] = f
    	elif 'T1' in name:
    		output['paths']['T1'] = f
    return output					 

def HistogramMatching(input_brain,reference_brain):
	"WRITE SOME THING"
	input = input_brain['paths']
	brain_name = input_brain['name']
	reference = reference_brain['paths']
	reference_name = reference_brain['name']
	output= {}
	items = ['T1c','T2','T1','Flair']
	print 'Histogram of ' + brain_name + ' matching to ' + reference_name + ' ...'
	for item in items:
	
		output[item] = input[item].replace('.mha','matched.mha')
		command = c3d + ' ' + reference[item] + ' ' + input[item] + ' -histmatch 5 -o ' + output[item]
		system(command)
		print input[item]
		print 'matched to'
		print reference[item]

	return output	


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate the DICE score for a BrainSet')
	parser.add_argument('path', type=str)
	parser.add_argument('reference_path', type=str)
	args = parser.parse_args()
	mypath = args.path
	reference_path = args.reference_path

	#mypath = home + "/data/LeaderBoard/HG/"
	brains = {}
	brains= [(join(mypath,d),d) for d in os.listdir(mypath) if isdir(join(mypath,d))]
	#brains['names'] = [d for d in os.listdir(mypath) if isdir(join(mypath,d))]
	reference_brain = (reference_path, os.path.split(reference_path)[1])
	pdb.set_trace()
	reference = LoadPath(reference_brain)
	for brain in brains:
		print 'Processing ' + brain[0]
		modality_paths = LoadPath(brain)
		HistogramMatching(modality_paths,reference)
