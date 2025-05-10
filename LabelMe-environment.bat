@echo off
echo Creating LabelMe environment...

conda create -n labelme_env python=3.9 -y
call conda activate labelme_env

pip install pyqt5==5.15.9
pip install labelme==5.2.1

echo ✅ LabelMe environment setup complete.
pause
