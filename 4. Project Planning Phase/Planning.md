# Project Planning Phase: Planning & Setup

This phase reviews the development timeline, task prioritization, and dataset/model sourcing strategy.

## 1. Project Timeline & Milestones
We structured the project execution into 4 successive phases:
* **Phase A: Data Sourcing & Exploration:** Aggregated a representative UNDP dataset (`dataset/hdi_data.csv`) of 150 nations. Performed exploratory analysis in Jupyter.
* **Phase B: Mathematical Modeling:** Selected and trained an Ordinary Least Squares (OLS) Linear Regression model to maximize interpretability.
* **Phase C: Web Interface Development:** Built a Flask server to host the model and designed glassmorphic web pages.
* **Phase D: System Verification & Deployment:** Verified prediction scenarios, tested input boundaries, and deployed to Render.

## 2. Resource & Technology Choices
* **Inference Platform:** Python 3.8+ with Flask for a lightweight web server.
* **ML Stack:** Scikit-learn, Pandas, NumPy for calculations.
* **Visualization:** Seaborn & Matplotlib for exploratory charts.
* **Persistence:** Pickle library for serializing model weights.

---

## 🔗 Detailed Reference Link
For the mathematical modeling equations, data lifecycle stages, and model selection justifications, please refer to:
* **[Project Methodology](../docs/Methodology.md)**
