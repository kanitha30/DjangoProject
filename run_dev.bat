@echo off
rem หา manage.py ภายในโฟลเดอร์ D:\DjangoProject
set "ROOT=D:\DjangoProject"
set "VENV=%ROOT%\venvKanitha"
set "PY=%VENV%\Scripts\python.exe"
set "ACT=%VENV%\Scripts\activate.bat"
set "MG="

echo Searching for manage.py under %ROOT% ...
for /f "delims=" %%F in ('dir /s /b "%ROOT%\manage.py" 2^>nul') do (
	set "MG=%%F"
	goto :found_manage
)

echo manage.py not found under %ROOT%.
echo Please verify your Django project location.
goto :end

:found_manage
echo Found manage.py at: %MG%
if exist "%ACT%" (
	echo Activating virtualenv from %ACT% ...
	call "%ACT%"
) else (
	echo WARNING: activate script not found at %ACT% — ensure your venv path is correct.
)

if exist "%PY%" (
	echo Using Python: %PY%
	"%PY%" "%MG%" runserver
) else (
	echo WARNING: python.exe not found in venv at %PY%. Trying system python...
	python "%MG%" runserver
)

:end
