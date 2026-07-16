# Requirement Analysis

This phase details the system specifications, data input boundaries, and non-functional requirements to build a reliable prediction tool.

## 1. Functional Requirements
* **Core Inference Engine:** The system must accept three raw predictors:
  1. Life Expectancy at Birth (years)
  2. Mean Years of Schooling (years)
  3. Gross National Income (GNI) Per Capita (PPP USD)
* **Prediction Output:** The application must return a predicted HDI score (0.0 to 1.0) formatted to 4 decimal places.
* **Development Classification:** The system must map predictions to the official UNDP brackets:
  * Low Development ($HDI < 0.550$)
  * Medium Development ($0.550 \le HDI < 0.700$)
  * High Development ($0.700 \le HDI < 0.800$)
  * Very High Development ($HDI \ge 0.800$)

## 2. Non-Functional Requirements
* **Input Validation & Safety:** The backend must validate that inputs are numerical and fall within realistic physical ranges:
  * Life Expectancy: $20.0$ to $100.0$ years
  * Schooling: $0.0$ to $20.0$ years
  * GNI Per Capita: \$100 to \$150,000 PPP
* **UI Responsiveness:** The prediction forms must render dynamically and adapt to mobile, tablet, and desktop screens with a professional glassmorphic layout.
* **Low Latency:** Inference execution and template rendering must take less than 100ms.

---

## 🔗 Detailed Reference Link
For the comprehensive objectives, boundary limits, and data validation scopes, please refer to:
* **[Project Overview Document](../docs/Project_Overview.md)**
