import os
from os import system
from os.path import isdir, join, isfile
import pdb
import argparse
home = '/home/local/USHERBROOKE/havm2701'
c3d = home + '/libs/c3d-1.0.0-Linux-x86_64/bin/./c3d'


def LoadPath(path):
    "WRITE SOME THING"

    list_dir = [join(path,join(d,f)) for d in os.listdir(path) if isdir(join(path,d)) for f in  os.listdir(join(path,d)) if 'N4ITK' in f and 'mask' not in f and '.mha' in f and 'matched' not in f]
    list_name = [f for d in os.listdir(path) if isdir(join(path,d)) for f in  os.listdir(join(path,d)) if 'N4ITK' in f and 'mask' not in f and '.mha' in f and 'matched' not in f]
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
    return path					 

def Convert_mha2nii(input):
	"WRITE SOME THING"

	output= {}
	items = ['T1c','T2','T1','Flair']
	
	for item in items:
		output[item] = input[item].replace('mha','nii.gz')
		command = c3d + ' ' + input[item] + ' -o ' + output[item]
		system(command)

	return output	

def Get_csf_mask(input,output):
	"WRITE SOME THING"

	command = '/usr/local/fsl/bin/fast -S 4 -n 3 -H 0.7 -I 4 -l 20.0 -o ' + output + ' ' + input['Flair'] + ' ' + input['T2'] + ' ' +input['T1c'] + ' ' +input['T1']
	#command = '/usr/local/fsl/bin/fast -S 3 -n 3 -H 0.3 -I 4 -l 20.0 -o ' + output + ' ' + input['Flair'] + ' ' + input['T2'] + ' ' +input['T1c']
	
	system(command)
	mask_path = output + '_pve_0.nii.gz'
	return mask_path


def Convert_nii2mha(input):
	"WRITE SOME THING"

	output1 = input.replace('_pve_0.nii.gz','_pre_csf_mask.mha')
	output2 = input.replace('_pve_0.nii.gz','_csf_mask.mha')
	command1 = c3d + ' ' + input + ' -o ' + output1
	
	system(command1)
	command2 = c3d + ' ' + output1 + ' -shift  1  -o ' + output2
	system(command2)
	
	os.remove(output1)
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate the DICE score for a BrainSet')
	parser.add_argument('path', type=str)
	args = parser.parse_args()
	mypath = args.path

	#mypath = home + "/data/LeaderBoard/HG/"
	brains = {}
	brains['paths'] = [join(mypath,d) for d in os.listdir(mypath) if isdir(join(mypath,d))]
	brains['names'] = [d for d in os.listdir(mypath) if isdir(join(mypath,d))]

	for path,name in zip(brains['paths'],brains['names']):
		print 'Processing ' + name
		mask_basename = path + '/' + name + '_processed'
		modality_paths = LoadPath(path)
		nii_modality_paths = Convert_mha2nii(modality_paths)
		mask_path = Get_csf_mask(nii_modality_paths,mask_basename)
		Convert_nii2mha(mask_path)
		


