import streamlit as st
import requests
import pandas as pd
import os

# Configuration de la page
st.set_page_config(page_title="DevSpend-Flow Dashboard", page_icon="💸", layout="wide")

st.title("💸 DevSpend-Flow - Dashboard")
st.markdown("Bienvenue sur le tableau de bord de vos dépenses.")

# On lit l'URL depuis les variables d'environnement, sinon on utilise le localhost par défaut
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api/v1")

# On fait un appel GET à notre API pour récupérer le résumé analytique
try:
    response = requests.get(f"{API_URL}/analytics/summary")
    response.raise_for_status() # Lève une erreur si l'API répond mal
    data = response.json()
    
    # Affichage du total général
    st.metric(label="Total Général des dépenses", value=f"{data['total_general']:.2f} €")
    
    st.divider() # Ligne de séparation
    
    # Préparation des données pour les graphiques
    if data["total_par_categorie"]:
        df = pd.DataFrame(data["total_par_categorie"])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Répartition par catégorie")
            # Graphique en barres
            st.bar_chart(df.set_index("categorie")["total"])
            
        with col2:
            st.subheader("Détail")
            # Tableau des données
            st.dataframe(df, use_container_width=True)
            
    else:
        st.info("Aucune transaction enregistrée pour le moment.")

except requests.exceptions.ConnectionError:
    st.error("⚠️ Impossible de contacter l'API. Es-tu sûr que le serveur Uvicorn tourne sur le port 8000 ?")