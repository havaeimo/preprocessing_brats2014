#!/bin/bash 
python /share/home3/brats/libs/lisa_brats/brains.py -r LG_0001 LG_0002 LG_0004 LG_0006 LG_0008 HG_0012 HG_0010 HG_0015 LG_0014 LG_0015 LG_0012 LG_0013 LG_0011 HG_0005 HG_0004 HG_0007 HG_0001 HG_0003 HG_0002 HG_0009 HG_0008 HG_0022 HG_0025 HG_0024 -O new_2013_DATASET_BRAINS_TRAIN > out1.log 

python /share/home3/brats/libs/lisa_brats/brains.py -r HG_0013 HG_0006 HG_0014 HG_0011 HG_0027 HG_0026 -O new_2013_DATASET_BRAINS_VALID > out2.log 


python /share/home3/brats/libs/lisa_brats/brains.py -r HG_0301 HG_0302 HG_0303 HG_0304 HG_0305 HG_0306 HG_0307 HG_0308 HG_0309 HG_0310 -O new_2013_DATASET_BRAINS_CHALLENGE > out2.log 

python /share/home3/brats/libs/lisa_brats/scripts/brains_analysis2.py --brains-archive new_2013_DATASET_BRAINS_TRAIN --out-brains-analysis new_2013_DATASET_ANALYSIS_TRAIN  > out3.log 


python /share/home3/brats/libs/lisa_brats/scripts/brains_analysis2.py --brains-archive new_2013_DATASET_BRAINS_VALID --out-brains-analysis new_2013_DATASET_ANALYSIS_VALID  > out4.log 