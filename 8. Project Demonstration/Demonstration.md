# Project Demonstration

This document showcases the running application, contains the primary demonstration links, and suggests an evaluation flow for auditors.

## 1. Project Summary
The **HDI Prediction System** is a responsive web application powered by a trained Scikit-learn Linear Regression model. It predicts country-level Human Development Index (HDI) scores using raw indicators: Life Expectancy, Schooling, and GNI per Capita. The interface utilizes a glassmorphic layout with dynamic color themes matching official UN development brackets.

## 2. Primary Demonstration Links

* **🚀 Live Deployment URL:** [hdi-predictor-7cwb.onrender.com](https://hdi-predictor-7cwb.onrender.com/)
  *(Hosts the running, interactive web application deployed on Render)*
* **🎥 Demonstration Video URL:** [Google Drive Video Walkthrough](https://drive.google.com/file/d/1NTuKqvSZDWj6mxcPyroNCTFybO-rs0jp/view?usp=sharing)
  *(Provides a recorded step-by-step overview of model training, server startup, inference, and boundary validation testing)*

## 3. Features Demonstrated
* **Real-time Prediction:** Sub-100ms model prediction based on user-entered values.
* **UNDP Category Classification:** Automated assignment to Low, Medium, High, or Very High categories with color-coded results cards.
* **Input Validation & Safety Bounds:** Rejects invalid numeric characters and displays warning alerts if values lie outside realistic global ranges (e.g. Life Expectancy not in $[20, 100]$).
* **Glassmorphic Layout:** Responsive UI styling adapting to mobile and desktop displays.

## 4. Suggested Evaluation Flow
1. **Interactive Test:** Navigate to the [Live Deployment URL](https://hdi-predictor-7cwb.onrender.com/) and enter test parameters:
   - *Example (High Profile):* Life Expectancy = `82.0`, Mean Schooling = `13.0`, GNI = `50000` -> Expect predicted HDI `0.9305` (Very High Development).
2. **Boundary Test:** Enter life expectancy as `12` or `120` to verify boundary checks and notice the descriptive error alerts.
3. **Recorded Tour:** If internet connectivity to Render is slow or a walkthrough is preferred, watch the [Google Drive Video Walkthrough](https://drive.google.com/file/d/1NTuKqvSZDWj6mxcPyroNCTFybO-rs0jp/view?usp=sharing).
