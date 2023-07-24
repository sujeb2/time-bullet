@echo off
title 모듈 업데이트
set /p link=requirements.txt 파일 위치 입력: 
pip install -r %link%
echo 성공
pause
exit