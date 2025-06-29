

## 🎓 **Subsection A – Introduction to Machine Learning**

> **Lecture Duration**: \~2 hours
> **Slides**: \~25–30

---

### 🟦 Slide 1 – Title Slide

**Title**: Introduction to Machine Learning
**Subtitle**: Data Science Course – M2 AI & Data Science
**Presented by**: *Ali Mokh*

> *Optional image: AI in the real world (self-driving car, fraud detection, etc.)*

---

### 🟦 Slide 2 – Learning Objectives

By the end of this lecture, you will be able to:

* Explain what machine learning is and how it differs from traditional programming
* Identify different types of machine learning (supervised vs. unsupervised)
* Understand the full ML pipeline: from data to deployment
* Recognize overfitting, underfitting, and generalization
* Use Scikit-learn’s API and pipelines

---

### 🟦 Slide 3 – What is Machine Learning?

* A method of teaching computers to learn from data
* **Tom Mitchell's Definition**:

  > *“A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.”*
* In contrast to **explicit rule-based programming**

---

### 🟦 Slide 4 – Traditional Programming vs. ML

| Traditional Programming | Machine Learning      |
| ----------------------- | --------------------- |
| Rules + Data → Output   | Data + Output → Rules |
| Hand-coded logic        | Model learns patterns |
| Static behavior         | Adaptive behavior     |

> *Speaker note: Give a spam filtering example – rules vs. ML.*

---

### 🟦 Slide 5 – ML in the Real World

* Credit scoring
* Medical diagnosis
* Personalized recommendations
* Voice assistants
* Image recognition
* Predictive maintenance

---

### 🟦 Slide 6 – Categories of Machine Learning

* Supervised Learning
* Unsupervised Learning
* Semi-supervised Learning
* Reinforcement Learning

> We'll focus on the first two in this course.

---

### 🟦 Slide 7 – Supervised Learning

* Learn from **labeled data**
* Objective: predict output `y` from input `X`
* **Tasks**:

  * Regression → continuous `y`
  * Classification → discrete labels
* 📌 Example: Predicting house prices from features like area, rooms

---

### 🟦 Slide 8 – Unsupervised Learning

* No labels, only input data `X`
* Discover patterns or structures
* **Tasks**:

  * Clustering (e.g., customer segmentation)
  * Dimensionality Reduction (e.g., PCA)
* 📌 Example: Grouping customers by behavior without labels

---

### 🟦 Slide 9 – Visual: Supervised vs. Unsupervised

> Show a graphic:

* Labeled dataset → model
* Unlabeled dataset → clusters

---

### 🟦 Slide 10 – Machine Learning Workflow

Typical ML pipeline:

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Model Selection
5. Training
6. Evaluation
7. Hyperparameter Tuning
8. Deployment & Monitoring

> *Each stage will be explored in more detail throughout the course.*

---

### 🟦 Slide 11 – Key Terminologies

* **Features**: Independent variables (X)
* **Target/Label**: Dependent variable (y)
* **Sample/Instance**: A single observation
* **Model**: Mathematical function mapping X to y
* **Loss Function**: Quantifies model error
* **Learning Algorithm**: Adjusts parameters to minimize loss

---

### 🟦 Slide 12 – Train/Test Split

* Separate dataset into:

  * **Training Set**: Used to train the model
  * **Test Set**: Used to evaluate generalization
* Typical split: 80/20 or 70/30
* Prevents **data leakage**

---

### 🟦 Slide 13 – Overfitting vs. Underfitting

* **Underfitting**:

  * Too simple
  * High bias
* **Overfitting**:

  * Too complex
  * High variance
* Ideal: low bias and variance

> *Include diagram: model complexity vs. error*

---

### 🟦 Slide 14 – Generalization & Cross-Validation

* Generalization: model’s performance on unseen data
* **k-Fold Cross-Validation**:

  * Data split into k parts
  * Each part used as validation once
  * Reduces variance in evaluation

---

### 🟦 Slide 15 – Bias–Variance Tradeoff

* Total Error = Bias² + Variance + Irreducible Error
* Need balance:

  * High bias → underfit
  * High variance → overfit

> *Include visualization with curves*

---

### 🟦 Slide 16 – Introduction to Scikit-learn

* Python’s most widely used ML library
* Clean and consistent API
* Integrates:

  * Preprocessing
  * Modeling
  * Validation
  * Pipelines

---

### 🟦 Slide 17 – Estimator API

Every ML model in Scikit-learn follows this structure:

```python
model = ModelClass()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

### 🟦 Slide 18 – Transformer & Preprocessing API

For preprocessing:

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
```

Other examples:

* `MinMaxScaler`
* `OneHotEncoder`
* `SimpleImputer`

---

### 🟦 Slide 19 – Scikit-learn Pipeline Example

Combine preprocessing + model:

```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
pipe.fit(X_train, y_train)
```

> Reduces code repetition and error.

---

### 🟦 Slide 20 – Common Scikit-learn Models

| Task           | Model Classes                                         |
| -------------- | ----------------------------------------------------- |
| Classification | `LogisticRegression`, `RandomForestClassifier`, `SVC` |
| Regression     | `LinearRegression`, `Ridge`, `SVR`                    |
| Clustering     | `KMeans`, `DBSCAN`                                    |

---

### 🟦 Slide 21 – Case Study 1: Titanic Dataset

* **Goal**: Predict survival (`Survived`)
* Features: `Sex`, `Age`, `Pclass`, `Fare`, etc.
* Binary classification
* Example model: Logistic Regression

> Discuss preprocessing: filling missing ages, encoding gender, etc.

---

### 🟦 Slide 22 – Case Study 2: Boston Housing

* **Goal**: Predict median house price (`MEDV`)
* Regression task
* Input features: `CRIM`, `ZN`, `RM`, `LSTAT`, etc.
* Metrics: MSE, R²

---

### 🟦 Slide 23 – Summary

✅ Machine learning learns from data
✅ Supervised vs. Unsupervised learning
✅ Train/Test splits and overfitting
✅ Scikit-learn provides modular tools
✅ Pipelines standardize preprocessing and modeling

---

### 🟦 Slide 24 – Questions for Discussion

* When would you prefer unsupervised learning?
* What happens if we evaluate on training data?
* How does Scikit-learn simplify ML workflows?

---

### 🟦 Slide 25 – Teaser: Next Steps

➡️ **Next Lecture**: Model Evaluation
➡️ **Hands-on Lab**: Build your first ML model with Scikit-learn on the Titanic dataset
