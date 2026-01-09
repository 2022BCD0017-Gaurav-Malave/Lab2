# Lab 2: Analysis Questions - Sample Answers

**Student Name:** [Your Name]  
**Roll Number:** [Your Roll Number]  
**Date:** January 2026

---

## Question 1: How did GitHub Actions improve experiment reproducibility?

### Answer:

GitHub Actions significantly improved experiment reproducibility in the following ways:

**1. Consistent Environment:**
Every experiment runs in a fresh Ubuntu environment with the same:
- Python version (3.10)
- Package versions (from requirements.txt)
- System dependencies
- Operating system configuration

This eliminates the "works on my machine" problem where experiments produce different results on different computers.

**2. Automated Execution:**
The workflow file defines exact steps that execute identically every time:
- Checkout code
- Install dependencies
- Run training script
- Save artifacts

There's no room for human error in manual execution steps.

**3. Version Control Integration:**
Every experiment is tied to a specific Git commit, allowing us to:
- Reproduce any experiment by checking out that commit
- See exactly what code produced what results
- Track changes between experiments

**4. Documentation:**
The Job Summary automatically documents:
- When the experiment ran
- What metrics were achieved
- What artifacts were produced
- Which commit triggered it

This creates an automatic experiment log without manual record-keeping.

**5. Artifact Preservation:**
Models and results are automatically saved and downloadable, ensuring results are preserved even if local files are lost.

**Impact:** Any team member or evaluator can reproduce exact results by checking out a specific commit and viewing its workflow run, making the research fully transparent and verifiable.

---

## Question 2: How easy was it to compare results across runs?

### Answer:

**Moderate Difficulty** - The comparison process has both strengths and weaknesses.

**What Made It Easy:**

1. **Centralized Location:** All experiments are in one place (Actions tab) with clear run numbers and timestamps

2. **Structured Metrics Display:** Job Summary presents metrics in a consistent table format, making it easy to read individual results

3. **Commit Messages:** Descriptive commit messages help identify what each experiment tested

4. **Artifacts:** Can download and compare detailed results files

**What Made It Difficult:**

1. **No Side-by-Side Comparison:** Must open each run in a separate tab to compare metrics - GitHub doesn't provide a comparison dashboard

2. **Manual Process:** Need to manually note down metrics or switch between tabs repeatedly

3. **No Visualization:** No graphs or charts showing how metrics changed across experiments

4. **No Sorting/Filtering:** Cannot sort runs by metric values (e.g., "show best R² score")

**Comparison Workflow Used:**
```
1. Open Actions tab
2. Open first experiment in new tab
3. Open second experiment in another tab
4. Manually compare metrics
5. Repeat for all experiments
6. Create own spreadsheet to track results
```

**Conclusion:** While not impossible, comparing results requires significant manual effort. A dedicated ML experiment tracking tool would make this much easier.

---

## Question 3: What role does Git commit history play in experiment tracking?

### Answer:

Git commit history serves as the **experiment journal** for this workflow. It plays several critical roles:

**1. Experiment Identifier:**
Each commit uniquely identifies one experiment configuration:
```
commit abc123 → Experiment 1: LinearRegression
commit def456 → Experiment 2: Ridge, alpha=0.1
commit ghi789 → Experiment 3: Ridge, alpha=1.0
```

**2. Change Documentation:**
Commit messages document what changed between experiments:
- Which model was used
- What hyperparameters were set
- What preprocessing was applied
- What data split was used

Example: `"Experiment 5: Lasso, alpha=0.1, test_split=0.3"`

**3. Time-Ordered Log:**
Commits create a chronological record showing:
- The sequence of experiments
- When each was conducted
- The evolution of our approach

**4. Code State Preservation:**
Each commit preserves the exact code that produced specific results:
- Can checkout any commit to see exact configuration
- Can rerun any experiment by checking out its commit
- No ambiguity about "what did I change?"

**5. Reproducibility Gateway:**
To reproduce experiment N:
```bash
git checkout <commit-hash>
git push  # Triggers workflow with exact same code
```

**6. Experiment Lineage:**
Git history shows experiment relationships:
- Which experiments built on previous ones
- What hypotheses were tested in sequence
- How strategy evolved based on results

