#!/bin/bash

# Stop au premier échec
set -e

echo "========================================"
echo "🚀 Lancement du pipeline GameTracker"
echo "========================================"

# 1️⃣ Attente de la base de données
echo "⏳ [1/4] Attente de la base de données..."
./scripts/wait-for-db.sh
echo "✅ Base de données prête"

# 2️⃣ Initialisation des tables
echo "🗄️  [2/4] Initialisation des tables..."
mysql \
  -h "$DB_HOST" \
  -u "$DB_USER" \
  -p"$DB_PASSWORD" --skip-ssl \
  "$DB_NAME" < ./scripts/init-db.sql
echo "✅ Tables initialisées"

# 3️⃣ Pipeline ETL SANS main.py
echo "🔄 [3/4] Exécution du pipeline ETL..."
python << 'EOF'
import pandas as pd

from src.extract import extract
from src.transform import transform_players, transform_scores
from src.load import load_players, load_scores
from src.database import database_connection

# Paths
players_path = "data/raw/Players.csv"
scores_path = "data/raw/Scores.csv"

print("📥 Extraction...")
df_players = extract(players_path)
df_scores = extract(scores_path)

print("🧹 Transformation des joueurs...")
df_players_clean = transform_players(df_players)
valid_player_ids = df_players_clean["player_id"].tolist()

print("🧹 Transformation des scores...")
df_scores_clean = transform_scores(df_scores, valid_player_ids)

print("📤 Chargement en base...")
with database_connection() as conn:
    load_players(df_players_clean, conn)
    load_scores(df_scores_clean, conn)

print("✅ ETL terminé")
EOF

# 4️⃣ Génération du rapport
echo "📊 [4/4] Génération du rapport..."
python -m src.report
echo "✅ Rapport généré"

echo "========================================"
echo "🎉 Pipeline GameTracker terminé avec succès"
echo "========================================"
