# Project Methodology

This document details the scientific and technical methodology applied in the **Human Development Index (HDI) Prediction System**. It covers the data lifecycle, theoretical mathematical equations, feature engineering decisions, and model evaluation framework.

---

## 1. Dataset Collection & Features

The dataset (`dataset/hdi_data.csv`) is representative of the official **United Nations Development Programme (UNDP) Human Development Report**. It aggregates development indicators across **150 countries** covering diverse developmental states.

The dataset includes the following variables:
* **Predictor 1 (Life Expectancy at Birth):** Average number of years a newborn is expected to live. This acts as a proxy for the country's health systems and general mortality profile.
* **Predictor 2 (Mean Years of Schooling):** Average number of years of education received by individuals aged 25 and older. This acts as a proxy for educational attainment and accessibility.
* **Predictor 3 (Gross National Income (GNI) Per Capita):** GNI per capita converted to international dollars using Purchasing Power Parity (PPP) rates. This represents the economic standard of living.
* **Target (HDI Score):** The composite decimal scale index ranging from $0.0$ (lowest human development) to $1.0$ (highest human development).

---

## 2. Mathematical Modeling

To predict the HDI score, we implement a **Linear Regression** model. The relationship between the predictors and the target index is modeled as:

$$HDI = \beta_0 + \beta_1 \cdot x_1 + \beta_2 \cdot x_2 + \beta_3 \cdot x_3 + \epsilon$$

Where:
* $x_1$: Life Expectancy at Birth (years)
* $x_2$: Mean Years of Schooling (years)
* $x_3$: GNI Per Capita (USD PPP)
* $\beta_0$: Intercept (base value)
* $\beta_1, \beta_2, \beta_3$: Coefficient weights corresponding to each feature
* $\epsilon$: Residual error term

### Trained Parameters
From the trained pickled model, we extract the exact coefficients and intercept:
* **Intercept ($\beta_0$):** $+0.00660801$
* **Life Expectancy Coefficient ($\beta_1$):** $+0.00717492$
* **Mean Years of Schooling Coefficient ($\beta_2$):** $+0.01985100$
* **GNI Per Capita Coefficient ($\beta_3$):** $+0.00000155$

Thus, the concrete prediction formula is:

$$HDI = 0.00660801 + 0.00717492 \cdot (\text{Life Expectancy}) + 0.01985100 \cdot (\text{Schooling}) + 0.00000155 \cdot (\text{GNI})$$

---

## 3. Workflow Stages

### Stage A: Data Preprocessing & Validation
* **Missing Value Imputation:** Minor missing values simulated in raw datasets are handled via statistical imputation (e.g. replacing null values with feature medians) within the exploratory pipeline.
* **Feature Scaling Rationale:** No feature scaling (Standardization/MinMax) is applied to the final training inputs. Since Linear Regression coefficients are scale-dependent, training on raw values preserves the direct physical meaning of weights (e.g., an increase of 1 year of schooling directly contributes $+0.0199$ to the HDI score).

### Stage B: Exploratory Data Analysis (EDA)
Executed inside the `notebooks/hdi_analysis.ipynb` environment, the EDA phase includes:
1. **Univariate Analysis:** Reviewing skewness and distributions of the input features.
2. **Multivariate Relational Analysis:** Visualizing predictors against the target HDI using Seaborn scatter and strip plots.
3. **Correlation Heatmaps:** Showing highly linear relations between the target HDI and the predictors (Life Expectancy and Schooling both demonstrate strong positive correlations of $r > 0.85$).

### Stage C: Model Training & Tuning
* **Split Ratio:** The dataset is partitioned into **80% training** and **20% testing** subsets using a set random seed for repeatability.
* **Training Algorithm:** Standard Ordinary Least Squares (OLS) regression trained using Scikit-learn.

---

## 4. Model Selection Justification

Linear Regression was selected over non-linear models (e.g., Random Forests, Gradient Boosted Trees, Neural Networks) due to the following academic and operational considerations:

1. **Analytical Alignment with UNDP Framework:** The official HDI calculation compounds these three dimensions. In a moderately linear space, Linear Regression behaves closely to the actual index index-building logic.
2. **High Explainability & Policy Value:** The model weights can be directly explained. For instance, each year of schooling increases HDI by $\approx 0.02$, providing policymakers with clear, actionable ratios.
3. **Low Compute Overhead:** Linear Regression executes with $O(1)$ query time and negligible space complexity, making it ideal for hosting on zero-tier free servers (e.g. Render) without cold-start memory leaks.
4. **Generalization:** Non-linear models run the risk of overfitting on a small dataset (150 countries), whereas OLS remains robust and generalizes well across diverse regions.
