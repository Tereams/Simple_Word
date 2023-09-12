@echo off

rem 设置虚拟环境路径
set VENV_PATH=E:\class\AI\venv

rem 切换到虚拟环境
call %VENV_PATH%\Scripts\activate.bat

rem 运行你的程序
python window.py

rem 退出虚拟环境
deactivate