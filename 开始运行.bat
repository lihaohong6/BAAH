@echo off

rem 获取当前命令执行地址
cd
echo Current working directory: %cd%

rem 获取批处理文件所在的目录
set "scriptDirectory=%~dp0"

rem 构建Python可执行文件路径
set "pythonExecutable=%scriptDirectory%tools\python3.10\python.exe"

rem 要运行的Python脚本的路径
set "pythonScript=%scriptDirectory%main.py"

rem 使用python命令运行Python脚本
"%pythonExecutable%" "%pythonScript%"

rem 暂停，以便在执行完成后查看输出，可选步骤
pause
