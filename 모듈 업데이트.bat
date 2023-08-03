@echo off
title 모듈 업데이트 스크립트
set /p link=requirements.txt 파일위치:  
pip install -r %link%
echo pip 업그레이드 중
python.exe -m pip install --upgrade pip
echo 성공
pause
exit