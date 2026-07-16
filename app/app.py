import os
import pickle
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
# Secret key required for session-based messages (flashing errors)
app.secret_key = "hdi_prediction_secret_key"

# Resolve absolute path to the serialized pickle model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "hdi_model.pkl")

# Load model globally on startup
model = None
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print("Machine Learning Model loaded successfully from:", MODEL_PATH)
except Exception as e:
    print(f"CRITICAL ERROR: Failed to load model from {MODEL_PATH}. Error: {e}")

def classify_hdi(score):
    """
    Classifies the HDI Score according to official UN Development Program brackets:
    - Low Human Development: < 0.550
    - Medium Human Development: 0.550 to < 0.700
    - High Human Development: 0.700 to < 0.800
    - Very High Human Development: >= 0.800
    """
    if score < 0.550:
        return "Low Human Development", "low-hdi"
    elif score < 0.700:
        return "Medium Human Development", "medium-hdi"
    elif score < 0.800:
        return "High Human Development", "high-hdi"
    else:
        return "Very High Human Development", "very-high-hdi"

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        flash("Error: Machine Learning model is not loaded. Please contact administration.", "danger")
        return redirect(url_for("home"))

    try:
        # Retrieve form parameters
        life_exp_raw = request.form.get("life_expectancy")
        schooling_raw = request.form.get("mean_years_of_schooling")
        gni_raw = request.form.get("gni_per_capita")

        # Basic presence validation
        if not life_exp_raw or not schooling_raw or not gni_raw:
            flash("All input fields are required.", "danger")
            return redirect(url_for("home"))

        # Cast to float/int
        life_exp = float(life_exp_raw)
        schooling = float(schooling_raw)
        gni = float(gni_raw)

        # Range validations
        errors = []
        if not (20.0 <= life_exp <= 100.0):
            errors.append("Life Expectancy must be between 20 and 100 years.")
        if not (0.0 <= schooling <= 20.0):
            errors.append("Mean Years of Schooling must be between 0 and 20 years.")
        if not (100.0 <= gni <= 150000.0):
            errors.append("GNI Per Capita must be between $100 and $150,000.")

        if errors:
            for err in errors:
                flash(err, "danger")
            # Return form inputs back to home so the user doesn't have to re-enter
            return render_template("home.html", 
                                   life_expectancy=life_exp_raw,
                                   mean_years_of_schooling=schooling_raw,
                                   gni_per_capita=gni_raw)

        # Model Inference
        # Features must be fed in the exact order: Life Expectancy, Mean Years of Schooling, GNI Per Capita
        prediction = model.predict([[life_exp, schooling, gni]])
        predicted_score = float(prediction[0])

        # Clip predictions between logical bounds of HDI (0.0 to 1.0)
        predicted_score = max(0.0, min(1.0, predicted_score))

        # Classification
        classification_msg, classification_class = classify_hdi(predicted_score)

        return render_template("result.html",
                               predicted_score=round(predicted_score, 4),
                               classification_msg=classification_msg,
                               classification_class=classification_class,
                               life_expectancy=life_exp,
                               mean_years_of_schooling=schooling,
                               gni_per_capita=gni)

    except ValueError:
        flash("Invalid input. Please enter valid numeric values.", "danger")
        return redirect(url_for("home"))
    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "danger")
        return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
