@echo off
REM setup.bat - Setup script for SNN2 project (Windows)

echo Setting up SNN2 project...

REM Check if model file exists
if not exist "spikingresformer_s.pth" (
    echo Model file 'spikingresformer_s.pth' not found.
    echo Please download or copy the model file to this directory.
    echo The model file should be approximately 204MB in size.
    echo.
    echo You can:
    echo 1. Copy it from your original location
    echo 2. Download it from your cloud storage
    echo 3. Train the model from scratch using the provided code
    echo.
) else (
    echo Model file found: spikingresformer_s.pth
)

REM Check Python dependencies
echo Checking Python environment...
python --version

echo Setup complete!
echo Your repository is ready to use on Kaggle or other cloud platforms.
pause
