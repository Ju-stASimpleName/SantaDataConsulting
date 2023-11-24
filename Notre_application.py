import streamlit as st

st.snow()
# Configuration de la page
# st.set_page_config(page_title="Best-seller app", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")


st.title(":santa: Santa Data Consulting :christmas_tree:")

st.subheader("Modèle de prédiction de Best-Sellers pour les jouets et jeux sur Amazon US pendant les fêtes de fin d'année.")

st.write("Bienvenue dans cette interface dans laquelle a été intégrée notre modèle de prédiction conçu pour anticiper les chances qu'a un produit de devenir un best-seller pendant la période de fêtes de fin d'année sur la plateforme Amazon US.")

st.write("Contexte :\n Notre modèle a été spécifiquement entraîné sur un ensemble de données soigneusement sélectionné, comprenant des références de produits vendus dans la catégorie 'toys & games' sur Amazon US. Cette catégorie, étant particulièrement dynamique et compétitive pendant la période des fêtes de fin d'année, offre un terrain propice à la prédiction des best-sellers.")

st.write("Caractéristiques prises en compte :\n* Prix : Un facteur crucial, car il influence directement la décision d'achat du consommateur pendant les périodes promotionnelles.\n* Note Globale : La satisfaction des clients est un indicateur majeur de la popularité du produit.\n* Nombre de Votants : Un nombre élevé de votants suggère une base d'utilisateurs significative, ce qui peut être lié à la notoriété du produit.\n* Nombre de Ventes le Mois Précédent : Une indication solide de la tendance récente de popularité du produit.")

st.write("Objectif :\n L'objectif principal de notre système est de fournir aux vendeurs une estimation fiable des chances qu'a leur produit de devenir un best-seller pendant la période de fête. Cette information précieuse peut guider les stratégies marketing, les décisions de tarification, et les efforts de promotion pour maximiser les opportunités de vente.")

st.write("Avantages clés :\n* Précision : Grâce à notre modèle basé sur un arbre de décision, nous avons atteint des niveaux élevés de précision dans la prédiction des best-sellers.\n* Adaptabilité : Le modèle peut s'ajuster aux évolutions du marché, assurant ainsi une pertinence continue pendant toute la période de fête.\n* Facilité d'utilisation : Avec une interface simple d'utilisation, notre système permet aux utilisateurs de prendre des décisions éclairées sans nécessiter une expertise technique approfondie.")

st.write("En conclusion, notre modèle de prédiction représente un outil puissant pour les vendeurs cherchant à optimiser leur présence sur Amazon US pendant la période des fêtes de fin d'année. En combinant des données pertinentes et une analyse avancée, nous sommes convaincus que notre solution contribuera à maximiser les opportunités de vente et à orienter les entreprises vers le succès.")