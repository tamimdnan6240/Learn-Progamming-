conda create -n labelme_env python=3.9 -y
conda activate labelme_env

pip install pyqt5==5.15.9
pip install labelme==5.2.1

## use the following lines for LabelMe task. 
## conda activate labelme_env
## python LabelMe_guide_Tamim.py

## Call LabelME GUI Script
labelme

