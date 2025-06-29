
# Airbnb Price Prediction Project

## Objective

The goal of this project is to apply **data exploration** and **supervised machine learning techniques** to predict the **logarithm of Airbnb prices** based on listing features. Students will learn how to:

* Explore and visualize complex datasets
* Perform data cleaning and feature engineering
* Train, evaluate, and compare ML models
* Generate predictions for a hidden test set

---

## Project Deliverables

1. **Jupyter Notebook** (`airbnb_project.ipynb`) containing:

   * Exploratory data analysis (EDA)
   * Preprocessing and feature engineering steps
   * Model training and evaluation
   * Visualizations and markdown explanations

2. **Prediction File** (`prediction.csv`) containing:

   * Two columns: `id` and `prediction`
   * Format should match `prediction_example.csv`

---

## 👥 Team

* Max **2 students per group**

---

### Features Overview (from `Explication.txt`)

Each row represents one Airbnb listing. Below are the available features:

| Column Name                    | Description                                      |
| ------------------------------ | ------------------------------------------------ |
| `id`                           | Listing ID                                       |
| `property_type`                | Type of property (e.g., Apartment, House)        |
| `room_type`                    | Room type (e.g., Private room, Entire home/apt)  |
| `amenities`                    | Text list of amenities (e.g., Wifi, TV, Kitchen) |
| `accommodates`                 | How many people the listing accommodates         |
| `bathrooms`                    | Number of bathrooms                              |
| `bed_type`                     | Type of bed                                      |
| `cancellation_policy`          | Cancellation policy                              |
| `cleaning_fee`                 | Cleaning fee (true/false or amount)              |
| `city`                         | City of the listing                              |
| `description`                  | Textual description of the listing               |
| `first_review`                 | Date of the first review                         |
| `host_has_profile_pic`         | Whether host has profile picture                 |
| `host_identity_verified`       | Whether host is identity-verified                |
| `host_response_rate`           | Host’s response rate (percentage)                |
| `host_since`                   | Host registration date                           |
| `instant_bookable`             | Can the listing be instantly booked              |
| `last_review`                  | Date of the last review                          |
| `latitude`, `longitude`        | Geolocation                                      |
| `name`                         | Name/title of the listing                        |
| `neighbourhood`                | Neighbourhood or zone                            |
| `number_of_reviews`            | Total number of reviews                          |
| `review_scores_rating`         | Overall rating (out of 100)                      |
| `zipcode`                      | Zip/postal code                                  |
| `bedrooms`, `beds`             | Number of bedrooms and beds                      |
| **`log_price`** *(train only)* | Logarithm of the nightly price (target)          |

## Project Structure

### 1. 🔍 Data Exploration (≈ 1/3 of the time)

* Present dataset structure (features, types, distributions)
* Highlight missing values, outliers, distributions, and correlations
* Include rich visualizations (histograms, heatmaps, maps if relevant)
* Justify preprocessing/feature selection based on exploration

### 2. Prediction (≈ 2/3 of the time)

* Experiment with different preprocessing pipelines:

  * Encoding
  * Scaling/normalization
  * Feature engineering
* Try multiple ML models:

  * Linear Regression, Decision Trees, Random Forests, XGBoost, etc.
* Perform rigorous model evaluation:

  * Train/test split, cross-validation
  * Define a baseline model
  * Compare models with clear metrics (e.g., RMSE)

---

## Notebook Requirements

* **Clear structure** with:

  * Markdown explanations
  * Comments in code
  * Visualizations of key steps and results
* **Readable and pedagogical**: A good notebook > high score with unreadable code
* **Prediction file** must follow the required format exactly

---

## Evaluation Criteria

### ✔️ 1/3 of the grade: **Data Exploration**

* Clarity and completeness of dataset presentation
* Relevance and aesthetics of visualizations
* Insights and hypotheses generated

### ✔️ 2/3 of the grade: **Prediction**

* Diversity and creativity in feature engineering
* Variety of models tested
* Evaluation rigor and baseline comparison
* Result analysis and justifications

> 🔔 **Tip**: A well-structured and explained notebook with moderate performance is **preferred** over an unclear one with a high score.

---

## Provided Files

| Filename                 | Purpose                              |
| ------------------------ | ------------------------------------ |
| `airbnb_train.csv`       | Training set with target `log_price` |
| `airbnb_test.csv`        | Test set without `log_price`         |
| `prediction_example.csv` | Sample output format for submission  |
| `Explication.txt`        | Feature and task explanation         |

