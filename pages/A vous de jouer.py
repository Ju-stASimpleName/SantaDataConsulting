import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Configuration de la page

st.title("Inscrivez les caractéristiques de votre produit")
# Importation des data sets
link_products = r"C:\Users\Wilders\Desktop\santa_data_consulting\amazon_products.csv"
link_categories = r"C:\Users\Wilders\Desktop\santa_data_consulting\amazon_categories.csv"
data_products = pd.read_csv(link_products)
df_products = pd.DataFrame(data_products)
data_categories = pd.read_csv(link_categories)
df_categories = pd.DataFrame(data_categories)
# Nettoyage du data set products
df_products.dropna(inplace=True)
# Merge des deux dataframes
df_all = pd.merge(df_products, df_categories, how="left", left_on="category_id", right_on="id")
# Filtrage pour ne retenir que la section toys & games
df_toys = df_all.loc[df_all["category_name"].str.contains("|".join(["Toys", "Games"]))]
# Échantillonnage pour ajuster le poids de la variable True pendant l'entraînement du modèle
df_sample_false = df_toys[df_toys['isBestSeller'] == False].sample(n=700)
df_sample_true = df_toys[df_toys['isBestSeller'] == True]
# Concaténation des deux dataframes échantillonnés
df_toys_sample = pd.concat([df_sample_true, df_sample_false])
# Initialisation du modèle
X = df_toys_sample[["stars", "reviews", "boughtInLastMonth", "price"]]
y = df_toys_sample["isBestSeller"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, train_size=0.75)
# Définition des meilleurs paramètres pour notre arbre de décision
best_params = {'max_depth': 4, 'min_samples_leaf': 4, 'min_samples_split': 10}
# Création du modèle d'arbre de décision avec les meilleurs paramètres
modelDTC = DecisionTreeClassifier(random_state=45, **best_params)
# Entraînement du modèle
modelDTC.fit(X_train, y_train)
# Sauvegarde du modèle
joblib.dump(modelDTC, 'modele_decision_tree_parametres_optimises.pkl')
# Création d'un formulaire personnalisé pour collecter les informations de l'utilisateur
form = st.form(key='my_form')
my_stars = form.number_input('Quelle note moyenne a obtenu ton produit? ')
my_reviews = form.number_input('Combien d\'évaluations a reçu ton produit? ')
boughtInLastMonth = form.number_input('Combien de ventes ton produit a-t-il enregistré le mois dernier? ')
my_price = form.number_input('Quel est le prix de vente de ton produit? ')
submit_button = form.form_submit_button('Verdict')
# Vérifier si le formulaire a été soumis
if submit_button:
    # Vérifier que tous les champs sont remplis
    if my_stars is not None and my_reviews is not None and boughtInLastMonth is not None and my_price is not None:
        # Exécuter la prédiction seulement si tous les champs sont remplis
        my_data = np.array([my_stars, my_reviews, boughtInLastMonth, my_price]).reshape(1, 4)
        prediction = modelDTC.predict(my_data)
        # Afficher le résultat
        if prediction[0]:
            st.markdown("<h1 style='text-align: center;'>Félicitations, ce produit est une tuerie! \U0001F680</h1>", unsafe_allow_html=True)
        else:
            st.markdown("<h1 style='text-align: center;'>Dommage, il reste encore un peu de travail pour en faire un best-seller! \U0001F527</h1>", unsafe_allow_html=True)