import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models import Player
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

def convert_height(height_str):
    try:
        feet, inches = height_str.split('-')
        return int(feet) * 12 + int(inches)
    except:
        return None
    
def convert_weight(weight_str):
    try:
        return int(weight_str)
    except:
        return None
    
def seed_players():
    db = SessionLocal()

    try:
        active_players = players.get_active_players()

        print(f"Seeding {len(active_players)} active players into the database...")

        for i, player in enumerate(active_players):
            try:
                info = commonplayerinfo.CommonPlayerInfo(player_id=player['id'])
                data = info.get_normalized_dict()['CommonPlayerInfo'][0]

                db_player = Player(
                    id=data['PERSON_ID'],
                    name=data['DISPLAY_FIRST_LAST'],
                    birthdate=data['BIRTHDATE'][:10] if data['BIRTHDATE'] else None,
                    team=data['TEAM_NAME'],
                    position=data['POSITION'],
                    height_inches=convert_height(data['HEIGHT']),
                    weight_lbs=convert_weight(data['WEIGHT'])
                )

                db.merge(db_player)
                db.commit()

                print(f"({i+1}/{len(active_players)}) Saved {data['DISPLAY_FIRST_LAST']}")
                time.sleep(0.5)

            except Exception as e:
                print(f"Error saving player {player['full_name']}: {e}")
                db.rollback()
                continue

    finally:
        db.close()

if __name__ == "__main__":
    seed_players()
