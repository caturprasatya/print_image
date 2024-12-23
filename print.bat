@echo off

echo Starting script execution...

echo Installing dependencies...
call pip install -r requirements.txt

:: Check if the file parameter is provided
if "%1"=="" (
    echo Error: No image file specified.
    echo Usage: print_image_batch.bat ^<path_to_image^>
    exit /b 1
)

:: Run the Python script
python print_image.py -f %1

:: Exit script
exit /b 0
