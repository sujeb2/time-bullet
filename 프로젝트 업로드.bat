@echo off
title 프로젝트 업데이트 스크립트
git add -A
git commit -a -m "Pull Request by someone"
git push
echo 성공
pause
exit