# Brainstorming & Ideation: Problem Statement

This phase focuses on identifying the socio-economic challenges in measuring national development and framing the system's objectives.

## 1. Problem Context & Ideation
Traditional metrics of national progress (e.g., Gross Domestic Product) only reflect economic output and ignore quality-of-life indicators. The United Nations Development Programme (UNDP) introduced the Human Development Index (HDI) to compile health, education, and income statistics into a single score. 

However, standard calculations require complex index normalization. Our brainstorming goal was to build a machine learning regression model that can:
* **Predict Instantly:** Estimate a country's HDI score using raw, unnormalized socio-economic parameters.
* **Maintain Transparency:** Ensure full interpretability of features to guide policy adjustments.
* **Categorize Development:** Classify countries into low, medium, high, and very high development brackets.

## 2. Completed Phase Deliverables
* **Feature Scope Definition:** Identified 3 core input features (Life Expectancy at Birth, Mean Years of Schooling, and GNI Per Capita).
* **Predictive Framework Formulation:** Selected a regression approach with safety boundary constraints to handle prediction safety.
* **Interface Specification:** Drafted a glassmorphic Flask web interface for public accessibility.

---

## 🔗 Detailed Reference Link
For the comprehensive problem statement, objectives, scope, and expected outcomes, please refer to the detailed project overview:
* **[Project Overview Document](../docs/Project_Overview.md)**
