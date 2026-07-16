# Project Testing & Validation

This phase reports on the model evaluation scores, validates boundary conditions, and runs specific test scenarios.

## 1. Model Performance Metrics
The Ordinary Least Squares model achieves the following validation performance on the testing partition:
* **Coefficient of Determination ($R^2$):** `0.9459` (Explains 94.59% of target variance)
* **Mean Squared Error (MSE):** `0.000738`
* **Root Mean Squared Error (RMSE):** `0.0272` (Typical prediction error is $<0.03$ index units)

## 2. Test Verification Scenarios
To check mathematical calculations, three representative developmental profiles were verified:
1. **Scenario A (High Development):** 
   - Inputs: Life Exp = 82.0, Schooling = 13.0, GNI = \$50,000
   - Output: `0.9305` (Very High Human Development)
2. **Scenario B (Medium Development):**
   - Inputs: Life Exp = 68.0, Schooling = 7.0, GNI = \$6,000
   - Output: `0.6428` (Medium Human Development)
3. **Scenario C (Low Development):**
   - Inputs: Life Exp = 53.0, Schooling = 3.0, GNI = \$1,200
   - Output: `0.4483` (Low Human Development)

## 3. Input Validation Auditing
Tested edge cases and invalid inputs to verify that the app does not crash:
* Empty fields or non-numeric characters raise a visible user warning.
* Out-of-bounds parameters (e.g. Life Expectancy = 150) trigger a validation error, guiding users back to safe ranges.

---

## 🔗 Detailed Reference Link
For the comprehensive metrics table, scenario steps, and UI verification screenshots, please refer to:
* **[Model Performance & Results Analysis](../docs/Results.md)**
