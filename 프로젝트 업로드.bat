@echo off
title 프로젝트 업로드 스크립트
git add -A
set /p commit_str=업로드할 메세지 입력: 
git commit -a -m "%commit_str%"
git push
echo 성공
pause
exit