# Project Design Phase: Solution Architecture

This phase details the architectural blueprint, data transmission sequence, and choice of technologies for the system.

## 1. System Architecture
The application employs an MVC-style pattern optimized for Python-based ML microservices:
* **View (Frontend):** Responsive glassmorphic interface (`app/templates/home.html` & `result.html`) powered by vanilla CSS (`app/static/style.css`).
* **Controller (Routing & Validation):** Flask web server (`app/app.py`) which manages routes, validates inputs, and handles error redirection.
* **Model (Inference Engine):** Scikit-learn Linear Regression model serialized to a binary (`model/hdi_model.pkl`) using Pickle.

## 2. End-to-End Data Pipeline
1. **Client Submission:** User submits raw features via HTTP POST request.
2. **Server Validation:** Backend runs range boundary validation checks. Fails trigger session flash alerts; passes cast data to floating-point values.
3. **Inference Execution:** Flask loads the serialized pickled model and calls the regression estimator to predict the HDI score.
4. **Post-Processing:** Predictions are clipped to a valid range of $[0.0, 1.0]$ and categorized into development brackets.
5. **UI Rendering:** The results page renders the predicted score and corresponding bracket.

---

## 🔗 Detailed Reference Link
For the system architecture diagram (Mermaid format), data flow maps, and tech stack rationale, please refer to:
* **[System Architecture & Workflow](../docs/Architecture.md)**
