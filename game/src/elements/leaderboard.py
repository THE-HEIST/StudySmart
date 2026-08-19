from game.data_processing_module.config import LangaDB

def show_leaderboard(limit=5):
    data = LangaDB('game/data/leaderboard.json', default_data=[])
    top_player = data.sort_by("score",reverse=True,limit=limit)
    print("\n" + "="*45)
    print("         🏆 LEADERBOARD - TOP DETECTIVES 🏆")
    print("="*45)
    print(f"{'RANK':<6} | {'NAME':<15} | {'SCORE':<7} | {'RANK TITLE'}")
    print("-" * 45)
    if not top_player:
        print("No player found!")
    else:
        for idx, player in enumerate(top_player,1):
            name=player.get("player_name","Unknows")
            score=player.get("score",0)
            rank_title = player.get('rank',"ROOKIE")