**Example Scenario:**
If we achieved good results in commit xyz789 but later experiments performed worse, we can:
1. View the commit: `git show xyz789`
2. See exactly what was different
3. Revert or incorporate those changes
4. Understand why it worked

**Limitation:** Commit history only tracks code changes, not why decisions were made or observations during experiments - this requires additional documentation.

**Conclusion:** Git commit history transforms version control into experiment tracking, providing traceability and reproducibility that manual logs can't match.

---

## Question 4: What were the benefits of this approach compared to Lab 1?

### Answer:

**Major Improvements Over Lab 1:**

**1. Automation vs Manual Execution**

*Lab 1:*
- Manually run Python scripts
- Remember to save results
- Risk of forgetting steps

*Lab 2:*
- Automatic execution on push
- Consistent process every time
- No steps forgotten

**2. Environment Consistency**

*Lab 1:*
- Results vary by machine
- Dependency conflicts possible
- "Works on my machine" syndrome

*Lab 2:*
- Same environment every time
- Fresh install per run
- Reproducible across machines

**3. Result Storage**

*Lab 1:*
- Manual file management
- Easy to overwrite results
- No automatic backup

*Lab 2:*
- Automatic artifact storage
- Each run preserved separately
- Downloadable from GitHub

**4. Experiment Tracking**

*Lab 1:*
- Manual notes or spreadsheet
- Easy to lose track
- Hard to remember what changed

*Lab 2:*
- Git commits track changes
- Automatic experiment log
- Clear history of all runs

**5. Collaboration**

*Lab 1:*
- Hard to share results
- Difficult for others to reproduce
- Results stay local

*Lab 2:*
- All results on GitHub
- Anyone can view and reproduce
- Public record of work

**6. Traceability**

*Lab 1:*
- Loose connection between code and results
- Which code produced which results?

*Lab 2:*
- Direct link: commit → workflow run → results
- Perfect traceability

**7. Professional Workflow**

*Lab 1:*
- Ad-hoc process
- Not industry standard

*Lab 2:*
- CI/CD pipeline
- Mirrors professional ML workflows
- Scalable approach

**Quantitative Benefits:**

| Aspect | Lab 1 | Lab 2 |
|--------|-------|-------|
| Setup Time | 5 min | 30 min (one-time) |
| Per-Experiment Time | 5 min | 2 min + 2 min wait |
| Reproducibility | Low | High |
| Collaboration | Difficult | Easy |
| Result Preservation | Manual | Automatic |
| Environment Issues | Common | Rare |

**Conclusion:** Lab 2's automated approach requires more initial setup but provides significantly better reproducibility, traceability, and collaboration capabilities - essential for professional ML work.

---

## Question 5: What limitations does this approach have?

### Answer:

Despite improvements, this approach has several significant limitations:

**1. Manual Code Modification**

*Problem:* Must manually edit code for each experiment
- Tedious and time-consuming
- Error-prone (typos, forgot to change all places)
- Clutters codebase with experiment-specific code

*Example:* To test 10 alpha values, need 10 code changes and commits

*Better Approach:* Configuration files or command-line parameters

**2. Git History Pollution**

*Problem:* Experiment commits clutter Git history
- Makes real development changes hard to find
- Not suitable for production code
- Mixing experimentation with development

*Example:* 50 experiment commits vs 5 actual feature commits

*Better Approach:* Separate experiment tracking system

**3. No Automatic Optimization**

*Problem:* Cannot automatically find best hyperparameters
- Must manually decide what to try next
- No systematic parameter search
- Inefficient exploration of parameter space

*Better Approach:* Hyperparameter tuning tools (GridSearch, Optuna)

**4. Limited Comparison Capabilities**

*Problem:* Difficult to compare experiments
- No built-in comparison dashboard
- Must manually track metrics
- Cannot visualize trends

*Example:* Want to see "how does R² change with alpha?" - must manually plot

*Better Approach:* MLflow, Weights & Biases dashboards

**5. Workflow Execution Time**

*Problem:* Must wait for CI/CD pipeline
- 2-3 minutes per experiment
- Cannot run multiple experiments in parallel easily
- Slower than local execution

