# GameTracker - Pipeline ETL

Ce projet automatise l'extraction, le nettoyage et l'analyse de données de jeux vidéo.

## Architecture
- **Docker Compose** : Orchestration MySQL 8.0 et App Python 3.11.
- **Python (Pandas)** : Nettoyage des données et gestion des types.
- **Bash** : Automatisation du pipeline et attente de la base de données.

Markdown
# GameTracker - Pipeline ETL Automatisé

Ce projet implémente un pipeline complet d'Extraction, Transformation et Chargement (ETL) pour les données de performance de la startup GameTracker.

## 1. Prérequis techniques
* **Docker** (version 20.10+)
* **Docker Compose** (version 2.0+)
* **Client Git**
* Connexion internet (pour le build initial des images)

## 2. Structure du projet
```text
.
├── data/               # Fichiers CSV sources (Players.csv, Scores.csv)
├── database/           # Volume de données MySQL (créé au lancement)
├── output/             # Contient le rapport final (rapport.txt)
├── scripts/            # Scripts Bash d'automatisation
│   ├── init-db.sql     # Schéma de la base de données
│   ├── wait-for-db.sh  # Script de vérification de disponibilité MySQL
│   └── run_pipeline.sh # Script maître d'automatisation
├── src/                # Code source Python
│   ├── config.py       # Gestion des variables d'environnement
│   ├── database.py     # Connexion et Context Manager
│   ├── extract.py      # Module d'extraction des CSV
│   ├── transform.py    # Module de nettoyage (Pandas)
│   ├── load.py         # Module de chargement MySQL
│   ├── report.py       # Module de génération de statistiques
│   └── main.py         # Orchestrateur du pipeline
├── docker-compose.yml  # Orchestration multi-conteneurs
└── Dockerfile          # Configuration de l'image Python

### 3. Probléme qualité 

1.Doublons : certains joueurs et scores apparaissent plusieurs fois
2. Emails invalides : certains emails ne contiennent pas de @
3. Dates incohérentes : formats variés (2023-06-15, 15/03/2023, date_inconnue, 30-02-2024)
4. Espaces parasites : espaces en début/fin de certains username
5. Scores négatifs : certains scores sont négatifs (aberrants)
6. Valeurs manquantes : certains champs email ou score sont vides
7. Références orphelines : certains scores réfèrent à un player_id qui n’existe pas dansPlayers.csv

