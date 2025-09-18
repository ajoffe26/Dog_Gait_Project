@echo off
pushd %~dp0\..
call .venv\Scripts\activate.bat
%*
popd
