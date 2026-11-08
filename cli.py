import pandas as pd
import os

# 1. Définir le chemin vers notre fichier CSV
CSV_PATH = os.path.join("data", "transactions.csv")

def process_transactions():
    print("⏳ Chargement des données...")
    
    # 2. Lire le fichier CSV avec pandas
    df = pd.read_csv(CSV_PATH)
    
    # Afficher le nombre de lignes au départ
    print(f"Lignes initiales : {len(df)}")
    
    # 3. Nettoyage : Supprimer les doublons
    df = df.drop_duplicates()
    print(f"Lignes après nettoyage des doublons : {len(df)}")
    
    # 4. Nettoyage : Remplir les catégories manquantes par "Inconnu"
    df['categorie'] = df['categorie'].fillna('Inconnu')
    
    # 5. Calcul des statistiques (Total par catégorie)
    print("\n📊 Total des dépenses par catégorie :")
    stats_par_categorie = df.groupby('categorie')['montant'].sum().sort_values(ascending=False)
    
    # Affichage propre
    for categorie, total in stats_par_categorie.items():
        print(f" - {categorie} : {total:.2f} €")
        
    # 6. Total général
    total_general = df['montant'].sum()
    print(f"\n💰 Total général des dépenses : {total_general:.2f} €")

if __name__ == "__main__":
    process_transactions()