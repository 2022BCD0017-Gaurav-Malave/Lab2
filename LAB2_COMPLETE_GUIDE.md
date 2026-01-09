# Lab 2: Complete Step-by-Step Guide
## Automated Training and Metric Reporting Using GitHub Actions

---

## Overview
This lab teaches you to automate ML workflows using GitHub Actions. You'll train models automatically on every push and track experiments through Git commits.

---

## Step 1: Create GitHub Account and Repository

### 1.1 Create GitHub Account
- Go to https://github.com
- Sign up with username format: `<roll_no>_<name>` (e.g., `2022bcs0123_benthomas`)
- Use your institute email ID

### 1.2 Create Repository
1. Click the "+" icon → "New repository"
2. Name: `lab2`
3. Set to **Public**
4. Initialize with README (optional)
5. Click "Create repository"

---

## Step 2: Set Up Local Project Structure

Create the following folder structure on your computer:

```
lab2/
├── dataset/
│   └── winequality-red.csv
├── models/
│   └── .gitkeep
├── results/
│   └── .gitkeep
├── .github/
│   └── workflows/
│       └── train.yml
├── train.py
├── requirements.txt
└── README.md
```

---

## Step 3: Download Dataset

1. Download the Wine Quality dataset from:
   https://archive.ics.uci.edu/dataset/186/wine+quality
2. Download the red wine CSV file
3. Save it as `winequality-red.csv` in the `dataset/` folder

---

## Step 4: Create Project Files

I've created all necessary files for you. You'll need to copy them to your local repository.

### Files Created:
1. **train.py** - Training script with model training and evaluation
2. **requirements.txt** - Python dependencies
3. **.github/workflows/train.yml** - GitHub Actions workflow
4. **.gitkeep files** - To track empty directories
5. **README.md** - Project documentation

---

## Step 5: Initialize Git and Push to GitHub

Open terminal/command prompt in your `lab2` folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit with message
git commit -m "Initial commit: Lab 2 setup"

# Add remote repository (replace with your username)
git remote add origin https://github.com/<your_username>/lab2.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 6: Run Experiments

For each experiment, you'll modify `train.py` and push changes:

### Experiment 1: Linear Regression (Baseline)
Already set up in the initial train.py file. Just push to trigger the workflow.

### Experiment 2: Ridge Regression (alpha=0.1)
1. Open `train.py`
2. Find the line: `model = LinearRegression()`
3. Replace with: `model = Ridge(alpha=0.1)`
4. Find: `from sklearn.linear_model import LinearRegression`
5. Replace with: `from sklearn.linear_model import Ridge`
6. Commit and push:
```bash
git add train.py
git commit -m "Experiment 2: Ridge regression, alpha=0.1"
git push
```

### Experiment 3: Ridge Regression (alpha=1.0)
1. Change `model = Ridge(alpha=0.1)` to `model = Ridge(alpha=1.0)`
2. Commit and push:
```bash
git add train.py
git commit -m "Experiment 3: Ridge regression, alpha=1.0"
git push
```

### Experiment 4: Lasso Regression (alpha=0.1)
1. Replace Ridge with Lasso
2. Change import: `from sklearn.linear_model import Lasso`
3. Change model: `model = Lasso(alpha=0.1)`
4. Commit and push:
```bash
git add train.py
git commit -m "Experiment 4: Lasso regression, alpha=0.1"
git push
```

### Experiment 5: Different Test Split (0.3)
1. Find: `test_size=0.2`
2. Replace with: `test_size=0.3`
3. Commit and push:
```bash
git add train.py
git commit -m "Experiment 5: Lasso, alpha=0.1, test_split=0.3"
git push
```

### Experiment 6: Different Scaler (MinMaxScaler)
1. Find: `from sklearn.preprocessing import StandardScaler`
2. Replace with: `from sklearn.preprocessing import MinMaxScaler`
3. Find: `scaler = StandardScaler()`
4. Replace with: `scaler = MinMaxScaler()`
5. Commit and push:
```bash
git add train.py
git commit -m "Experiment 6: MinMaxScaler preprocessing"
git push
```

