@echo off
setlocal

python --version >nul 2>&1
if %errorlevel% neq 0 (
    curl -o python-installer.exe https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe

    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    del python-installer.exe

    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python installation failed. Exiting...
        exit /b 1
    ) else (
        echo Python installed successfully.
    )
)

pip install -r requirements.txt

python app/main.py

endlocal