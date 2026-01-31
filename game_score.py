player_name = input("enter player name: ")
games_played_str = input("enter number of games played: ")
total_score_str = input("enter total score: ")

games_played = int(games_played_str)
total_score = int(total_score_str)

average_score = total_score / games_played

#output display

print("\n=====players score summary=====")
print(f"Player: {player_name}")
print(f"Games played: {games_played}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")
print("=================================================")