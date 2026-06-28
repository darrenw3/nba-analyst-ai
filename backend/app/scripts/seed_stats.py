import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models import Player, SeasonStats
from nba_api.stats.endpoints import playercareerstats
    
def seed_stats():
    db = SessionLocal()

    try:
        players = db.query(Player).all()
        print(f"Seeding season stats for {len(players)} players into the database...")

        for i, player in enumerate(players):
            try:
                stats = playercareerstats.PlayerCareerStats(player_id=player.id)
                data = stats.get_normalized_dict()['SeasonTotalsRegularSeason']

                for season in data:
                    gp = season['GP']
                    if gp == 0:
                        continue

                    db_stats = SeasonStats(
                        player_id=player.id,
                        season=season['SEASON_ID'],
                        games_played=gp,
                        minutes_per_game=round(season['MIN'] / gp, 1),
                        points_per_game=round(season['PTS'] / gp, 1),
                        rebounds_per_game=round(season['REB'] / gp, 1),
                        assists_per_game=round(season['AST'] / gp, 1),
                        steals_per_game=round(season['STL'] / gp, 1),
                        blocks_per_game=round(season['BLK'] / gp, 1),
                        field_goal_percentage=season['FG_PCT'],
                        three_point_percentage=season['FG3_PCT'],
                        free_throw_percentage=season['FT_PCT']
                    )

                    db.add(db_stats)

                db.commit()
                print(f"({i+1}/{len(players)}) Saved stats for {player.name}")
                time.sleep(0.5)

            except Exception as e:
                print(f"Error seeding stats for {player.name}: {e}")
                db.rollback()
                continue


    finally:
        db.close()

if __name__ == "__main__":
    seed_stats()
