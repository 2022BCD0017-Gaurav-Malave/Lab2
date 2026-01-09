# 🚀 Quick Start Instructions for Lab 2

## Files Provided

I've created all the necessary files for your Lab 2 assignment:

### Core Files:
1. **train.py** - Complete training script with model training and evaluation
2. **requirements.txt** - Python dependencies
3. **train.yml** - GitHub Actions workflow file
4. **README.md** - Project documentation

### Setup Files:
5. **setup.sh** - Linux/Mac setup script
6. **setup.bat** - Windows setup script
7. **gitignore.txt** - Git ignore file (rename to .gitignore)
8. **models_gitkeep.txt** - For models/ directory (rename to .gitkeep)
9. **results_gitkeep.txt** - For results/ directory (rename to .gitkeep)

### Documentation:
10. **LAB2_COMPLETE_GUIDE.md** - Detailed step-by-step guide
11. **CHEAT_SHEET.md** - Quick reference for experiments
12. **ANALYSIS_ANSWERS.md** - Sample answers to lab questions

---

## 📥 What You Need to Do

### Step 1: Download Files (5 minutes)
Download all files from this conversation to your computer.

### Step 2: Setup Project Structure (10 minutes)

**Option A - Automatic Setup (Recommended):**

For Linux/Mac:
```bash
chmod +x setup.sh
./setup.sh
```

For Windows:
```cmd
setup.bat
```

**Option B - Manual Setup:**
```
Create this structure:
lab2/
├── dataset/
├── models/
│   └── .gitkeep
├── results/
│   └── .gitkeep
├── .github/
│   └── workflows/
│       └── train.yml
├── train.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Step 3: Download Dataset (5 minutes)
1. Go to: https://archive.ics.uci.edu/dataset/186/wine+quality
2. Download the red wine CSV file
3. Save as `winequality-red.csv` in the `dataset/` folder

### Step 4: Customize Workflow (2 minutes)
Open `.github/workflows/train.yml` and update:
```yaml
echo "**Name:** Your Name Here" >> $GITHUB_STEP_SUMMARY
echo "**Roll Number:** Your Roll Number Here" >> $GITHUB_STEP_SUMMARY
```

Replace with your actual name and roll number.

### Step 5: Create GitHub Repository (5 minutes)
1. Create GitHub account with format: `<roll_no>_<name>`
   Example: `2022bcs0123_benthomas`
2. Create new public repository named `lab2`

### Step 6: Push to GitHub (5 minutes)
```bash
cd lab2
git init
git add .
git commit -m "Initial commit: Lab 2 setup"
git branch -M main
git remote add origin https://github.com/<your-username>/lab2.git
git push -u origin main
```

### Step 7: Verify First Run (5 minutes)
1. Go to GitHub → Actions tab
2. Check the workflow run
3. Verify Job Summary shows metrics
4. Download artifacts to confirm they work

### Step 8: Run Experiments (30-60 minutes)
Follow the experiment guide in CHEAT_SHEET.md or LAB2_COMPLETE_GUIDE.md

Minimum 6 experiments suggested:
1. LinearRegression (baseline)
2. Ridge (alpha=0.1)
3. Ridge (alpha=1.0)
4. Lasso (alpha=0.1)
5. Lasso with test_split=0.3
6. Different scaler (MinMaxScaler)

### Step 9: Take Screenshots (10 minutes)
Capture:
- Job Summary with metrics (showing your name/roll number)
- Artifacts section showing downloadable files
- All workflow runs in Actions tab

### Step 10: Prepare Submission (20 minutes)
1. GitHub repository link
2. Screenshots
3. Answers to analysis questions (use ANALYSIS_ANSWERS.md as reference)

---

## ⚡ Fastest Path to Completion

```bash
# 1. Download all files to a folder named "lab2"
# 2. Run setup script (setup.sh or setup.bat)
# 3. Download dataset to dataset/ folder
# 4. Update train.yml with your name and roll number
# 5. Create GitHub repo and push:

git init
git add .
git commit -m "Initial commit: Lab 2 setup"
git branch -M main
git remote add origin https://github.com/<username>/lab2.git
git push -u origin main

# 6. For each experiment, modify train.py and push:

git add train.py
git commit -m "Experiment 2: Ridge, alpha=0.1"
git push

# 7. After all experiments, take screenshots and write answers
```

---

## 📚 Where to Find Help

- **Complete walkthrough:** LAB2_COMPLETE_GUIDE.md
- **Quick reference:** CHEAT_SHEET.md
- **Analysis help:** ANALYSIS_ANSWERS.md
- **Git issues:** Check README.md troubleshooting section

---

## ✅ Checklist

- [ ] All files downloaded
- [ ] Project structure created
- [ ] Dataset downloaded
- [ ] Workflow customized with your name/roll number
- [ ] GitHub repository created
- [ ] Initial commit pushed successfully
- [ ] First workflow run successful
- [ ] Job Summary displays correctly
- [ ] Artifacts downloadable
- [ ] 6+ experiments completed
- [ ] Screenshots captured
- [ ] Analysis questions answered

---

## 🆘 Common Issues

**"Dataset not found"**
- Check file is in `dataset/winequality-red.csv`
- Ensure folder and file names match exactly

**"Workflow doesn't trigger"**
- Verify file is in `.github/workflows/train.yml`
- Check you pushed to `main` branch
- Enable Actions in repository settings

**"Import errors"**
- Check requirements.txt is present
- Verify workflow installs dependencies step

**"Artifacts not uploaded"**
- Ensure models/ and results/ folders exist
- Check training script completes successfully

---

## 💡 Pro Tips

1. **Test locally first:** Run `python train.py` before pushing
2. **Read the logs:** If workflow fails, check the complete log
3. **One change at a time:** Don't modify multiple things per experiment
4. **Descriptive commits:** Help your future self understand what you tested
5. **Keep notes:** Document observations for analysis questions

---

## 🎯 Time Estimate

- **Setup:** 30-45 minutes
- **Experiments:** 30-60 minutes (depending on number)
- **Documentation:** 30-45 minutes
- **Total:** 2-3 hours

---

## 🏆 Success Criteria

You'll know you're successful when:
✅ GitHub Actions runs automatically on each push
✅ Job Summary shows your name and metrics
✅ Artifacts are downloadable
✅ You can compare results across experiments
✅ Git history shows all experiment commits
✅ You understand the benefits and limitations

---

**Ready to start? Open LAB2_COMPLETE_GUIDE.md for detailed instructions!**

Good luck! 🚀