*Better Approach:* Local parallel execution with cloud logging

**6. No Experiment Relationships**

*Problem:* Cannot express experiment dependencies
- "This experiment builds on Experiment 3"
- No way to mark baseline vs variant
- No experiment hierarchy

*Better Approach:* Dedicated experiment tracking with parent/child relationships

**7. Limited Metadata**

*Problem:* Only code and metrics stored
- No hypothesis documentation
- No failure reason tracking
- No notes or observations

*Better Approach:* Experiment notes, tags, descriptions

**8. No Data Versioning**

*Problem:* Dataset not versioned with code
- If dataset changes, hard to know which data produced which results
- Cannot track data preprocessing experiments

*Better Approach:* DVC (Data Version Control)

**9. Artifact Management**

*Problem:* Artifacts stored per-run
- No model registry
- Hard to find "best model"
- No model versioning strategy
- Artifacts eventually deleted by GitHub

*Better Approach:* Model registry (MLflow Model Registry)

**10. Resource Constraints**

*Problem:* GitHub Actions has limits
- Limited compute time
- No GPU access
- Concurrent run limits
- Storage limits for artifacts

*Better Approach:* Dedicated ML platform or cloud compute

**11. No Experiment Status**

*Problem:* Cannot mark experiments as:
- Baseline
- Failed (but informative)
- Best so far
- To revisit

*Better Approach:* Experiment tagging and status tracking

**12. Scalability Issues**

*Problem:* Doesn't scale to:
- Large teams (merge conflicts)
- Many experiments (hundreds)
- Complex workflows (multi-stage pipelines)
- Long-running training (hours/days)

**Real-World Scenario Where This Breaks:**

Imagine testing 100 different hyperparameter combinations:
- 100 code edits
- 100 commits
- 100 workflow runs
- 5+ hours of waiting
- Git history destroyed
- No automatic "best" selection

**What Professional ML Teams Use Instead:**

| Tool | Purpose |
|------|---------|
| MLflow | Experiment tracking, model registry |
| Weights & Biases | Experiment visualization, comparison |
| Optuna | Automatic hyperparameter tuning |
| DVC | Data version control |
| Kubeflow | ML pipelines at scale |
| SageMaker | Cloud ML platform |

**Conclusion:** 

This approach is excellent for **learning CI/CD concepts** and suitable for **small-scale experimentation**, but has significant limitations for professional ML work. It's a stepping stone toward proper MLOps practices, not the final destination.

The next evolution would combine:
- Configuration-driven experiments (no code changes)
- Dedicated experiment tracking (MLflow)
- Automatic optimization (Optuna)
- Proper model registry
- Data versioning (DVC)

This lab taught us WHY these professional tools exist - by experiencing their absence!

---

## Summary Table: Lab 1 vs Lab 2 vs Professional MLOps

| Feature | Lab 1 | Lab 2 | Professional |
|---------|-------|-------|--------------|
| Automation | ❌ None | ✅ CI/CD | ✅ Full Pipeline |
| Reproducibility | ❌ Low | ✅ High | ✅ Perfect |
| Experiment Tracking | ❌ Manual | 🟡 Git-based | ✅ Dedicated Tool |
| Comparison | ❌ Spreadsheet | 🟡 Manual | ✅ Automatic Dashboard |
| Optimization | ❌ Manual | ❌ Manual | ✅ Automatic |
| Configuration | 🟡 Hardcoded | 🟡 Hardcoded | ✅ Files/CLI |
| Scalability | ✅ Local Only | 🟡 Limited | ✅ Cloud Scale |
| Collaboration | ❌ Difficult | ✅ Easy | ✅ Multi-team |
| Cost | ✅ Free | ✅ Free | 💰 Paid |

---

**Overall Assessment:**

Lab 2 represents a **significant step forward** in ML experiment management, introducing automation and reproducibility. However, it also clearly demonstrates the limitations that led to the development of professional MLOps tools. The experience of using this approach helps us understand and appreciate why tools like MLflow, Weights & Biases, and cloud ML platforms exist.

---

*End of Analysis*