---

## Step 7: View Results

After each push:

1. Go to your GitHub repository
2. Click on "Actions" tab
3. Click on the latest workflow run
4. View the **Job Summary** to see metrics
5. Scroll down to **Artifacts** section
6. Download artifacts to verify model and results files

---

## Step 8: Take Screenshots

For your submission, capture:

1. **Job Summary Screenshot**: Show the summary with your name, roll number, and metrics
2. **Artifacts Screenshot**: Show the downloadable artifacts section
3. **Multiple Runs**: Show all experiment runs in the Actions tab

---

## Step 9: Answer Analysis Questions

### Question 1: How did GitHub Actions improve experiment reproducibility?
**Answer**: GitHub Actions creates a consistent, automated environment for every experiment. Each run uses the same Python version, dependencies, and execution steps defined in the workflow. This eliminates "works on my machine" problems and ensures anyone can reproduce the exact same results by checking out the same commit.

### Question 2: How easy was it to compare results across runs?
**Answer**: Comparing results is relatively easy because:
- Each run's metrics appear in the Job Summary
- Artifacts are stored separately for each run
- Commit messages help identify what changed
However, you need to manually open each run to compare metrics - there's no automatic comparison dashboard.

### Question 3: What role does Git commit history play in experiment tracking?
**Answer**: Git commit history serves as an experiment log:
- Each commit represents one experiment configuration
- Commit messages document what was changed (model type, hyperparameters, etc.)
- You can trace back to any experiment by checking out its commit
- The history provides a chronological record of all experiments tried
This makes it easy to revisit previous configurations or understand the evolution of experiments.

### Question 4: What were the benefits compared to Lab 1?
**Answer**: 
- **Automation**: No need to manually run training scripts
- **Consistency**: Same environment for every run
- **Traceability**: Every experiment is tied to a Git commit
- **Artifact Storage**: Models and results automatically saved
- **Remote Execution**: Can trigger experiments from anywhere
- **Version Control**: Easy to revert to previous configurations
- **Collaboration**: Team members can see all experiments

### Question 5: What limitations does this approach have?
**Answer**:
- **Manual Code Changes**: Still need to edit code for each experiment (tedious and error-prone)
- **No Parameter Visualization**: Can't easily visualize how different parameters affect metrics
- **Limited Comparison**: Need to manually open each run to compare
- **No Automatic Optimization**: Can't automatically search for best parameters
- **Workflow Time**: Need to wait for CI/CD pipeline to complete
- **Git Pollution**: Many commits for parameter changes clutters history
- **No Experiment Database**: Results aren't stored in a queryable format

---

## Submission Checklist

- [ ] GitHub repository link
- [ ] Screenshot showing Job Summary with metrics for all experiments
- [ ] Screenshot showing downloadable artifacts
- [ ] Answers to all 5 analysis questions
- [ ] Repository is public and accessible

---

## Troubleshooting

### Workflow doesn't trigger
- Check that the workflow file is in `.github/workflows/`
- Ensure you pushed to the `main` branch
- Check the Actions tab for any errors

### Workflow fails
- Check the workflow logs for error messages
- Ensure dataset file exists in the correct location
- Verify requirements.txt has all dependencies

### No artifacts
- Check that the `models/` and `results/` directories exist
- Ensure the training script completes successfully
- Verify artifact paths in the workflow match actual file locations

---

## Tips for Success

1. **Test Locally First**: Run `python train.py` locally before pushing to ensure it works
2. **Meaningful Commits**: Use descriptive commit messages for each experiment
3. **Check Logs**: If workflow fails, read the complete log to identify issues
4. **Small Changes**: Change one thing at a time between experiments
5. **Document**: Keep notes on what you're testing in each experiment

---

## Additional Resources

- GitHub Actions Documentation: https://docs.github.com/en/actions
- Scikit-learn Documentation: https://scikit-learn.org/
- Git Basics: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics

---

Good luck with your lab! 🚀
