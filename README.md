Description du projet
Ce projet consiste en une application web Flask conçue pour estimer le prix d'une voiture d'occasion en fonction de plusieurs critères clés. L'application permet aux utilisateurs d'entrer des informations telles que :
Modèle de la voiture
Kilométrage
Année de fabrication
Boîte de vitesses (manuelle ou automatique)
Puissance fiscale
Type de carburant (essence, diesel, électrique, etc.)
Fonctionnalités principales :
Estimation du prix : L'utilisateur remplit un formulaire avec les caractéristiques de la voiture et soumet les données pour obtenir une estimation du prix de la voiture basée sur un modèle de machine learning pré-entraîné.
Interface utilisateur intuitive : Le design est simple et moderne, permettant une navigation fluide. L'interface s'adapte aux différents types d'appareils, offrant ainsi une expérience utilisateur agréable.
Prédiction de prix basée sur un modèle de machine learning : Le modèle utilise les bibliothèques Python telles que scikit-learn pour effectuer des prédictions sur le prix d'une voiture d'occasion en fonction des données fournies.
Chargement dynamique du modèle : Lors du démarrage de l'application, le modèle est chargé et prêt à faire des prédictions dès que l'utilisateur envoie des informations via le formulaire.
Gestion des erreurs et des entrées invalides : L'application prend en charge les erreurs liées aux entrées des utilisateurs (champs manquants, valeurs incorrectes) et affiche des messages d'erreur appropriés.
Technologies utilisées :
Flask : Un micro-framework Python pour le développement d'applications web.
Pandas et NumPy : Pour la gestion des données d'entrée et la manipulation des valeurs numériques.
scikit-learn : Utilisé pour charger et appliquer le modèle de machine learning pour la prédiction des prix.
HTML, CSS : Pour le rendu et le design de l'interface utilisateur.
Gunicorn : Un serveur WSGI pour déployer l'application sur un serveur de production.
Fonctionnement du modèle :
Le modèle de machine learning a été entraîné avec des données relatives aux voitures d'occasion et utilise ces informations pour prédire le prix d'un véhicule en fonction de ses caractéristiques. Le modèle a été sauvegardé dans un fichier .pkl et est chargé dynamiquement au démarrage de l'application.
