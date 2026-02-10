"""Module ETL : Extract, Transform, Load."""
import pandas as pd

# ============== TRANSFORM PLAYERS ==============
def transform_players(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforme et nettoie les données des joueurs selon les 4 règles strictes.
    """
    df = df.copy()

    # 1. Supprimer les doublons sur player_id
    df = df.drop_duplicates(subset=['player_id'])

    # 2. Nettoyer les espaces des username (strip)
    df['username'] = df['username'].str.strip()

    #Supprimer les doublons sur player_id username
    df = df.drop_duplicates(subset=['username'])

    # 3. Convertir les dates d’inscription (pd.to_datetime, errors='coerce')
    # Note : Assure-toi que la colonne s'appelle bien registration_date dans ton CSV
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')

    # 4. Remplacer les emails invalides (sans @) par None
    df['email'] = df['email'].where(df['email'].str.contains('@', na=False), None)

    return df


# ============== TRANSFORM SCORES ==============
def transform_scores(df: pd.DataFrame, valid_player_ids: list) -> pd.DataFrame:
    """
    Transforme et nettoie les données des scores selon les 4 règles strictes.
    """
    df = df.copy()

    # 1. Supprimer les doublons sur score_id
    df = df.drop_duplicates(subset=['score_id'])

    # 2. Convertir les dates et les scores en types numériques appropriés
    # On utilise to_datetime pour la date et to_numeric pour le score
    df['played_at'] = pd.to_datetime(df['played_at'], errors='coerce')
    df['score'] = pd.to_numeric(df['score'], errors='coerce')

    # 3. Supprimer les lignes avec un score négatif ou nul
    df = df[df['score'] > 0]

    # 4. Supprimer les scores dont le player_id n’est pas dans valid_player_ids
    df = df[df['player_id'].isin(valid_player_ids)]

    df = df.drop_duplicates(subset=['player_id','game','played_at'])

    return df


