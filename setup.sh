#!/bin/bash

# Lab 2 Setup Script
# This script organizes all files into the correct directory structure

echo "================================================"
echo "Lab 2: Setting up project structure"
echo "================================================"

# Create main directories
echo "Creating directories..."
mkdir -p dataset
mkdir -p models
mkdir -p results
mkdir -p .github/workflows

# Move .gitkeep files
echo "Setting up empty directory tracking..."
mv models_gitkeep.txt models/.gitkeep
mv results_gitkeep.txt results/.gitkeep

# Move workflow file
echo "Setting up GitHub Actions workflow..."
mv train.yml .github/workflows/train.yml

# Move .gitignore
echo "Setting up .gitignore..."
mv gitignore.txt .gitignore

# Display structure
echo ""
echo "================================================"
echo "Project structure created successfully!"
echo "================================================"
echo ""
echo "Directory structure:"
tree -L 2 -a 2>/dev/null || find . -maxdepth 2 -not -path '*/\.*' | sed 's|[^/]*/| |g'

echo ""
echo "================================================"
echo "Next steps:"
echo "================================================"
echo "1. Download winequality-red.csv and place it in dataset/"
echo "2. Update train.yml with your name and roll number"
echo "3. Initialize git repository:"
echo "   git init"
echo "   git add ."
echo "   git commit -m 'Initial commit: Lab 2 setup'"
echo "4. Add remote and push:"
echo "   git remote add origin https://github.com/<your-username>/lab2.git"
echo "   git push -u origin main"
echo ""
echo "For detailed instructions, see LAB2_COMPLETE_GUIDE.md"
echo "For quick reference, see CHEAT_SHEET.md"
echo "================================================"
