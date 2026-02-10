""" Point d’entree du pipeline ETL GameTracker."""
from src.config import Config
from src.database import database_connection
from src.extract import extract_data
from src.transform import transform_players, transform_scores
from src.load import load_players, load_scores

def run_pipeline():
    """ Execute le pipeline ETL complet (Players et Scores). """
    print("=" * 50)
    print(" Démarrage du pipeline ETL GameTracker")
    print("=" * 50)

    with database_connection() as conn:
        # --- ÉTAPE : EXTRACTION ---
        print("\n--- [1/3] Extraction des données CSV ---")
        # On extrait les deux DataFrames bruts
        df_players_raw, df_scores_raw = extract_data()

        # --- ÉTAPE : TRANSFORMATION & CHARGEMENT PLAYERS ---
        print("\n--- [2/3] Traitement des Joueurs (Players) ---")
        df_players_clean = transform_players(df_players_raw)
        load_players(df_players_clean, conn)
        
        # --- ÉTAPE : TRANSFORMATION & CHARGEMENT SCORES ---
        print("\n--- [3/3] Traitement des Scores ---")
        # On récupère la liste des player_id valides pour éviter les orphelins
        valid_ids = df_players_clean['player_id'].unique().tolist()
        
        # On transforme les scores en vérifiant les IDs
        df_scores_clean = transform_scores(df_scores_raw, valid_ids)
        load_scores(df_scores_clean, conn)

    print("\n" + "=" * 50)
    print(" Pipeline terminé avec succès !")
    print("=" * 50)

if __name__ == '__main__':
    run_pipeline()

    