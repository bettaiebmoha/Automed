from flask import Flask, request, render_template
import pandas as pd
import pickle
import os

app = Flask(__name__)

# 📌 Définition du chemin du modèle
MODEL_PATH = r"models/modele_voiture.pkl"

# 📌 Vérifier si le fichier existe avant de charger
if not os.path.exists(MODEL_PATH):
    print(f"❌ Erreur : Le fichier {MODEL_PATH} n'existe pas !")
else:
    print(f"📁 Chemin du modèle détecté : {MODEL_PATH}")

# 📌 Charger le modèle
model_pipeline = None  # Variable globale pour stocker le modèle

def load_model():
    global model_pipeline
    try:
        with open(MODEL_PATH, "rb") as file:
            model_pipeline = pickle.load(file)
        print("✅ Modèle chargé avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors du chargement du modèle : {e}")
        model_pipeline = None

# Charger le modèle au démarrage de l'application
load_model()

@app.route("/", methods=["GET", "POST"])
def home():
    car_models = sorted([
        "Peugeot 208", "Citroen C3", "Kia Sportage SX", "Volkswagon Golf 8 GTE",
        "Mercedes Benz CLA", "Peugeot Partner", "Skoda Kamiq", "BMW Série 5"
    ])  # Liste réduite pour l'exemple

    if request.method == "POST":
        try:
            if model_pipeline is None:
                raise ValueError("Le modèle n'est pas chargé correctement.")

            # 🔹 Récupérer les valeurs du formulaire
            model = request.form.get("model")
            mileage = request.form.get("mileage")
            year = request.form.get("year")
            gearbox = request.form.get("gearbox")
            fiscal_power = request.form.get("fiscal_power")
            fuel = request.form.get("fuel")

            # 🔹 Vérifier si tous les champs sont remplis
            if not all([model, mileage, year, gearbox, fiscal_power, fuel]):
                raise ValueError("Tous les champs doivent être remplis.")

            # 🔹 Convertir les valeurs
            mileage = int(mileage)
            year = int(year)
            fiscal_power = int(fiscal_power)

            # 🔹 Créer un DataFrame pour la prédiction
            features = pd.DataFrame([[model, mileage, year, gearbox, fiscal_power, fuel]],
                                    columns=["Modèle", "Kilométrage", "Année", "Boîte de vitesses", "Puissance fiscale", "Carburant"])

            print("📝 Données envoyées au modèle :", features)

            # 🔹 Faire la prédiction
            predicted_price = model_pipeline.predict(features)[0]

            return render_template("index.html", prediction=f"Prix estimé : {predicted_price:.2f} DT", models=car_models)

        except Exception as e:
            print(f"❌ Erreur lors de la prédiction : {e}")
            return render_template("index.html", error=f"Erreur: {e}", models=car_models)

    return render_template("index.html", models=car_models)

if __name__ == "__main__":
    app.run(debug=True)
