import datetime
from src.database import database_connection

def generate_report():
    """Génère un rapport de synthèse complet dans output/rapport.txt."""
    print("Étape 4.1 : Génération du rapport de synthèse...")

    try:
        with database_connection() as conn:
            cursor = conn.cursor()

            # 1. Statistiques générales [cite: 142]
            cursor.execute("SELECT COUNT(*) FROM players")
            nb_players = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM scores")
            nb_scores = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(DISTINCT game) FROM scores")
            nb_games = cursor.fetchone()[0]

            # 2. Top 5 des meilleurs scores avec pseudo et nom du jeu [cite: 143]
            query_top5 = """
                SELECT p.username, s.game, s.score 
                FROM scores s
                JOIN players p ON s.player_id = p.player_id
                ORDER BY s.score DESC
                LIMIT 5
            """
            cursor.execute(query_top5)
            top5 = cursor.fetchall()

            # 3. Score moyen par jeu [cite: 144]
            cursor.execute("SELECT game, AVG(score) FROM scores GROUP BY game")
            avg_scores = cursor.fetchall()

            # 4. Répartition des joueurs par pays [cite: 145]
            cursor.execute("SELECT country, COUNT(*) FROM players GROUP BY country ORDER BY COUNT(*) DESC")
            players_country = cursor.fetchall()

            # 5. Répartition des sessions par plateforme [cite: 146]
            cursor.execute("SELECT platform, COUNT(*) FROM scores GROUP BY platform ORDER BY COUNT(*) DESC")
            platform_dist = cursor.fetchall()

        # Écriture dans le fichier output/rapport.txt [cite: 139, 149]
        with open("output/rapport.txt", "w", encoding="utf-8") as f:
            f.write("====================================================\n")
            f.write("GAMETRACKER - Rapport de synthese\n")
            f.write(f"Genere le : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("====================================================\n\n")

            f.write("--- Statistiques generales ---\n")
            f.write(f"Nombre de joueurs : {nb_players}\n")
            f.write(f"Nombre de scores : {nb_scores}\n")
            f.write(f"Nombre de jeux : {nb_games}\n\n")

            f.write("--- Top 5 des meilleurs scores ---\n")
            for i, (user, game, score) in enumerate(top5, 1):
                f.write(f"{i}. {user} | {game} | {score}\n")
            f.write("\n")

            f.write("--- Score moyen par jeu ---\n")
            for game, avg in avg_scores:
                f.write(f"{game} : {avg:.1f}\n")
            f.write("\n")

            f.write("--- Joueurs par pays ---\n")
            for country, count in players_country:
                f.write(f"{country if country else 'Inconnu'} : {count}\n")
            f.write("\n")

            f.write("--- Sessions par plateforme ---\n")
            for plat, count in platform_dist:
                f.write(f"{plat if plat else 'Autre'} : {count}\n")
            
            f.write("====================================================\n")

        print("✅ Rapport généré avec succès dans output/rapport.txt[cite: 221].")

    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")
        raise # Permet au script Bash de s'arrêter en cas d'erreur [cite: 202]

if __name__ == "__main__":
    generate_report()