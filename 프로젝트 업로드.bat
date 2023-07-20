@echo off
title 프로젝트 업로드 스크립트
git add -A
git commit -a -m "hotfix"
git push
echo 성공
pause
exit