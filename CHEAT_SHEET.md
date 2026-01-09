# Lab 2 - Quick Reference Cheat Sheet

## 🎯 Experiment Variations Guide

### Model Types

**1. Linear Regression (Baseline)**
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```

**2. Ridge Regression**
```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.1)  # Try: 0.01, 0.1, 1.0, 10.0
```

**3. Lasso Regression**
```python
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1)  # Try: 0.01, 0.1, 1.0
```

**4. ElasticNet**
```python
from sklearn.linear_model import ElasticNet
model = ElasticNet(alpha=0.1, l1_ratio=0.5)
```

### Preprocessing Options

**1. StandardScaler (Default)**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
```

**2. MinMaxScaler**
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
```

**3. RobustScaler**
```python
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
```

### Test Split Variations

```python
# In preprocess_data() function
test_size=0.2   # 80-20 split (default)
test_size=0.25  # 75-25 split
test_size=0.3   # 70-30 split
```

### Random State

```python
# For reproducibility
random_state=42  # default
random_state=123 # try different seeds
```

## 📝 Commit Message Examples

```bash
git commit -m "Experiment 1: LinearRegression baseline, test_split=0.2"
git commit -m "Experiment 2: Ridge, alpha=0.1, test_split=0.2"
git commit -m "Experiment 3: Ridge, alpha=1.0, test_split=0.2"
git commit -m "Experiment 4: Lasso, alpha=0.1, test_split=0.2"
git commit -m "Experiment 5: Lasso, alpha=0.1, test_split=0.3"
git commit -m "Experiment 6: Ridge, alpha=0.1, MinMaxScaler"
git commit -m "Experiment 7: ElasticNet, alpha=0.1, l1_ratio=0.5"
```

## 🔄 Git Workflow

```bash
# 1. Make changes to train.py
# 2. Stage changes
git add train.py

# 3. Commit with descriptive message
git commit -m "Experiment X: [description]"

# 4. Push to GitHub (triggers workflow)
git push

# 5. Check GitHub Actions tab for results
```

## 📊 Expected Metrics Range

For Wine Quality dataset:
- **MSE:** Typically between 0.3 - 0.6
- **RMSE:** Typically between 0.5 - 0.8
- **R² Score:** Typically between 0.25 - 0.45

Lower MSE/RMSE = Better
Higher R² = Better

## 🐛 Common Issues & Fixes

**Issue: Workflow doesn't trigger**
- Check file is in `.github/workflows/train.yml`
- Ensure you pushed to `main` branch
- Verify repository Actions are enabled

**Issue: Dataset not found**
- Ensure `winequality-red.csv` is in `dataset/` folder
- Check file name spelling (case-sensitive on Linux)
- Verify dataset is committed to repository

**Issue: Import errors**
- Check all imports are in `requirements.txt`
- Ensure correct package names and versions
- Review workflow logs for specific missing packages

**Issue: Artifacts not uploaded**
- Ensure `models/` and `results/` directories exist
- Check script completes without errors
- Verify files are created before artifact upload step

## ✅ Pre-Push Checklist

Before each push:
- [ ] Modified train.py with one change
- [ ] Tested locally with `python train.py`
- [ ] Wrote descriptive commit message
- [ ] Ready to wait for workflow completion (~2-3 minutes)

## 🎓 Recommended Experiment Sequence

1. **Baseline:** LinearRegression, StandardScaler, test_split=0.2
2. **Ridge variations:** Try alpha=0.01, 0.1, 1.0, 10.0
3. **Lasso variations:** Try alpha=0.01, 0.1, 1.0
4. **Test split:** Try 0.25, 0.3
5. **Different scaler:** Try MinMaxScaler, RobustScaler
6. **ElasticNet:** Try different alpha and l1_ratio combinations

Aim for at least 6-8 experiments minimum!

## 📸 Screenshot Requirements

Capture:
1. **Job Summary** - Shows metrics with your name/roll number
2. **Artifacts Section** - Shows downloadable model and results
3. **Actions Tab** - Shows all workflow runs
4. **Commit History** - Shows all experiment commits

## 💡 Pro Tips

- Run experiments in logical order (baseline first)
- Keep detailed notes of what you're testing
- Compare results as you go
- Look for patterns in how parameters affect metrics
- Don't change multiple things at once
- Wait for each workflow to complete before pushing next

---

Good luck! 🚀
