@echo off
title ��� ������Ʈ ��ũ��Ʈ
set /p link=requirements.txt ������ġ:  
pip install -r %link%
echo pip ���׷��̵� ��
python.exe -m pip install --upgrade pip
echo ����
pause
exit