````markdown
# Day 8 — Machine Learning Basics

## Goal

By the end of Day 8, you should understand the basic foundation of Machine Learning.

Do not focus on memorizing many algorithms today.  
Focus on understanding how Machine Learning works step by step.

---

# 1. What is Machine Learning?

Machine Learning is a method where computers learn patterns from data and use those patterns to make predictions or decisions.

In normal programming, we write rules manually.

Example:

```python
if marks >= 50:
    print("Pass")
else:
    print("Fail")
````

In Machine Learning, we give data to the computer and the model learns patterns automatically.

Example:

```text
Study hours + previous results → model learns pattern → predicts future result
```

---

# 2. Dataset

A dataset is a collection of data.

Usually, it looks like a table.

Example:

| Hours Studied | Attendance | Marks | Result |
| ------------- | ---------: | ----: | ------ |
| 2             |         60 |    35 | Fail   |
| 5             |         80 |    70 | Pass   |
| 7             |         90 |    85 | Pass   |

This full table is called a dataset.

---

# 3. Features

Features are input columns.

They help the model make predictions.

Example:

| Hours Studied | Attendance | Marks |
| ------------- | ---------: | ----: |

These columns are features because they are used to predict the result.

In Python, features are usually stored in `X`.

Example:

```python
X = df[["Hours Studied", "Attendance", "Marks"]]
```

---

# 4. Target

Target is the output column.

It is the thing we want to predict.

Example:

| Result |
| ------ |
| Pass   |
| Fail   |
| Pass   |

Here, `Result` is the target.

In Python, target is usually stored in `y`.

Example:

```python
y = df["Result"]
```

---

# 5. Supervised Learning

Supervised Learning means the dataset already has answers.

The model learns from examples where the correct output is already given.

Example:

| Hours Studied | Result |
| ------------: | ------ |
|             1 | Fail   |
|             2 | Fail   |
|             5 | Pass   |
|             7 | Pass   |

The model learns:

```text
More study hours usually means higher chance of passing.
```

Common supervised learning tasks:

* Predict house price
* Predict exam result
* Predict customer purchase
* Detect spam email
* Predict salary

---

# 6. Unsupervised Learning

Unsupervised Learning means the dataset does not have answers.

The model tries to find hidden patterns or groups by itself.

Example:

| Age | Income | Shopping Score |
| --: | -----: | -------------: |
|  22 |   3000 |             80 |
|  45 |  12000 |             40 |
|  30 |   7000 |             70 |

There is no target column.

The model may group customers into:

* budget customers
* premium customers
* frequent buyers

Common unsupervised learning tasks:

* Customer grouping
* Pattern discovery
* Market segmentation
* Similar product grouping

---

# 7. Train/Test Split

Train/Test Split means dividing the dataset into two parts.

| Data Type     | Purpose                         |
| ------------- | ------------------------------- |
| Training Data | Used to teach the model         |
| Testing Data  | Used to check model performance |

Common split:

```text
80% training data
20% testing data
```

Why this is important:

If the model trains and tests on the same data, it may only memorize the answers.

That is bad.

We want the model to perform well on new unseen data.

---

# 8. Basic Prediction Flow

Most Machine Learning projects follow this flow:

```text
1. Load dataset
2. Clean dataset
3. Select features
4. Select target
5. Split data into train/test
6. Train model
7. Make prediction
8. Evaluate result
```

Example flow:

```text
Student data → train model → give new student hours → predict marks
```

---

# 9. Simple Linear Regression

Linear Regression is one of the simplest Machine Learning algorithms.

It is used to predict numbers.

Examples:

* Predict marks
* Predict salary
* Predict house price
* Predict temperature

Linear Regression tries to find a straight-line relationship between input and output.

Formula:

```text
y = mx + b
```

Meaning:

| Symbol | Meaning                  |
| ------ | ------------------------ |
| y      | predicted value          |
| x      | input value              |
| m      | slope                    |
| b      | starting value/intercept |

Example:

| Study Hours | Marks |
| ----------: | ----: |
|           1 |    20 |
|           2 |    40 |
|           3 |    60 |
|           4 |    80 |

The model learns:

```text
More study hours → more marks
```

Then it can predict marks for a new value.

---

# 10. Practical Python Example

Install required libraries:

```bash
pip install pandas scikit-learn
```

Code:

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])
```

Expected output:

```text
Predicted Marks: 120
```

---

# 11. Important Terms Summary

| Term                  | Simple Meaning                       |
| --------------------- | ------------------------------------ |
| Machine Learning      | Computer learns patterns from data   |
| Dataset               | Collection of data                   |
| Feature               | Input column                         |
| Target                | Output column                        |
| Model                 | Algorithm that learns patterns       |
| Training              | Teaching model using data            |
| Prediction            | Model gives output for new data      |
| Supervised Learning   | Data has answers                     |
| Unsupervised Learning | Data has no answers                  |
| Train/Test Split      | Divide data for learning and testing |
| Linear Regression     | Predicts numeric values              |

---

# 12. Day 8 Final Checklist

By the end of Day 8, you should be able to explain:

* What Machine Learning is
* What a dataset is
* What features are
* What a target is
* Difference between supervised and unsupervised learning
* Why train/test split is used
* Basic Machine Learning workflow
* What Linear Regression does
* How to train a simple model in Python

---

# 13. Main Rule

Do not memorize algorithms blindly.

First understand:

```text
Data → Pattern → Prediction → Evaluation
```

This is the core idea of Machine Learning.

```
```
