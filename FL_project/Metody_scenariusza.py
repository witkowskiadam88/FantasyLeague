import json
import Players_module

"""wytlumaczenie importowania jsona: https://www.tech-otaku.com/mac/using-python-to-loop-through-json-encoded-data/ """

def player_function(position):
    file_path = open("fantasyleague/FL_project/players_dict.json")
    players_dict_json_file = json.load(file_path)

    print("\n",position,":")
    for player_step in players_dict_json_file["players"][position]:
        print(player_step.upper(),"(", players_dict_json_file["players"][position][player_step]["skill"], ")")
        for key, value in players_dict_json_file["players"][position][player_step].items():
            print(key, ":", value)
        print("####################")

    file_path.close()


def player_choice_function():
    print("Wybierz gracza")
    player_input = input()
    player_picked = Players_module.Players.player_create_object(player_input, None, None, None, None, None, None, None,None)
    return player_picked



def team_name_input():
    print("Wpisz nazwe zespolu")
    team_name = input()


def create_team():
    team = []
    return team
        

    