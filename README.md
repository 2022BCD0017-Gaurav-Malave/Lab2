# Lab 2: Automated Training and Metric Reporting Using GitHub Actions

## 📋 Project Overview

This project demonstrates automated machine learning workflows using GitHub Actions. The system automatically trains models, computes evaluation metrics, and stores artifacts whenever code is pushed to the repository.

## 🎯 Objectives

- Automate model training using CI/CD pipelines
- Track experiments through Git commit history
- Store models and results as workflow artifacts
- Display evaluation metrics in GitHub Actions Job Summary

## 📁 Project Structure

```
lab2/
├── dataset/
│   └── winequality-red.csv      # Wine Quality dataset
├── models/
│   └── model.pkl                 # Trained model (generated)
├── results/
│   └── results.json              # Evaluation metrics (generated)
├── .github/
│   └── workflows/
│       └── train.yml             # GitHub Actions workflow
├── train.py                      # Training script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/lab2.git
cd lab2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Dataset

Download the Wine Quality dataset from:
https://archive.ics.uci.edu/dataset/186/wine+quality

Save `winequality-red.csv` in the `dataset/` folder.

## 🔬 Running Experiments

Each experiment requires:
1. Modify `train.py` (change model, hyperparameters, preprocessing)
2. Commit changes with descriptive message
3. Push to GitHub to trigger automated training

### Example Experiments

**Experiment 1: Linear Regression (Baseline)**
```bash
# Already configured - just push
git add .
git commit -m "Experiment 1: Linear Regression baseline"
git push
```

**Experiment 2: Ridge Regression**
```python
# In train.py, change:
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.1)
```
```bash
git add train.py
git commit -m "Experiment 2: Ridge regression, alpha=0.1"
git push
```

**Experiment 3: Different Test Split**
```python
# In train.py, change:
test_size=0.3  # instead of 0.2
```
```bash
git add train.py
git commit -m "Experiment 3: Test split 0.3"
git push
```

## 📊 Viewing Results

1. Navigate to **Actions** tab in GitHub
2. Click on the latest workflow run
3. View **Job Summary** for metrics
4. Download artifacts from **Artifacts** section

## 🧪 Dataset Information

**Dataset:** Wine Quality Dataset (Red Wine)
- **Source:** UCI Machine Learning Repository
- **Samples:** ~1600 instances
- **Features:** 11 physicochemical properties
- **Target:** Wine quality (score 0-10)

### Features
- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol

## 📈 Evaluation Metrics

All experiments report:
- **Mean Squared Error (MSE):** Lower is better
- **Root Mean Squared Error (RMSE):** Lower is better
- **R² Score:** Higher is better (max 1.0)

## 🔧 Technologies Used

- **Python 3.10**
- **scikit-learn:** Machine learning models
- **pandas:** Data manipulation
- **numpy:** Numerical operations
- **GitHub Actions:** CI/CD automation

## 👨‍💻 Student Information

**Name:** [Your Name]
**Roll Number:** [Your Roll Number]

## 📝 Lab Questions

### Q1: How did GitHub Actions improve experiment reproducibility?
GitHub Actions ensures every experiment runs in an identical environment with the same dependencies, Python version, and execution steps.

### Q2: How easy was it to compare results across runs?
Results can be compared by viewing Job Summaries and downloading artifacts from each run, though manual comparison is required.

### Q3: What role does Git commit history play in experiment tracking?
Commit history serves as an experiment log, documenting what changed in each experiment and allowing us to revisit any previous configuration.

### Q4: What were the benefits compared to Lab 1?
- Automated execution
- Consistent environment
- Built-in version control
- Artifact storage
- Remote accessibility
- Team collaboration

### Q5: What limitations does this approach have?
- Manual code modifications required
- No automatic parameter optimization
- Results comparison not automated
- Git history cluttered with experiments
- Workflow execution time overhead

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Wine Quality Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality)

## 📄 License

This project is for educational purposes as part of Lab 2 coursework.

---

**Last Updated:** January 2026
