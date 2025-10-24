# (Windows) เปิด Command Prompt หรือ PowerShell แล้วรันคำสั่งทีละบรรทัด:
cd /d D:\DjangoProject\venvKanitha\Scripts\KanithaProject
# ถ้ายังไม่ได้ activate venv:
# Windows PowerShell:
# .\..\Scripts\Activate.ps1
# หรือ CMD:
# ..\Scripts\activate.bat

python manage.py makemigrations student_data
python manage.py migrate
python manage.py runserver
