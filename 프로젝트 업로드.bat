@echo off
title ������Ʈ ���ε� ��ũ��Ʈ
git add -A
set /p commit_str=���ε��� �޼��� �Է�: 
git commit -a -m "%commit_str%"
git push
echo ����
pause
exit