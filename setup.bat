@echo off
REM Lab 2 Setup Script for Windows
REM This script organizes all files into the correct directory structure

echo ================================================
echo Lab 2: Setting up project structure
echo ================================================

REM Create main directories
echo Creating directories...
if not exist "dataset\" mkdir dataset
if not exist "models\" mkdir models
if not exist "results\" mkdir results
if not exist ".github\" mkdir .github
if not exist ".github\workflows\" mkdir .github\workflows

REM Move .gitkeep files
echo Setting up empty directory tracking...
move /Y models_gitkeep.txt models\.gitkeep
move /Y results_gitkeep.txt results\.gitkeep

REM Move workflow file
echo Setting up GitHub Actions workflow...
move /Y train.yml .github\workflows\train.yml

REM Move .gitignore
echo Setting up .gitignore...
move /Y gitignore.txt .gitignore

echo.
echo ================================================
echo Project structure created successfully!
echo ================================================
echo.
echo Next steps:
echo 1. Download winequality-red.csv and place it in dataset\
echo 2. Update .github\workflows\train.yml with your name and roll number
echo 3. Initialize git repository:
echo    git init
echo    git add .
echo    git commit -m "Initial commit: Lab 2 setup"
echo 4. Add remote and push:
echo    git remote add origin https://github.com/^<your-username^>/lab2.git
echo    git push -u origin main
echo.
echo For detailed instructions, see LAB2_COMPLETE_GUIDE.md
echo For quick reference, see CHEAT_SHEET.md
echo ================================================
echo.
pause
