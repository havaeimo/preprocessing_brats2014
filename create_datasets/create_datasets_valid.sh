#!/bin/bash

python /share/home3/brats/libs/lisa_brats/brains.py -r LG_brats_tcia_pat393_1 brats_tcia_pat370_4 brats_tcia_pat111_1 brats_tcia_pat221_1 brats_tcia_pat444_6 brats_tcia_pat234_1 LG_brats_2013_pat0001_1 brats_tcia_pat280_1 brats_tcia_pat455_1 brats_2013_pat0015_1 brats_tcia_pat396_3 brats_tcia_pat437_3 brats_tcia_pat444_3 brats_tcia_pat391_3 brats_tcia_pat399_7 brats_tcia_pat198_2 brats_tcia_pat399_6 brats_tcia_pat260_5 brats_tcia_pat401_1 brats_tcia_pat260_11 LG_brats_tcia_pat254_1 brats_tcia_pat171_1 brats_tcia_pat368_1 brats_tcia_pat377_1 brats_tcia_pat231_1 brats_tcia_pat133_1 brats_tcia_pat370_9 brats_tcia_pat368_2 brats_tcia_pat290_6 LG_brats_tcia_pat410_1 LG_brats_tcia_pat109_2 -O new_preprocessed_2014_BRAINS_VALID > out1_valid.log

#python /share/home3/brats/libs/lisa_brats/scripts/brains_analysis4.py --brains-archive new_preprocessed_2014_BRAINS_VALID --out-brains-temp Analysis_VALID_TEMP > out2_valid.log

#python /share/home3/brats/libs/lisa_brats/scripts/brains_analysis_randomizing.py --brains-analysis-temp Analysis_VALID_TEMP --out-brains-analysis new_preprocessed_2014_ANALYSIS_VALID > out3_valid.log
