# Model Performance & Results Analysis

This document reports the performance metrics of the trained **Human Development Index (HDI) Prediction model**, provides concrete prediction examples, analyzes residual limits, and links UI presentation layers with system outputs.

---

## 1. Model Evaluation Metrics

After training the Ordinary Least Squares (OLS) Linear Regression model on an 80-20 train-test split, the following metrics were recorded on the testing partition:

| Metric | Recorded Value | Academic Interpretation |
| :--- | :--- | :--- |
| **R-squared ($R^2$) Score** | `0.9459` | **Coefficient of Determination:** The model explains **94.59%** of the variance in country-level HDI scores using only life expectancy, mean schooling, and per capita income. |
| **Mean Squared Error (MSE)** | `0.000738` | The average of the squared prediction errors. The near-zero value indicates that actual data points lie extremely close to the regression hyperplane. |
| **Root Mean Squared Error (RMSE)** | `0.0272` | The average standard deviation of residuals. On the $0.0$ to $1.0$ HDI scale, a typical prediction is off by **less than 0.03 units**, indicating high reliability. |

---

## 2. Prediction Scenarios & Classification

To demonstrate the mathematical predictability of the system, we walk through three representative national development tiers:

### Scenario A: High Development Profile
* **Inputs:** Life Expectancy = $82.0$ years, Schooling = $13.0$ years, GNI Per Capita = \$50,000
* **Math Computation:**
  $$HDI = 0.006608 + 0.007175(82.0) + 0.019851(13.0) + 0.000001549(50000)$$
  $$HDI = 0.006608 + 0.588350 + 0.258063 + 0.077450 = 0.9305$$
* **System Classification:** **Very High Human Development** (since $HDI \ge 0.800$)

### Scenario B: Medium Development Profile
* **Inputs:** Life Expectancy = $68.0$ years, Schooling = $7.0$ years, GNI Per Capita = \$6,000
* **Math Computation:**
  $$HDI = 0.006608 + 0.007175(68.0) + 0.019851(7.0) + 0.000001549(6000)$$
  $$HDI = 0.006608 + 0.487900 + 0.138957 + 0.009294 = 0.6428$$
* **System Classification:** **Medium Human Development** (since $0.550 \le HDI < 0.700$)

### Scenario C: Low Development Profile
* **Inputs:** Life Expectancy = $53.0$ years, Schooling = $3.0$ years, GNI Per Capita = \$1,200
* **Math Computation:**
  $$HDI = 0.006608 + 0.007175(53.0) + 0.019851(3.0) + 0.000001549(1200)$$
  $$HDI = 0.006608 + 0.380275 + 0.059553 + 0.001859 = 0.4483$$
* **System Classification:** **Low Human Development** (since $HDI < 0.550$)

---

## 3. UI Presentation & Verification

The Flask application processes these predictions dynamically and displays them using custom glassmorphic cards:

### Web Input Interface
Users enter indicators through a styled landing page. Submitting the form runs the Flask controller routing layer logic (`app/app.py`), which calls the model's `predict()` function.
* **Reference UI Screenshot:** [HOME.png](../screenshots/HOME.png)

### Web Result Card
The prediction results page displays the calculated score (rounded to 4 decimal places) alongside its official UNDP grouping. The grouping is styled dynamically using a custom color code:
* **Very High Development:** Sleek purple-indigo accents.
* **High Development:** Emerald-green accents.
* **Medium Development:** Warm amber accents.
* **Low Development:** Crimson-red alert accents.
* **Reference UI Screenshot:** [RESULT.png](../screenshots/RESULT.png)
