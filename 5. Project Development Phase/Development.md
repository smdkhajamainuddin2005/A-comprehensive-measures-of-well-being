# Project Development Phase: Implementation

This phase covers model development, serialization, and integration into the web application logic.

## 1. Model Training & Mathematics
The core ML model is an Ordinary Least Squares (OLS) Linear Regression trained on the 150-country dataset. The training yields the following exact parameters:
* **Intercept ($\beta_0$):** $+0.00660801$
* **Life Expectancy Coeff ($\beta_1$):** $+0.00717492$
* **Mean Schooling Coeff ($\beta_2$):** $+0.01985100$
* **GNI Per Capita Coeff ($\beta_3$):** $+0.00000155$

This translates to the predictive formula:
$$HDI = 0.00660801 + 0.00717492 \cdot (\text{Life Expectancy}) + 0.01985100 \cdot (\text{Schooling}) + 0.00000155 \cdot (\text{GNI})$$

## 2. Software Development
* **Exploratory Data Analysis:** Conducted univariate distribution and multivariate correlation mapping inside `notebooks/hdi_analysis.ipynb`.
* **Model Serialization:** Serialized the trained Scikit-learn model to `model/hdi_model.pkl`.
* **Flask Controller:** Programmed `app/app.py` to:
  * Read the serialized model on startup.
  * Extract input values safely.
  * Implement predictions, clip them to $[0.0, 1.0]$, and classify them.

---

## 🔗 Detailed Reference Links
* **[Project Methodology](../docs/Methodology.md)** - Details on calculations and preprocessing.
* **[Exploratory Notebook](../notebooks/hdi_analysis.ipynb)** - Code showing EDA, training, and pickle export.
