from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Charger le modèle entraîné et les données nécessaires
model_pipeline = None  # Initialise une variable globale pour le modèle
car_models = sorted(set([
    "Peugeot 208", "Citroen C3", "Kia Sportage SX", "Volkswagon Golf 8 GTE", "Mercedes Benz CLA",
    "Peugeot Partner", "Skoda Kamiq", "BMW Série 5", "Mercedes Benz GLC", "Nissan Juke",
    "Renault Kwid Populaire", "BMW X1", "Mercedes Benz Classe S350", "Jaguar F Pace", "Jaguar XF",
    "Mercedes Benz Classe C", "Mercedes Benz Classe E Coupé", "Range Rover Evoque", "Jeep Compass",
    "Cupra Formentor Exclusive", "Porche Cayenne", "BMW Série 4 Grand Coupé", "DS 3 Chic",
    "BMW Série 1", "Golf 7 Join", "Kia Rio SX", "Seat Arona", "Toyota Hilux Double Cabine",
    "Audi A3 Sportback", "Volkswagon Golf 7", "Chery Tiggo 8 Pro", "Volkswagon Passat", "Renault Clio Campus",
    "BMW Série 3", "BMW X5", "BMW Série 7", "Volkswagon Tiguan", "Hyundai Tucson", "Mini 5 Porte", 
    "Fiat 500", "Renault Symbol", "Hyundai Grand i10", "Ssangyong Tivoli", "Haval H6", "Mitsubishi Pajero",
    "Skoda Fabia", "Ford Ecosport", "Hyundai Creta", "Mazda 2", "Toyota Land Cruiser", "Nissan Qashqai",
    "Audi A5 Sportback", "Seat Ibiza", "Nissan Patrol", "Peugeot 308", "Volkswagon Polo", "Toyota RAV4",
    "Range Rover Sport", "Mini Cooper", "Peugeot 508", "Mercedes Benz GLA", "BMW Série X4", "Hyundai i20"
]))

def load_model():
    global model_pipeline
    try:
        # Charger le modèle entraîné (par exemple, un pipeline scikit-learn)
        with open(r"C:\Users\betta\Downloads\modele_voiture.pkl", "rb") as file:
            model_pipeline = pickle.load(file)
        print("✅ Modèle chargé avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors du chargement du modèle : {e}")

# Charger le modèle au démarrage de l'application
load_model()

@app.route("/", methods=["GET", "POST"])
def home():
    models = car_models  # Utiliser la liste car_models directement

    if request.method == "POST":
        try:
            if not model_pipeline:
                raise ValueError("Le modèle n'est pas chargé correctement.")

            # Récupérer les valeurs du formulaire
            model = request.form.get("model")
            mileage = request.form.get("mileage")
            year = request.form.get("year")
            gearbox = request.form.get("gearbox")
            fiscal_power = request.form.get("fiscal_power")
            fuel = request.form.get("fuel")

            # Vérifier si tous les champs sont remplis
            if not all([model, mileage, year, gearbox, fiscal_power, fuel]):
                raise ValueError("Tous les champs doivent être remplis.")

            # Convertir les valeurs numériques
            mileage = int(mileage)
            year = int(year)
            fiscal_power = int(fiscal_power)

            # Créer un DataFrame pour la prédiction
            features = pd.DataFrame([[model, mileage, year, gearbox, fiscal_power, fuel]],
                                    columns=["Modèle", "Kilométrage", "Année", "Boîte de vitesses", "Puissance fiscale", "Carburant"])

            print("📝 Données envoyées au modèle :", features)

            # Faire la prédiction
            predicted_price = model_pipeline.predict(features)[0]
            return render_template("index.html", prediction=f"Prix estimé : {predicted_price:.2f} DT", models=models)

        except Exception as e:
            print(f"❌ Erreur lors de la prédiction : {e}")
            return render_template("index.html", error=f"Erreur: {e}", models=models)

    return render_template("index.html", models=models)

if __name__ == "__main__":
    app.run(debug=True)
